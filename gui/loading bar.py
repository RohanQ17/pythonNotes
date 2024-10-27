from tkinter import *
from tkinter.ttk import *
import time


def start():
    tasks= 100
    x=0
    while(x<tasks):
        time.sleep(0.05)
        bar['value']+=1

        x+=1
        percent.set(str(int((x/tasks)*100))+"%")
        win.update_idletasks()

win=Tk()
percent= StringVar()
bar=Progressbar(win,orient=HORIZONTAL,length=400)
bar.pack(pady=30,padx=40)

percentlabel= Label(win,textvariable=percent).pack()

button = Button(win,text="download",command=start).pack()

win.mainloop()