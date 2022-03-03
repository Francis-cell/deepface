# coding=gbk
import cv2 as cv
import numpy as np
import torchvision.transforms as transorms

def cv2_imwrite():
    # --------ģ��ͼƬ��tensor����--------
    # ָ����ȡ��ͼƬ·��
    input_path = "../database/ZhangHanyun/1.jpg"
    # ��ȡͼƬ��ͼƬĬ�ϱ���ȡ�ĸ�ʽΪ(height, width, channel)
    img = cv.imread(input_path)
    # ͼ��תΪtensor����ʱͼƬ��Ϊ��channel, height, width��������0-255��һ��Ϊ0-�� ��С����
    input_transform = transorms.Compose([
        transorms.ToTensor()
    ])

    # unsqueeze(0)��������չά������ά��չΪ4ά��(bathch_size, channel, height, width)
    # ����ʵ��ʵ���п��������������Ҳ���չά�ȵģ�Ҳ���Բ���չ
    img = input_transform(img).unsqueeze(0)

    # =============== ����׼����ɣ���ʼ���� ============ #
    # 1.���Ƚ�tensor��ά�ȣ�4ά��Ϊ3ά:image.squeeze(0)
    # 2.tensorתΪnumpy:image.squeeze(0).numpy()
    # 3.ת��ά�ȣ��ɣ�channel, height, width����Ϊ��height, width, channel��
    # 4.����������numpyת��άnp.uint8������ͼƬӦ�еĸ�ʽ��
    # 5.����ͼƬ��ִ�к���cv2.imwrite(filename, img),filename:����·����Ҫ, img:�����ͼƬ
    img = np.transpose(img.squeeze(0).numpy() * 255.0, (1, 2, 0)).astype(np.uint8)
    save_path = "C:/Users/86185/Desktop/save/"
    cv.imwrite(save_path + "zhang.jpg", img)


if __name__ == '__main__':
    cv2_imwrite()