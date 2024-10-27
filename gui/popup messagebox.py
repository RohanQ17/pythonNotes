

from tkinter import *
from tkinter import messagebox
def click():

    messagebox.showwarning(title='virus alert',message='your computer has a virus')
    if messagebox.askokcancel(title='choose',message='do you want to install antivirus'):
        print("are you sure")
    else:
        messagebox.showwarning(title='virus alert', message='your computer has a virus')
window = Tk()
window.geometry("400x400")
butt = Button(window,text="click me please",font=("Arial",20),padx=20,command=click)
butt.place(x=110,y=140)
window.mainloop()
