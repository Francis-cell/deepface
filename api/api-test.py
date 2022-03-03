# coding=gbk
import warnings
import sys

sys.path.append('..')
from utils import img_base64 as ib64
from utils import json_format

warnings.filterwarnings("ignore")

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# ------------------------------

from flask import Flask, jsonify, request, make_response

import argparse
import uuid
import json
import time
from tqdm import tqdm

# ------------------------------

import tensorflow as tf

tf_version = int(tf.__version__.split(".")[0])

# ------------------------------

if tf_version == 2:
    import logging

    tf.get_logger().setLevel(logging.ERROR)

# ------------------------------

from deepface import DeepFace

# ------------------------------

app = Flask(__name__)

# ------------------------------

if tf_version == 1:
    graph = tf.get_default_graph()


# ------------------------------
# Service API Interface

@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'


@app.route('/analyze', methods=['POST'])
def analyze():
    global graph

    tic = time.time()
    req = request.get_json()
    trx_id = uuid.uuid4()

    # ---------------------------

    if tf_version == 1:
        with graph.as_default():
            resp_obj = analyzeWrapper(req, trx_id)
    elif tf_version == 2:
        resp_obj = analyzeWrapper(req, trx_id)

    # ---------------------------

    toc = time.time()

    resp_obj["trx_id"] = trx_id
    resp_obj["seconds"] = toc - tic

    return resp_obj, 200


def analyzeWrapper(req, trx_id=0):
    resp_obj = jsonify({'success': False})

    instances = []
    if "img" in list(req.keys()):
        raw_content = req["img"]  # list

        for item in raw_content:  # item is in type of dict
            instances.append(item)

    if len(instances) == 0:
        return jsonify({'success': False, 'error': 'you must pass at least one img object in your request'}), 205

    print("Analyzing ", len(instances), " instances")

    # ---------------------------

    detector_backend = 'opencv'

    actions = ['emotion', 'age', 'gender', 'race']

    if "actions" in list(req.keys()):
        actions = req["actions"]

    if "detector_backend" in list(req.keys()):
        detector_backend = req["detector_backend"]

    # ---------------------------

    try:
        resp_obj = DeepFace.analyze(instances, actions=actions)
    except Exception as err:
        print("Exception: ", str(err))
        return jsonify({'success': False, 'error': str(err)}), 205

    # ---------------
    # print(resp_obj)
    return resp_obj


# =============对比两张图片相似度=============
@app.route('/verify', methods=['POST'])
def verify():
    global graph

    tic = time.time()
    req = request.get_json()
    trx_id = uuid.uuid4()

    resp_obj = jsonify({'success': False})

    if tf_version == 1:
        with graph.as_default():
            resp_obj = verifyWrapper(req, trx_id)
    elif tf_version == 2:
        resp_obj = verifyWrapper(req, trx_id)

    # --------------------------

    toc = time.time()

    resp_obj["trx_id"] = trx_id
    resp_obj["seconds"] = toc - tic

    return resp_obj, 200


def verifyWrapper(req, trx_id=0):
    resp_obj = jsonify({'success': False})

    model_name = "VGG-Face";
    distance_metric = "cosine";
    detector_backend = "opencv"
    if "model_name" in list(req.keys()):
        model_name = req["model_name"]
    if "distance_metric" in list(req.keys()):
        distance_metric = req["distance_metric"]
    if "detector_backend" in list(req.keys()):
        detector_backend = req["detector_backend"]

    # ----------------------

    instances = []
    if "img" in list(req.keys()):
        raw_content = req["img"]  # list

        for item in raw_content:  # item is in type of dict
            instance = []
            img1 = item["img1"];
            img2 = item["img2"]

            validate_img1 = False
            if len(img1) > 11 and img1[0:11] == "data:image/":
                validate_img1 = True

            validate_img2 = False
            if len(img2) > 11 and img2[0:11] == "data:image/":
                validate_img2 = True

            if validate_img1 != True or validate_img2 != True:
                return jsonify(
                    {'success': False, 'error': 'you must pass both img1 and img2 as base64 encoded string'}), 205

            instance.append(img1);
            instance.append(img2)
            instances.append(instance)

    # --------------------------

    if len(instances) == 0:
        return jsonify({'success': False, 'error': 'you must pass at least one img object in your request'}), 205

    print("Input request of ", trx_id, " has ", len(instances), " pairs to verify")

    # --------------------------

    try:
        resp_obj = DeepFace.verify(instances
                                   , model_name=model_name
                                   , distance_metric=distance_metric
                                   , detector_backend=detector_backend
                                   )

        if model_name == "Ensemble":  # issue 198.
            for key in resp_obj:  # issue 198.
                resp_obj[key]['verified'] = bool(resp_obj[key]['verified'])

    except Exception as err:
        resp_obj = jsonify({'success': False, 'error': str(err)}), 205
    print("===============OK==============")
    print("resp_obj的类型为：", type(resp_obj))
    return resp_obj


@app.route('/represent', methods=['POST'])
def represent():
    global graph

    tic = time.time()
    req = request.get_json()
    trx_id = uuid.uuid4()

    resp_obj = jsonify({'success': False})

    if tf_version == 1:
        with graph.as_default():
            resp_obj = representWrapper(req, trx_id)
    elif tf_version == 2:
        resp_obj = representWrapper(req, trx_id)

    # --------------------------

    toc = time.time()

    resp_obj["trx_id"] = trx_id
    resp_obj["seconds"] = toc - tic

    return resp_obj, 200


