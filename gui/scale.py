from tkinter import *
def submit():
    print("the temperature is ",scale.get(),"deg celsius")
window = Tk()
hot_image =PhotoImage(file='fire-emoji-402x512-8ma95d17.png')
hotlabel=Label(image=hot_image)
hotlabel.pack()


scale =Scale(window,
             from_=100,
             to=0,
             length=600,
             orient=VERTICAL,
             font=('Consolas',20),
             tickinterval=10,
             showvalue=0,
             resolution=5,
             troughcolor='#69EAFF',
             fg = '#FF1C00')
scale.pack()

button = Button(window,text="submit",command=submit)
button.pack()
cold_image = PhotoImage(file='cold-face-emoji-emoji-506x512-h79cno34.png')
coldlabel=Label(image=cold_image)
coldlabel.pack()
window.mainloop()