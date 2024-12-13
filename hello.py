from tkinter import *
from PIL import ImageTk,Image

import numpy as np

import pygame


#Assets https:techwithtim.net
msg = "Roll a dice!"
print(msg)

print(np.random.randint(1,99999))

root = Tk()


# e = Entry(root, width=100, borderwidth=10)
# e.pack()
# e.insert(0, "Enter your name: ")

# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="bye!")

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)

# my_img =  ImageTk.PhotoImage(Image.open("Screenshot_20180609-201153.png"))
# my_label = Label(image=my_img)
#my_label.pack()


class Position:
    def _init_ (self, x, y):
        self.x = x
        self.y = y

class Piece:
    def __init__(self, num, position, color):
        self.num = num
        self.position = position
        self.color = color


p1 = Piece(1, 1, "red")

print(p1.color)

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

# myButton = Button(root, text="Click me!", command=myClick, fg="red", bg="black")
# myButton.pack()

h = 1
w = 2

#Build our buttons
b01 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")
b03 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")
b05 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")
b07 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")
b10 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")
b12 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")
b14 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")
b16 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")
b21 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")
b23 = Button(root, text="O", font=("Helvetica", 20), height=h, width=w, bg = "black", fg="red")



#Place our buttons
b01.grid(row=0, column=1)
b03.grid(row=0, column=3)
b05.grid(row=0, column=5)
b07.grid(row=0, column=7)
b10.grid(row=1, column=0)
b12.grid(row=1, column=2)
b14.grid(row=1, column=4)
b16.grid(row=1, column=6)
b21.grid(row=2, column=1)

root.mainloop()