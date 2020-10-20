import numpy as np
import cv2
import pickle

l = []


def check_again():
    face_cascade = cv2.CascadeClassifier(r'C:\Users\akhil\Desktop\haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")

    with open("label.pickle",'rb')as f:
        og_label = pickle.load(f)

        labels = {v:k for k,v in og_label.items()}

    cap = cv2.VideoCapture(0)

    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            # roi_color = img[y:y + h, x:x + w]   #region of interest  = roi
            id_,conf = recognizer.predict(roi_gray)
            if conf >= 70 and conf <=80:
                l.append(labels[id_])
                cv2.putText(img,labels[id_],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            elif conf < 70:
                cv2.putText(img,'unknown',(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)

            cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()