# coding=gbk
from retinaface import RetinaFace
import matplotlib.pyplot as plt
import json

img_path = "./images/many2.jpg"
# ==detect_faces==
# resp = RetinaFace.detect_faces(img_path)
# print(resp)
#
# print(json.dumps(resp, sort_keys=True, indent=2))

# ==extract_faces==
faces = RetinaFace.extract_faces(img_path, align=True)
# print(face)
file_save_path = "C:/Users/86185/Desktop/save/"
i = 0
for face in faces:
    # plt.imshow(face)
    # plt.show()
    plt.imsave(file_save_path + str(i) + ".jpg", face)
    i += 1