from tkinter import *
win = Tk()

firstnamelabel = Label(win,text="first name").grid(row=0,column=0)
entry1= Entry(win).grid(row=0,column=1)
lastnamelabel = Label(win,text="last name").grid(row=1,column=0)
entry2= Entry(win).grid(row=1,column=1)
email = Label(win,text="email").grid(row=2,column=0)
entry3= Entry(win).grid(row=2,column=1)

butt= Button(win,text="submit",).grid(row=3,column=0,columnspan=2)

win.mainloop()


