# coding=gbk
import cv2 as cv
import numpy as np

file_path = "../images/好.jpg"
# 直接读取中文路径会报错
# img = cv.imread(file_path)
# 设置可以读取中文路径的图片
img = cv.imdecode(np.fromfile(file_path, dtype=np.uint8), 1)
cv.imshow("value", img)
cv.waitKey(10000)