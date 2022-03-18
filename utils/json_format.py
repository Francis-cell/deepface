# coding=gbk
import json

'''将传入的图片的数据作为数据生成需要的json格式的数据'''


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
    # 将last_values的值格式化成为json标准格式，并返回
    final_values = json.dumps(last_values)

    return final_values


'''为find api提供的方法（用于生成postman使用的body体中的数据）'''


def json_format_find(model, img_base64):
    last_values = {
        "modelName": model,
        "img": img_base64
    }

    # 将last_values的值格式化为json标准形式，并返回
    final_values = json.dumps(last_values)

    return final_values


'''将一个数组中的元素转换成需要的json格式作为结果'''


def json_format_find_out(arr):
    # identity 图片的路径
    name1 = arr[0]
    # VGG-Face_cosine 模型以及采用的计算方式
    name2 = arr[1]

    final_value = {}

    for i in range(len(arr)):
        # 处理除了第0位的偶数位的数据（图片的路径）
        if i != 0 and i % 2 == 0:
            insert_value = {
                arr[0]: arr[i],
                arr[1]: arr[i + 1]
            }

            final_value.update({str(int(i / 2)): insert_value})

    return final_value


'''为getBase64Code api提供的方法（用于生成postman使用的body体中的数据）'''


def json_format_getBase64Code(img_name, img_base64):
    last_values = {
        "photoName" : img_name,
        "base64Code" : img_base64
    }

    # 将last_values的值格式化为json标准形式，并返回
    final_values = json.dumps(last_values)

    return final_values