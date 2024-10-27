from tkinter import *

def display():
    if(x.get()==1):
        print("you agree :D")
    else: print("you dont :(")
window = Tk()
x = IntVar()
pic=PhotoImage(file='labelicon.png')
check_box = Checkbutton(window,
                        text="i agree",
                        variable = x,
                        onvalue= 1,
                        offvalue=0,
                        command= display,
                        font=('Arial',25),
                        foreground='#00FF00',
                        bg='black',
                        activeforeground='#00FF00',
                        activebackground='black',
                        image= pic,
                        compound= 'left',
                        padx=35,
                        pady=20)



check_box.pack()
window.mainloop()


