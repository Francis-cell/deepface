# coding=gbk
import cv2 as cv
import os

img_path = "../images/1.jpg"
# ����ͼƬ
img = cv.imread(img_path)
print(img)
# ͼƬչʾ
# cv.imshow('result_01', img)
# ͼ��չʾʱ�䣬��λ:����(ms)
# cv.waitKey(10000)
# ͼƬ����
save_path = "C:/Users/86185/Desktop/save/"
cv.imwrite(save_path + "save.jpg", img)