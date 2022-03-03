# coding=gbk
import img_base64
import json_format
import deal_with_picture

'''����ģ�͵�ѡ��(Ĭ�ϸ���VGG-Face��ֵ); img1��·��; img2��·��'''


def build_json_data(img1_path, img2_path, model_change="VGG-Face"):
    # ��ͼƬ1ת����base64�ı����ʽ�����
    img1_base64 = img_base64.img_base64(img1_path)
    # ��ͼƬ2ת����base64�ı����ʽ�����
    img2_base64 = img_base64.img_base64(img2_path)
    # ����Postman�п���ʹ�õ�json��ʽ������
    last_json = json_format.json_format(model_change, img1_base64, img2_base64)
    return last_json


'''�ȶ� һ��ͼƬ�����ƶ�'''


# ��������˵����
# 1��img1_path, img2_path��ͼƬ·����
# 2��models���������ɵ�json����ʱѡ���ģ��
def context_pair_pictures(img1_path, img2_path, models="VGG-Face"):
    # 1������ͼƬ
    deal_with_picture.deal_with_picture(img1_path)
    deal_with_picture.deal_with_picture(img2_path)
    # �ġ�ʹ�ô���֮���ͼƬ·��
    img_save_path = "../savePictures/"
    img1_real_name = img1_path.split("/")[-1]
    img1_path = img_save_path + img1_real_name
    # print("img1_path��ֵΪ��", img1_path)
    img2_real_name = img2_path.split("/")[-1]
    img2_path = img_save_path + img2_real_name
    # print("img2_path��ֵΪ��", img2_path)
    # �塢�������յ�json�������
    last_value = build_json_data(img1_path=img1_path, img2_path=img2_path, model_change=models)
    # ������������浽һ���ļ��У����㸴�ƻ�ȡ
    file = open("../output.txt", "w")
    file.write(last_value)
    file.close()
    print("���н���")


'''��һ��ͼƬ�в��ҵ�ǰ�����ͼƬ���ˣ��Ƿ�����һȺ���д���'''


# ��������˵����
# 1��models���������ɵ�json����ʱѡ���ģ��
# 2��img_path��Ҫ�ȶԵ�ͼƬ��·��
def context_one_many(models, img_path):
    # 1���������ͼƬ�����base64�������ʽ
    img_with_base64 = img_base64.img_base64(img_path=img_path)
    # 2��������Ҫ��json��ʽ������
    img_json = json_format.json_format_find(model=models, img_base64=img_with_base64)
    # print(img_json)
    # 3���������json���ݱ��浽һ��txt�ļ�����ȥ
    file = open("../output.txt", "w")
    file.write(img_json)
    file.close()
    print("���н���������")


'''����һ��ͼƬ��base64�ı���'''


# ��������˵����
# img_path��Ҫ����json���ݵ�ͼƬ��·��
def context_one_base64(img_path):
    # ������ͼƬת����base64�����ʽ
    imgBase64 = img_base64.img_base64(img_path=img_path)
    # ����һ������
    imgBase64 = imgBase64.split(",")[1]
    # ��ȡ�˴���ͼƬ������
    imgName = img_path.split("/")[-1].split(".")[0]
    # print("imgName��ֵΪ��", imgName)
    # ��ͼƬ��base64�ı���ת������Ҫ��json��ʽ
    last_value = json_format.json_format_getBase64Code(imgName, imgBase64)
    # �������Ҫ��json��ʽ��ͼƬ�ı��뱣�浽ָ�����ļ��ڣ����㸴��ʹ��
    file = open("../output.txt", "w")
    file.write(last_value)
    file.close()
    print("���н���!")


if __name__ == "__main__":
    # # һ��һ��ͼƬ�ıȶԲ���
    # models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace"]
    # img1_path = "../database/ZhangHanyun/3.jpg"
    # img2_path = "../database/ZhangHanyun/2.jpg"
    # context_pair_pictures(img1_path=img1_path, img2_path=img2_path, models=models[0])

    # # ������һ��ͼƬ��һ��ͼƬ��Ѱ�������ƵĽ��
    # # models = ["VGG-Face", "Facenet"]
    # models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace"]
    # # Ҫ�ȶԵ�ͼƬ��·��
    # img_path = "../database/ZhangHanyun/3.jpg"
    # # Ҫ���ȶԵĴ�����ͼƬ�Ĵ洢·��
    # # imgs_path = "../database/ZhangHanyun/"
    # context_one_many(models=models, img_path=img_path)

    # ��������һ��ͼƬ��base64�ı���
    # # Ҫ����json���ݵ�ͼƬ��·��
    # img_path = "../database/ZhangHanyun/3.jpg"
    # # ������Ҫ��json����
    # context_one_base64(img_path=img_path)


    # ��ʱ���ԣ�����ɾ����
    img_name = "test.jpg"
    img_save_path = "../savePictures/"
    # �ļ���ȡ
    f = open("../input.txt")
    imgBase64 = f.readline()
    img_base64.base64_to_img(img_name=img_name, img_save_path=img_save_path, img_base64=imgBase64)
    print("���н�����")
