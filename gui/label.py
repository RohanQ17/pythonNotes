from tkinter import *
# label = area widget that holds another text or picture

window = Tk()
window.geometry("400x400")
window.config(background="#5cfcff")
pic = PhotoImage(file='labelicon.png')  #choose a smaller picture
label = Label(window,
              text="YO",
              font=('Arial',20,'bold'),
              fg='black',
              bg='white',
              relief =RAISED,
              bd=10,
              padx=10,
              pady=10,
              image=pic,
              compound='center'
              )
label.place(x=180,y=180)

window.mainloop()

