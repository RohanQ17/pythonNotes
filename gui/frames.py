# frame = a rectangular container that groups and holds widgets
from tkinter import *

window = Tk()
frame= Frame(window,bg="pink",bd=5,relief=RAISED)
frame.pack()
button = Button(frame, text="W",font=("consolas",25),width=3)
button1 = Button(frame, text="A",font=("consolas",25),width=3)
button2 = Button(frame, text="S",font=("consolas",25),width=3)
button3 = Button(frame, text="D",font=("consolas",25),width=3)
button.pack(side=TOP)
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=BOTTOM)
window.mainloop()