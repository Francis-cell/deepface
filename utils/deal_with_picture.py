# coding=gbk
import deepface.DeepFace
import matplotlib.pyplot as plt


''' ���������Ҫ��Ŀ���ǽ�ͼƬ�ȴ���һ�飬��Ϊ���������׼ȷ�� '''
def deal_with_picture(img_path, detector_backend='retinaface'):
    face = deepface.DeepFace.detectFace(img_path=img_path, target_size=(500, 500), detector_backend=detector_backend)
    # ��ȡԭ����ͼƬ����
    real_name = img_path.split("/")[-1]
    plt.imsave("../savePictures/" + real_name, face)
    print("ͼƬ", real_name, "���гɹ���")