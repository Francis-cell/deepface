# coding=gbk
# 1、普通的文件写入
file = open("./fileSave.txt", "w")
file.write("hello")
file.close()


# 2、将字典写入到文件中
d = {'a': 'aaa', 'b': 'bbb'}
s = str(d)
f = open("./fileSave.txt", "w")
f.writelines(s)
f.close()