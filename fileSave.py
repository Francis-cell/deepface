# coding=gbk
# 1����ͨ���ļ�д��
file = open("./fileSave.txt", "w")
file.write("hello")
file.close()


# 2�����ֵ�д�뵽�ļ���
d = {'a': 'aaa', 'b': 'bbb'}
s = str(d)
f = open("./fileSave.txt", "w")
f.writelines(s)
f.close()