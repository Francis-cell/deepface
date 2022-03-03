# coding=gbk
from deepface import DeepFace
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import json

# ģ��ѡ��
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace"]

# ָ��ѡ��(���ƶ�ѡ���ָ��)
# cosine: ���ҡ� euclidean: ŷ����á� euclidean_l2: ŷ�����l2
metrics = ["cosine", "euclidean", "euclidean_l2"]
backends = ['opencv', 'mtcnn', 'retinaface']

# # �Ƚ�����ͼƬ�е����������ƶ�
# '''
# verify����˵����
# 1��model_name---������ʶ���㷨ѡ��Ŀǰ�����ܹ�ʹ�õ��У�"VGG-Face"(Ĭ��ֵ), "Facenet", "Facenet512", "OpenFace"��������"Facenet"��ԱȽ�׼ȷЩ��
# 2��distance_metric---�����ƶ�ָ���ѡ��"cosine"(Ĭ��ֵ), "euclidean", "euclidean_l2"��
# '''
# print("============���������ƶȱȽ�==============")
# img1_path = "./database/ZhangHanyun/3.jpg"
# img2_path = "./database/ZhangHanyun/2.jpg"
# result = DeepFace.verify(img1_path = "./images/3.jpg", img2_path = "./images/2.jpg", model_name=models[3], distance_metric= metrics[2])
# result = DeepFace.verify(img1_path, img2_path, model_name=models[0], distance_metric= metrics[2], detector_backend=backends[2])
# print(result)
# # ���������������ַ����
# print(json.dumps(result, sort_keys=True, indent=2))


#
# # ��һ��ͼƬ�а��������ƶ�(Ҫ���бȽϵ�����ͼƬ��ͼƬ�����ͼƬ)��ͼƬ��������
print("============Ѱ��ͼƬ���е���������ƥ���==============")
df = DeepFace.find(img_path = "./images/3.jpg", db_path = "./database/DiLiReBa", model_name=models[3], distance_metric= metrics[2])
print(df)
#
#
# # �����������沿����
# '''
# analyze����˵����
# 1��actions
#     age--���䡢emotion--���顢gender--�Ա�race--����
# '''
# print("============Ѱ��ͼƬ���������沿����==============")
# img_path = "./image-1/9.jpg"
# obj = DeepFace.analyze(img_path=img_path, actions= ['age', 'emotion', 'gender', 'race'])
# print(obj)
#
#
# # ����ʵʱ����
# print("============����ʵʱ����==============")
# video_source = "./video/1.mp4"
# value = DeepFace.stream(db_path="./database", source=video_source)
# print(value)
#
#
# # �����������ѡ��
# # Ŀǰû���ҵ���Դ������������� 'ssd', 'dlib']
# backends = ['opencv','mtcnn', 'retinaface']
# print("============���������ƶȱȽ�==============")
# result = DeepFace.verify(img1_path = "./images/3.jpg", img2_path = "./images/2.jpg", detector_backend=backends[1])
# print(result)
#
#
# �������
# print("============�������==============")
# backends = ['opencv', 'mtcnn', 'retinaface'] # 'ssd', 'dlib'Ŀǰ����ʹ��
# image_path = "./database/ZhangHanyun/1.jpg"
# # image_path = "./images/many1.jpg"
# face = DeepFace.detectFace(img_path=image_path, target_size=(500, 500), detector_backend=backends[2])
# print(face)
# ��face��������Ϊ���д�뵽fileSave.txt�ı���
# file = open("./fileSave.txt", "w")
# strings = str(face)
# file.write(strings)
# file.close()
#
# ��face��Ϊһ��ͼƬ�������(OpenCVͼƬ�ı��뷽ʽ��rgb�ģ����Ƿ��ؽ��face�����bgr�ģ���������Ҫ������rgb�ĲŻ��ǲ�ɫ��)
# cv.imshow('result', face[:, :, ::-1])
# cv.waitKey(10000)
# plt.imshow(face)
# plt.show()
# save_path = "C:/Users/86185/Desktop/save/"
# plt.imsave(save_path + "/zhang.jpg", face)
# ��face��Ϊһ��ͼƬ���浽ָ����·����(��ǰ��ʧ�ܵ�)
# save_path = "C:/Users/86185/Desktop/save/"
# cv.imwrite(save_path + "face.jpg", face)


# print("============�������==============")
# backends = ['opencv', 'mtcnn', 'retinaface']
# image_path = "./images/many1.jpg"
# for i in range(0, 9):
#     face = DeepFace.detectFace(img_path=image_path, target_size=(500, 500), detector_backend=backends[0])
#     cv.imshow('result', face)
#     cv.waitKey(3000)
#     print(i)



# print("============�����������==============")
# result = DeepFace.represent(img_path="./images/3.jpg", model_name=models[1])
# print(result)
























































