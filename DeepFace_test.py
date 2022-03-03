# coding=gbk
from deepface import DeepFace
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import json

# 模型选择
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace"]

# 指标选择(相似度选择的指标)
# cosine: 余弦、 euclidean: 欧几里得、 euclidean_l2: 欧几里得l2
metrics = ["cosine", "euclidean", "euclidean_l2"]
backends = ['opencv', 'mtcnn', 'retinaface']

# # 比较两张图片中的人脸的相似度
# '''
# verify参数说明：
# 1、model_name---》人脸识别算法选择【目前测试能够使用的有："VGG-Face"(默认值), "Facenet", "Facenet512", "OpenFace"】【其中"Facenet"相对比较准确些】
# 2、distance_metric---》相似度指标的选择【"cosine"(默认值), "euclidean", "euclidean_l2"】
# '''
# print("============人脸的相似度比较==============")
# img1_path = "./database/ZhangHanyun/3.jpg"
# img2_path = "./database/ZhangHanyun/2.jpg"
# result = DeepFace.verify(img1_path = "./images/3.jpg", img2_path = "./images/2.jpg", model_name=models[3], distance_metric= metrics[2])
# result = DeepFace.verify(img1_path, img2_path, model_name=models[0], distance_metric= metrics[2], detector_backend=backends[2])
# print(result)
# # 排序并且缩进两个字符输出
# print(json.dumps(result, sort_keys=True, indent=2))


#
# # 在一组图片中按人脸相似度(要进行比较的这样图片和图片库里的图片)将图片进行排序
print("============寻找图片库中的人脸相似匹配度==============")
df = DeepFace.find(img_path = "./images/3.jpg", db_path = "./database/DiLiReBa", model_name=models[3], distance_metric= metrics[2])
print(df)
#
#
# # 分析人脸的面部属性
# '''
# analyze参数说明：
# 1、actions
#     age--年龄、emotion--感情、gender--性别、race--种族
# '''
# print("============寻找图片中人脸的面部属性==============")
# img_path = "./image-1/9.jpg"
# obj = DeepFace.analyze(img_path=img_path, actions= ['age', 'emotion', 'gender', 'race'])
# print(obj)
#
#
# # 流和实时分析
# print("============流和实时分析==============")
# video_source = "./video/1.mp4"
# value = DeepFace.stream(db_path="./database", source=video_source)
# print(value)
#
#
# # 人脸检测器的选择
# # 目前没有找到资源的人脸监测器： 'ssd', 'dlib']
# backends = ['opencv','mtcnn', 'retinaface']
# print("============人脸的相似度比较==============")
# result = DeepFace.verify(img1_path = "./images/3.jpg", img2_path = "./images/2.jpg", detector_backend=backends[1])
# print(result)
#
#
# 检测人脸
# print("============检测人脸==============")
# backends = ['opencv', 'mtcnn', 'retinaface'] # 'ssd', 'dlib'目前不能使用
# image_path = "./database/ZhangHanyun/1.jpg"
# # image_path = "./images/many1.jpg"
# face = DeepFace.detectFace(img_path=image_path, target_size=(500, 500), detector_backend=backends[2])
# print(face)
# 将face的内容作为输出写入到fileSave.txt文本中
# file = open("./fileSave.txt", "w")
# strings = str(face)
# file.write(strings)
# file.close()
#
# 将face作为一张图片输出出来(OpenCV图片的编码方式是rgb的，但是返回结果face变成了bgr的，所以这里要调整回rgb的才会是彩色的)
# cv.imshow('result', face[:, :, ::-1])
# cv.waitKey(10000)
# plt.imshow(face)
# plt.show()
# save_path = "C:/Users/86185/Desktop/save/"
# plt.imsave(save_path + "/zhang.jpg", face)
# 将face作为一张图片保存到指定的路径下(当前是失败的)
# save_path = "C:/Users/86185/Desktop/save/"
# cv.imwrite(save_path + "face.jpg", face)


# print("============检测人脸==============")
# backends = ['opencv', 'mtcnn', 'retinaface']
# image_path = "./images/many1.jpg"
# for i in range(0, 9):
#     face = DeepFace.detectFace(img_path=image_path, target_size=(500, 500), detector_backend=backends[0])
#     cv.imshow('result', face)
#     cv.waitKey(3000)
#     print(i)



# print("============人脸向量检测==============")
# result = DeepFace.represent(img_path="./images/3.jpg", model_name=models[1])
# print(result)
























































