# coding=gbk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# ��ȡͼƬ
img_path = "./images/1.jpg"
img = mpimg.imread(img_path)
# չʾͼƬ
plt.imshow(img)
plt.show()
