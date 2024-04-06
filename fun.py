from cProfile import label
from logging import root
from tkinter import *
from tkinter import messagebox
import random
from types import BuiltinFunctionType

def no():
    messagebox.showinfo(' ','Thanks bro')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0,500), y= random.randint(0,500))

root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)

label = Label(root, text='are you Gay', font='Arial 20 bold' , bg='white').pack()
btnYes = Button(root, text='No', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNO = Button(root, text='yes ', font='Arial 20 bold', command=no).place(x=350, y=100)

root.mainloop()