#listbox = a list of selectable items within its own container
from tkinter import *
def submit():
    print("you picked :",listbox.get(listbox.curselection()))
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())
window =Tk()

listbox = Listbox(window,
                  bg="white",
                  font=("Arial",35),
                  width=10,
                  selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,"gtr")
listbox.insert(2,"mazda")
listbox.insert(3,"mclaren")
listbox.insert(4,"courvette")
listbox.config(height=listbox.size())
entrybox= Entry(window)
entrybox.pack()
addbutton = Button(window,text="add",command=add)
addbutton.pack()
deletebutton = Button(window,text="delete",command=delete)
deletebutton.pack()
submit_button = Button(window,text="submit",command=submit)
submit_button.pack()
window.mainloop()


