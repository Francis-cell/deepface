# coding=gbk
import cv2 as cv
import os

img_path = "../images/1.jpg"
# 加载图片
img = cv.imread(img_path)
print(img)
# 图片展示
# cv.imshow('result_01', img)
# 图像展示时间，单位:毫秒(ms)
# cv.waitKey(10000)
# 图片保存
save_path = "C:/Users/86185/Desktop/save/"
cv.imwrite(save_path + "save.jpg", img)