# coding=gbk
import cv2 as cv

'''拍照功能的实现'''
def make_photo():
    # 使用电脑默认的摄像头
    cap = cv.VideoCapture(0)
    i = 1
    while True:
        ret, frame = cap.read()
        if i != 0:
            print("frame的值为：", frame)
            i -= 1
        if ret:
            # 弹出窗口
            cv.imshow("capture", frame)
            # 等待按q键操作关闭摄像头
            if cv.waitKey(1) & 0xFF == ord('q'):
                file_name = "temp.jpeg"
                file_save_path = "./img_save/"
                cv.imwrite(file_save_path + file_name, frame)
                break
        else:
            break
    cap.release()
    cv.destroyAllWindows()


'''录像功能的实现'''
def make_video():
    # 调用默认的摄像头
    cap = cv.VideoCapture(0)
    # 指定视频代码
    fourcc = cv.VideoWriter_fourcc(*"DIVX")
    video_save_path = "./video_save/"
    out = cv.VideoWriter(video_save_path + 'temp.avi', fourcc, 20.0, (640, 480))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            # 弹出窗口
            cv.imshow("capture", frame)
            # 等待按q键操作关闭摄像头
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()



if __name__ == "__main__":
    # 拍照
    make_photo()

    # 录像
    # make_video()













