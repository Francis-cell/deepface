import base64

'''将图片转换成我们需要的base64编码格式'''
def img_base64(img_path):
    # 通过二进制方式打开图文件
    pic = open(img_path, "rb")
    # 使用b64encode转换为base64方式
    pic_base64 = base64.b64encode(pic.read())
    pic.close()
    # 我们需要的字符串的开头是这样的
    first_value = "data:image/jpeg;base64,"
    # base64默认返回的是byte格式的数据，此处需要强转str格式的才能使用
    last_value = str(pic_base64)
    # 截取需要的部分的数据
    last_value = last_value[2: -1]

    # 此处返回的final_value就是我们最终将要传入的图片的数据
    final_value = first_value + last_value
    return final_value

'''将图片的base64编码转换成图片格式'''
def base64_to_img(img_name, img_save_path, img_base64):
    img_base64 = str(img_base64)
    img_decode = base64.b64decode(img_base64)
    # img_save_path = "../savePictures/"

    with open(img_save_path + img_name, "wb") as f:
        f.write(img_decode)
