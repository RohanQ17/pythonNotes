from tkinter import *
window = Tk()
window.geometry("400x400")
window.config(background="#5cfcff")
pic = PhotoImage(file='labelicon.png')
count=0
def click():
    global count
    count += 1
    print("you clicked the button!",count,"times")

button = Button(window,
                text= "click me",
                command=click,
                font=("Comin Sans",30),
                fg="#00FF00",
                image=pic,
                compound='top'
                )
button.pack()
window.mainloop()