from tkinter import *
import time
xvelocity=1
yvelocity=1
WIDTH= 700
HEIGHT = 300
window = Tk()



canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
back= PhotoImage(file='distopia.png')
back_image=canvas.create_image(0,0,image=back)
pic= PhotoImage(file='monster.png')

my_image=canvas.create_image(0,0,image=pic,anchor=NW)

while True:
    coordinates= canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=WIDTH-pic.width() or coordinates[0]<0 ):
        xvelocity=-xvelocity
    if (coordinates[1] >= HEIGHT - pic.height() or coordinates[1] < 0):
        yvelocity = -yvelocity

    canvas.move(my_image,xvelocity,yvelocity)
    window.update()
    time.sleep(0.01)



window.mainloop()






