from tkinter import *
def drag(event):
    label.startx = event.x
    label.starty = event.y
def dragmotion(event):
    x= label.winfo_x() - label.startx + event.x
    y = label.winfo_y() - label.starty + event.y
    label.place(x=x,y=y)



window = Tk()

label= Label(window,bg="blue",height=10,width=12)
label.place(x=0,y=0)

label.bind("<Button-1>",drag)
label.bind("<B1-Motion>",dragmotion)
window.mainloop()

