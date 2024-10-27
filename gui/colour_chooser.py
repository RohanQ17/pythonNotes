from tkinter import *
from tkinter import colorchooser
def click():
    color = colorchooser.askcolor()
    print(color)
    colorhex= color[1]
    win.config(bg=colorhex)
win = Tk()
win.geometry("400x400")
button=Button(win,text= 'clickme',font=('Arial',25) ,command= click,)
button.place(x=140,y=140)

win.mainloop()