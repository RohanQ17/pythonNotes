from tkinter import *
from tkinter import ttk


#Toplevel() = a new window on the top of initial window , linked to it as well
# so closing the initial window will close any top levels too.
#anyways here are tabs
win=Tk()

notebook =ttk.Notebook(win)
tab1=Frame(notebook)
tab2=Frame(notebook)
notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both") # expand stays in centr and fill helps in actual exoansion

Label(tab1,text="welcome to first tab",width=20,height=30).pack()
Label(tab2,text="welcome to second tab",width=20,height=30).pack()


win.mainloop()
