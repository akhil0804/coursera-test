import os
import numpy as np
import cv2
from PIL import Image
import pickle
path = r'C:\Users\akhil\PycharmProjects\myfirst'
os.chdir(path)
path2 = r'C:\Users\akhil\PycharmProjects\images'

def face_training():

    BASE_DIR = os.path.dirname(path2)
    print(BASE_DIR)
    face_cascade = cv2.CascadeClassifier(r'C:\Users\akhil\Desktop\haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    current_id = 0
    label_ids = {}
    x_train = []
    y_label = []

    for root,dirs,files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root,file)
                label = os.path.basename(root).replace(" ","-").lower()
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]

                pil_image = Image.open(path).convert("L") #grayscale
                size = (550,550)
                final_image = pil_image.resize(size,Image.ANTIALIAS)
                image_array = np.array(final_image,np.uint8)

                faces = face_cascade.detectMultiScale(image_array,1.5,5)

                for (x,y,w,h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_label.append(id_)

    print(label_ids)

    with open("label.pickle",'wb')as f:
        pickle.dump(label_ids,f)
    recognizer.train(x_train,np.array(y_label))
    recognizer.save("trainner.yml")





