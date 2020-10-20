import cv2
import os

path = r'C:\Users\akhil\PycharmProjects\myfirst'
os.chdir(path)
path2 = r'C:\Users\akhil\PycharmProjects\images'


def take_pic(name1='DEFAULT'):
    entry = []
    a = 0
    face_cas = cv2.CascadeClassifier(r'C:\Users\akhil\Desktop\haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    # if front.name1.index() == 0:
    #     if not front.name.get in entry:
    #         entry.append(front.name1.get())
    #     id_ = front.name1.get()+'.txt'
    #     print(id_)
    # else:
    #     exit()

    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('img', img)
        # f = open(name1,'w')
        os.chdir(path2)
        if not os.path.exists(name1):
            os.makedirs(name1)
        os.chdir(name1)
        cv2.imwrite(name1 + str(a) + '.png',gray)
        a += 1
        os.chdir(path)
        # f.close()
        cv2.imshow('gray', img)
        k = cv2.waitKey(30)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
