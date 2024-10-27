from tkinter import *
#widgets = gui objects as buttons , textboxetc
#windows is a container used to hold these gui objects

wind = Tk() # instantiates a window for us
wind.title("riri")

icon = PhotoImage(file='icon.png')
wind.iconphoto(True,icon)
wind.config(background="#5cfcff")


wind.geometry("420x420")
wind.mainloop()


