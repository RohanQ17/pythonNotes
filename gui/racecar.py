from tkinter import *
def move(event):
    label.place(x=label.winfo_x()+20,y=label.winfo_y())

def move_back(event):
    label.place(x=label.winfo_x() -20, y=label.winfo_y())
window = Tk()
window.geometry("2000x400")

window.bind("<Right>",move)
window.bind("<Left>",move_back)

myimage=PhotoImage(file='car.png')
label= Label(window,image=myimage)
label.place(x=0,y=100)
window.mainloop()


