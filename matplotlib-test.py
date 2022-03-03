# coding=gbk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 读取图片
img_path = "./images/1.jpg"
img = mpimg.imread(img_path)
# 展示图片
plt.imshow(img)
plt.show()
