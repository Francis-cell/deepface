# coding=gbk
import deepface.DeepFace
import matplotlib.pyplot as plt


''' 这个方法主要的目的是将图片先处理一遍，调为正脸以提高准确率 '''
def deal_with_picture(img_path, detector_backend='retinaface'):
    face = deepface.DeepFace.detectFace(img_path=img_path, target_size=(500, 500), detector_backend=detector_backend)
    # 获取原本的图片名称
    real_name = img_path.split("/")[-1]
    plt.imsave("../savePictures/" + real_name, face)
    print("图片", real_name, "运行成功！")