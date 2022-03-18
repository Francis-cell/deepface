# coding=gbk
import json

'''�������ͼƬ��������Ϊ����������Ҫ��json��ʽ������'''


def json_format(model, img1_base64, img2_base64):
    insert_value = {
        "img1": img1_base64,
        "img2": img2_base64
    }

    last_values = {
        "model_name": model,
        "img": [
            insert_value
        ]
    }
    # ��last_values��ֵ��ʽ����Ϊjson��׼��ʽ��������
    final_values = json.dumps(last_values)

    return final_values


'''Ϊfind api�ṩ�ķ�������������postmanʹ�õ�body���е����ݣ�'''


def json_format_find(model, img_base64):
    last_values = {
        "modelName": model,
        "img": img_base64
    }

    # ��last_values��ֵ��ʽ��Ϊjson��׼��ʽ��������
    final_values = json.dumps(last_values)

    return final_values


'''��һ�������е�Ԫ��ת������Ҫ��json��ʽ��Ϊ���'''


def json_format_find_out(arr):
    # identity ͼƬ��·��
    name1 = arr[0]
    # VGG-Face_cosine ģ���Լ����õļ��㷽ʽ
    name2 = arr[1]

    final_value = {}

    for i in range(len(arr)):
        # ������˵�0λ��ż��λ�����ݣ�ͼƬ��·����
        if i != 0 and i % 2 == 0:
            insert_value = {
                arr[0]: arr[i],
                arr[1]: arr[i + 1]
            }

            final_value.update({str(int(i / 2)): insert_value})

    return final_value


'''ΪgetBase64Code api�ṩ�ķ�������������postmanʹ�õ�body���е����ݣ�'''


def json_format_getBase64Code(img_name, img_base64):
    last_values = {
        "photoName" : img_name,
        "base64Code" : img_base64
    }

    # ��last_values��ֵ��ʽ��Ϊjson��׼��ʽ��������
    final_values = json.dumps(last_values)

    return final_values