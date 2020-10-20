# welcome to my face_recognition project
THis project has 4 file each file does specfic task lets start by fuction that each file contibute and together they identify and recognize faces.
In this projects we have used inbuild python libaray function like numpy,tk-inter,opencv2.
this project uses opencv and haarcascade to detect the faces.

There are many haarcascade xml files which can be used to detect various features and emotion of a face like detecting a smile,lips,nose ets. 
In this project we are frontal face haarcascade file to detect the face.You can download it from above repository named in haarcascade_frontalface.
This file is used to detect the face in live images and we can crop out the face using Fishers algorithm or LBPH face-recognizer to train the face detected by the cascade and dump into a yml format which is later used for detecting the faces.

face:
This page runs to capture a video which then converted into images( as flow of images know as video) which is stored in a file under the name of the person's face.
The images are converted from rgb to gray scale for reducing contrast,bright light or anything which may create to detect or train the face,this gray_scaled images are stored in the person_name.png files.
face_train: 
this page deals with algorithm like fisherface,LBPH or eigenface etc. The stored images are croped by face and then converted into a numpy array if array contains 3-d the its is bascially RGB ratio of every part of window images with the help algorithms which is used for dump the tained file numpy array and stored in yml format file which is later used to recognize faces.
kkk.py:
This page is used to detect the faces if the founded face is not in the date-base ( yml file ) it will show unknown, during recognition the detected face undergoes into confidence matrix,if the confidence is more than 80% the recoginzed faced is in date-base with identified named.
If he matrix is less than 80% then show it as unknown, this message can displayed on love image with the help of a label function
front.py :
Tis files uses TK-inter, to create a gui interface for python each function of button are construced based on the files, there a is empty label element which used to identify the name of the person whose face,is going to be trained

(inshort) the front gui interface contains four buttons:
1. detect - which calls the first file face.py to identify faces and stored in a file
2. train - which calls the second file face_train.py which uses algorithm like fisherface,eigenface is converted into numpy array and stored in a yml file.
3. identify - which calls the third file kkk.py which uses the yml file created during the training, with the confidence matrix it helps identify the person 
              if its in the yml file else it shows unkown label to that face.
 4. quit- this fuction is used to get out of the running gui interace.
