#from turtle import *

#Pen()
#forward(90)
#left(120)

from tkinter import *
from tkinter import messagebox

def hello():
    messagebox.showinfo('Xin chao cac ban', 'cac ban khoe ko')

tk = Tk();
#btn = Button(tk, text = 'click me', command = hello);
#btn.pack()

cas = Canvas(tk, width = 1000, height= 1000);
cas.create_line(100, 1000,500, 200)
cas.create_polygon(400,300,100,100,200,200)
cas.create_text(100,300, text = 'Vu Van Quyet', font=('Times', 20))
cas.pack()
