from tkinter import *
def open():
    print("file has been opened")
def save():
    print("file has been save")


window =Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu= Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="open",command=open)
fileMenu.add_command(label="save",command=save)
fileMenu.add_separator()
fileMenu.add_command(label="exit",command= quit)

editmenu= Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="edit",menu=editmenu)
editmenu.add_command(label="cut")
editmenu.add_command(label="copy")
editmenu.add_command(label="paste")

window.mainloop()
