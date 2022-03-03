# coding=gbk
import cv2 as cv

'''���չ��ܵ�ʵ��'''
def make_photo():
    # ʹ�õ���Ĭ�ϵ�����ͷ
    cap = cv.VideoCapture(0)
    i = 1
    while True:
        ret, frame = cap.read()
        if i != 0:
            print("frame��ֵΪ��", frame)
            i -= 1
        if ret:
            # ��������
            cv.imshow("capture", frame)
            # �ȴ���q�������ر�����ͷ
            if cv.waitKey(1) & 0xFF == ord('q'):
                file_name = "temp.jpeg"
                file_save_path = "./img_save/"
                cv.imwrite(file_save_path + file_name, frame)
                break
        else:
            break
    cap.release()
    cv.destroyAllWindows()


'''¼���ܵ�ʵ��'''
def make_video():
    # ����Ĭ�ϵ�����ͷ
    cap = cv.VideoCapture(0)
    # ָ����Ƶ����
    fourcc = cv.VideoWriter_fourcc(*"DIVX")
    video_save_path = "./video_save/"
    out = cv.VideoWriter(video_save_path + 'temp.avi', fourcc, 20.0, (640, 480))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            # ��������
            cv.imshow("capture", frame)
            # �ȴ���q�������ر�����ͷ
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()



if __name__ == "__main__":
    # ����
    make_photo()

    # ¼��
    # make_video()













