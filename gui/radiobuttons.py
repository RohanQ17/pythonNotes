from tkinter import *

food=["gtr","courvette","mazda"]

window = Tk()
def order():
    if x.get()==0:
        print("you will get a gtr")
    if x.get() == 1:
        print("you will get a courvette")
    if x.get() == 2:
        print("you will get a mazda")

x = IntVar()
# pic = Photoimage krke bna skte
#foodimages = [pic1,pic2,pic3]
for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value= index,
                               font=("Impact",40),
                               padx=40,
                               pady=10,
                               indicatoron=0,
                               #eliminate circle indicators,
                               command=order)
                               

                                #image= foodimages[index]
    radio_button.pack(anchor=W)



window.mainloop()