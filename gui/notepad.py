import sys
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

import os




def gg():
    showinfo("about this program","this program was made to implement python gui skills with various utility options added to make it actually useful to the people using it")
def change_color():
    color=colorchooser.askcolor(title="pick n choose")
    text.config(fg=color[1])
def new_file():
    window.title("Untitled")
    text.delete(1.0,END)
def change_font(*args):
    text.config(font=(font_name.get(), sizebox.get()))

def open_file():
    file= askopenfilename(defaultextension=".txt",file=[("All Files","*.*"),
                                                        ("Text Documents","*.txt")])

    try:
        window.title(os.path.basename(file))
        text.delete(1.0,END)

        file= open(file,"r")
        text.insert(1.0,file.read())

    except Exception:
        print("could read your chosen file")

    finally:
        file.close()
def copy(*args):
    text.event_generate("<<Copy>>")
def cut(*args):
    text.event_generate("<<Cut>>")
def paste():
    text.event_generate("<<Paste>>")



def savefile(*args):
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text file",".txt"),
                                               ("html file",".html")])
    if file is None:
        return
    input = str(text.get("1.0", END))
    file.write(input)
    file.close()

window= Tk()
window.title("notes")

icon = PhotoImage(file="C:\\Users\\ROHAN\\OneDrive\\Desktop\\dev\\icon2.png")
window.iconphoto(True, icon)


window.geometry("600x500")
window.bind("<Control-s>",savefile)
window.bind("<Control-c>",copy)
window.bind("<Control-x>",cut)
window.bind("<Control-v>",paste)



font_name=StringVar(window)
font_name.set("Arial")
font_size=StringVar(window)

text=Text(window,
          bg="#f5ecd6",
          font=(font_name,16),
          height=8,
          width=25,padx=10,
          fg='purple')
text.pack()
scroll= Scrollbar(text)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text.grid(sticky=N+E+S+W)

scroll.pack(side=RIGHT,fill=Y)
text.config(yscrollcommand=scroll.set)

frame=Frame(window)
frame.grid()

colorbutt=Button(frame,text='color',command=change_color)
colorbutt.grid(row=0,column=0)
fontbox=OptionMenu(frame,font_name,*font.families(),command=change_font)
fontbox.grid(row=0,column=1)

sizebox=Spinbox(frame,from_=16,to=100,textvariable=font_size,command=change_font)
sizebox.grid(row=0,column=2)

menubar= Menu(window)
window.config(menu=menubar,bg="#e8f4ff")

file_menu=Menu(menubar,tearoff=0,bg="#e8f4ff")
menubar.add_cascade(label="FILE",menu=file_menu)
file_menu.add_command(label="new file",command=new_file)
file_menu.add_command(label="open_file",command=open_file)

file_menu.add_command(label="save file",command=savefile)
file_menu.add_separator()
file_menu.add_command(label="exit",command=sys.exit)

edit_menu=Menu(menubar,tearoff=0,bg="#e8f4ff")
menubar.add_cascade(label="EDIT",menu=edit_menu)
edit_menu.add_command(label="copy file",command=copy)
edit_menu.add_command(label="cut file",command=cut)
edit_menu.add_command(label="paste file",command=paste)

help_menu=Menu(menubar,tearoff=0,bg="#e8f4ff")
menubar.add_cascade(label="HELP",menu=help_menu)
help_menu.add_command(label="About",command=gg)



window.mainloop()