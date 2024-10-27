from tkinter import *
def something(event):
    #print("you pressed"+ event.keysym)
    label.config(text= event.keysym)

window = Tk()
window.bind("<Key>",something)
label= Label(window,font=("Halvetica",100))
label.pack()
window.mainloop()

#mouse events
# window.bind("<button-1>",fnc)  button 1 is left click , 2 is wheel and 3 is right
#print("mouse coordinates" + string(event.x) + string(event.y) ) will give you the coordinated where you clicked
# <Motion> will give you the continous coordinates of a mouse