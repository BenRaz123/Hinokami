#!/usr/bin/env python3


# Hinokami Ver 2.0
# (c) 2022 by OuterSpiral Studios. All Rights Reserved
# Written using python 3.9.13
# Special Thanks to everyone supporting me along the way :)


# Main Developer: lLukii (Lucas Yichen Jiao) (He/Him/His)


from tkinter import *
import os
from tkinter import messagebox


# GUI basic setup
root = Tk()
root.geometry("720x720")
root.wm_title("Hinokami V2.0")
title1 = Label(root,text="Hinokami Ver 2.0",font=('Cabrili', '30'))
title1.pack()
title2 = Label(root,text="A new and innovative way to organize files!",font=('Cabrili', '15'))
title2.pack()
title3 = Label(root, text="\n")
title3.pack()

items = []
add_file = Entry(root,text="Enter a file name: ", font="cabrili")
add_file.pack()
title4 = Label(root, text="Select a file", font=('cabrili', 15, 'bold'))
title4.pack()

def check_file():
    if os.path.isfile(add_file.get()):
        title5 = Label(root, text=add_file.get())
        title5.pack()
        items.append(add_file.get())
    
    elif os.path.isdir(add_file.get()):
        messagebox.showerror("Error", "The selected path is a directory")
    
    else:
        messagebox.showerror("Error", "The selected path does not exist")

button1 = Button(root, text="Add file", command=check_file)
button1.pack()

title8 = Label(root, text="\n")

op_file = Entry(root,text="Open a file name: ", font="cabrili")
op_file.pack()
title6 = Label(root, text="Open a File", font=('cabrili', 15, 'bold'))
title6.pack()
title7 = Label(root, text="To open a file, type in the file number in the list from up to down.", font=('cabrili', 10))
title7.pack()


def open_file():
    try:
        os.system(f"open {items[int(op_file.get())-1]}")
    
    except:
        messagebox.showerror("Error", "This is not a valid position!")

        
button2 = Button(root, text="Open File", command=open_file)
button2.pack()

title8 = Label(root, text='\nListed Files: ', font=('cabrili', 15, 'bold'))


root.mainloop()