def representWrapper(req, trx_id=0):
    resp_obj = jsonify({'success': False})

    # -------------------------------------
    # find out model

    model_name = "VGG-Face";
    distance_metric = "cosine";
    detector_backend = 'opencv'

    if "model_name" in list(req.keys()):
        model_name = req["model_name"]

    if "detector_backend" in list(req.keys()):
        detector_backend = req["detector_backend"]

    # -------------------------------------
    # retrieve images from request

    img = ""
    if "img" in list(req.keys()):
        img = req["img"]  # list
    # print("img: ", img)

    validate_img = False
    if len(img) > 11 and img[0:11] == "data:image/":
        validate_img = True

    if validate_img != True:
        print("invalid image passed!")
        return jsonify({'success': False, 'error': 'you must pass img as base64 encoded string'}), 205

    # -------------------------------------
    # call represent function from the interface

    try:

        embedding = DeepFace.represent(img
                                       , model_name=model_name
                                       , detector_backend=detector_backend
                                       )

    except Exception as err:
        print("Exception: ", str(err))
        resp_obj = jsonify({'success': False, 'error': str(err)}), 205

    # -------------------------------------

    # print("embedding is ", len(embedding)," dimensional vector")
    resp_obj = {}
    resp_obj["embedding"] = embedding

    # -------------------------------------

    return resp_obj


# ============将传入的图片和一个图片文件夹中的图片进行比对============
@app.route('/find', methods=['POST'])
def find():
    global graph

    tic = time.time()
    req = request.get_json()
    trx_id = uuid.uuid4()

    resp_obj = jsonify({'success': False})

    if tf_version == 1:
        with graph.as_default():
            resp_obj = findWrapper(req, trx_id)
    elif tf_version == 2:
        resp_obj = findWrapper(req, trx_id)

    # --------------------------
    toc = time.time()
    resp_obj["trx_id"] = trx_id
    resp_obj["seconds"] = toc - tic
    return resp_obj, 200


def findWrapper(req, trx_id=0):
    resp_obj = jsonify({'success': False})
    # 默认采用的模型是"VGG-Face"
    model_name = "VGG-Face"
    # 此处选择的对比的文件夹位置
    db_path = "../facePictures"
    # 默认使用余弦规则
    distance_metric = "cosine"

    if "model_name" in list(req.keys()):
        model_name = req["model_name"]
    if "db_path" in list(req.keys()):
        db_path = req["db_path"]
    if "distance_metric" in list(req.keys()):
        distance_metric = req["distance_metric"]

    # ----------------------
    instances = []
    if "img" in list(req.keys()):
        raw_content = req["img"]  # list

        for item in raw_content:  # item is in type of dict
            item = item.split(",")[1]
            # base64解码
            img_name = "img.jpg"
            img_save_path = "../savePictures/"
            ib64.base64_to_img(img_Name=img_name, img_save_path=img_save_path, img_base64=item)
            instances.append(item)
            img_after_path = "../savePictures/img.jpg"

    if len(instances) == 0:
        return jsonify({'success': False, 'error': 'you must pass at least one img object in your request'})

    print("要分析的图片的数量为：", len(instances))

    # --------------------------
    try:
        resp_obj = DeepFace.find(
            img_path=img_after_path,
            db_path=db_path,
            model_name=model_name,
            distance_metric=distance_metric
        )
        # 将原本转换的结果转换成str格式的，方便进行数据清洗
        last_resp_obj = str(resp_obj)
        # 进行数据清洗
        a = last_resp_obj.split(" ")
        # 进行数据清洗，将a中' '元素全部去掉（这里目前有些问题，后续解决）
        b = []
        for i in range(len(a)):
            if a[i] != "":
                # b中的偶数位是需要进行处理的，末尾多了(\n+一个数字)
                if len(b) % 2 != 0 and i != (len(a) - 1):
                    b.append(a[i][:len(a[i]) - 2])
                else:
                    b.append(a[i])

        last_value = json_format.json_format_find_out(b)

    except Exception as err:
        print("Exception: ", str(err))
        return jsonify({'success': False, 'error': str(err)}), 205

    return last_value

# ================接收并处理来自后台的图片的base64编码==============
@app.route('/getBase64Code', methods=['POST'])
def get_base64_code():
    req = request.get_json()

    # ------------保存图片--------------
    try:
        # 1、接收到后端传来的图片的base64的编码
        # print("req的值是：", req)
        req_base64 = str(req.get("base64Code")).split("\'")[1]
        # 获取图片的名称
        img_name = str(req.get("photoName")) + ".jpg"
        # 指定图片保存路径
        img_save_path = "../facePictures/"

        # 2、将这个base64编码解码成图片格式，然后保存到指定的文件夹下
        ib64.base64_to_img(img_name=img_name, img_save_path=img_save_path, img_base64=req_base64)

        # 保存成功
        resp_obj = jsonify({'success': True})
    except Exception as err:
        return jsonify({'success': False}), 205

    return resp_obj, 200





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=5000,
        help='Port of serving api')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port)
