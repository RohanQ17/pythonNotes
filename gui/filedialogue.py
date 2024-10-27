from tkinter import *
from tkinter import filedialog
def open():
    filepath= filedialog.askopenfilename(filetypes=(("textfiles","*.text"),("allfiles","*.*")))
    file=open(filepath,'r')
    print(file.read())
    file.close()

window =Tk()
button= Button(window,text="open file",command= open,font=('Arial',20))
button.place(x=50,y=50)
window.mainloop()