from tkinter import *
import face
import kkk
import face_train
import cv2
import pickle
import tkinter.messagebox


def take_image():
    status1 = Label(k, text='preparing....', relief=SUNKEN, anchor=W)
    status1.grid(row=10, sticky='se')
    face.take_pic(name1.get())


def check_photo():
    status2 = Label(k, text='checking     ', relief=SUNKEN, anchor=W)
    status2.grid(row=10, sticky='se')
    kkk.check_again()


def train_photo():
    face_train.face_training()
    status3 = Label(k, text='prepared     ', relief=SUNKEN, anchor=W)
    status3.grid(row=10, sticky='se')


k = Tk()
k.title('front')
k.geometry('600x600')
k.grid_rowconfigure(0, weight=1)
k.grid_columnconfigure(0, weight=1)
label1 = Label(k,text='name')
label1.place(x=30,y=60)
name1 = Entry(k)
name1.place(x=100,y=60)
button_check = Button(k,text='Take Image',width=15,height=3,command=take_image)
button_check.place(x=30,y=120)
button_train = Button(k,text='Train',width=15,height=3,command=train_photo)
button_train.place(x=180,y=120)
button_detect = Button(k,text='Detect',width=15,height=3,command=check_photo)
button_detect.place(x=330,y=120)
button_quit = Button(k,text='QUIT',width=15,height=3,command=k.destroy)
button_quit.place(x=480,y=120)
status = Label(k, text='loaded.', relief=SUNKEN, anchor=W)
status.grid(row=10,sticky='se')


# ------function ------
k.mainloop()


