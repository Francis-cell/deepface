# coding=gbk
import cv2 as cv
import numpy as np

file_path = "../images/��.jpg"
# ֱ�Ӷ�ȡ����·���ᱨ��
# img = cv.imread(file_path)
# ���ÿ��Զ�ȡ����·����ͼƬ
img = cv.imdecode(np.fromfile(file_path, dtype=np.uint8), 1)
cv.imshow("value", img)
cv.waitKey(10000)