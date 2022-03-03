# coding=gbk
import cv2 as cv
import numpy as np
import torchvision.transforms as transorms

def cv2_imwrite():
    # --------模拟图片的tensor数据--------
    # 指定读取的图片路径
    input_path = "../database/ZhangHanyun/1.jpg"
    # 读取图片，图片默认被读取的格式为(height, width, channel)
    img = cv.imread(input_path)
    # 图像转为tensor，此时图片变为（channel, height, width），并将0-255归一化为0-， 减小计算
    input_transform = transorms.Compose([
        transorms.ToTensor()
    ])

    # unsqueeze(0)：是在扩展维度由三维扩展为4维，(bathch_size, channel, height, width)
    # 这是实际实验中可能遇到，所以我才扩展维度的，也可以不扩展
    img = input_transform(img).unsqueeze(0)

    # =============== 数据准备完成，开始保存 ============ #
    # 1.首先将tensor降维度，4维降为3维:image.squeeze(0)
    # 2.tensor转为numpy:image.squeeze(0).numpy()
    # 3.转换维度，由（channel, height, width）变为（height, width, channel）
    # 4.数据类型由numpy转换维np.uint8（这是图片应有的格式）
    # 5.保存图片，执行函数cv2.imwrite(filename, img),filename:保存路径名要, img:保存的图片
    img = np.transpose(img.squeeze(0).numpy() * 255.0, (1, 2, 0)).astype(np.uint8)
    save_path = "C:/Users/86185/Desktop/save/"
    cv.imwrite(save_path + "zhang.jpg", img)


if __name__ == '__main__':
    cv2_imwrite()