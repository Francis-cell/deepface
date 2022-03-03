# coding=gbk
import img_base64
import json_format
import deal_with_picture

'''传入模型的选择(默认给予VGG-Face的值); img1的路径; img2的路径'''


def build_json_data(img1_path, img2_path, model_change="VGG-Face"):
    # 将图片1转换成base64的编码格式并输出
    img1_base64 = img_base64.img_base64(img1_path)
    # 将图片2转换成base64的编码格式并输出
    img2_base64 = img_base64.img_base64(img2_path)
    # 返回Postman中可以使用的json格式的内容
    last_json = json_format.json_format(model_change, img1_base64, img2_base64)
    return last_json


'''比对 一对图片的相似度'''


# 参数输入说明：
# 1、img1_path, img2_path【图片路径】
# 2、models：最终生成的json数据时选择的模型
def context_pair_pictures(img1_path, img2_path, models="VGG-Face"):
    # 1、处理图片
    deal_with_picture.deal_with_picture(img1_path)
    deal_with_picture.deal_with_picture(img2_path)
    # 四、使用处理之后的图片路径
    img_save_path = "../savePictures/"
    img1_real_name = img1_path.split("/")[-1]
    img1_path = img_save_path + img1_real_name
    # print("img1_path的值为：", img1_path)
    img2_real_name = img2_path.split("/")[-1]
    img2_path = img_save_path + img2_real_name
    # print("img2_path的值为：", img2_path)
    # 五、生成最终的json结果数据
    last_value = build_json_data(img1_path=img1_path, img2_path=img2_path, model_change=models)
    # 六、将输出保存到一个文件中，方便复制获取
    file = open("../output.txt", "w")
    file.write(last_value)
    file.close()
    print("运行结束")


'''在一组图片中查找当前传入的图片的人，是否在这一群人中存在'''


# 参数输入说明：
# 1、models：最终生成的json数据时选择的模型
# 2、img_path：要比对的图片的路径
def context_one_many(models, img_path):
    # 1、将传入的图片处理成base64编码的形式
    img_with_base64 = img_base64.img_base64(img_path=img_path)
    # 2、生成需要的json形式的数据
    img_json = json_format.json_format_find(model=models, img_base64=img_with_base64)
    # print(img_json)
    # 3、将输出的json数据保存到一个txt文件里面去
    file = open("../output.txt", "w")
    file.write(img_json)
    file.close()
    print("运行结束！！！")


'''生成一张图片的base64的编码'''


# 参数输入说明：
# img_path：要生成json数据的图片的路径
def context_one_base64(img_path):
    # 将这张图片转换成base64编码格式
    imgBase64 = img_base64.img_base64(img_path=img_path)
    # 处理一下数据
    imgBase64 = imgBase64.split(",")[1]
    # 获取此处的图片的名字
    imgName = img_path.split("/")[-1].split(".")[0]
    # print("imgName的值为：", imgName)
    # 将图片的base64的编码转换成需要的json格式
    last_value = json_format.json_format_getBase64Code(imgName, imgBase64)
    # 将这个需要的json格式的图片的编码保存到指定的文件内，方便复制使用
    file = open("../output.txt", "w")
    file.write(last_value)
    file.close()
    print("运行结束!")


if __name__ == "__main__":
    # # 一、一对图片的比对测试
    # models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace"]
    # img1_path = "../database/ZhangHanyun/3.jpg"
    # img2_path = "../database/ZhangHanyun/2.jpg"
    # context_pair_pictures(img1_path=img1_path, img2_path=img2_path, models=models[0])

    # # 二、将一张图片在一组图片中寻找最相似的结果
    # # models = ["VGG-Face", "Facenet"]
    # models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace"]
    # # 要比对的图片的路径
    # img_path = "../database/ZhangHanyun/3.jpg"
    # # 要被比对的大量的图片的存储路径
    # # imgs_path = "../database/ZhangHanyun/"
    # context_one_many(models=models, img_path=img_path)

    # 三、生成一张图片的base64的编码
    # # 要生成json数据的图片的路径
    # img_path = "../database/ZhangHanyun/3.jpg"
    # # 生成需要的json数据
    # context_one_base64(img_path=img_path)


    # 临时测试（测完删掉）
    img_name = "test.jpg"
    img_save_path = "../savePictures/"
    # 文件读取
    f = open("../input.txt")
    imgBase64 = f.readline()
    img_base64.base64_to_img(img_name=img_name, img_save_path=img_save_path, img_base64=imgBase64)
    print("运行结束！")
