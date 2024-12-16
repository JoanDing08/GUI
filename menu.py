from tkinter import *

w=Tk()
w.title("Menu")
w.config(bg="purple")

menuBar=Menu(w)

f=Menu(menuBar,tearoff=0)
e=Menu(menuBar,tearoff=0)

menuBar.add_cascade(label="File",menu=f)
f.add_command(label="New Text File",command=None)
f.add_command(label="New File",command=None)
f.add_command(label="New Window",command=None)
f.add_command(label="New Window With Profile",command=None)
f.add_separator()
f.add_command(label="Exit",command=w.destroy)

menuBar.add_cascade(label="Edit",menu=e)
e.add_command(label="Undo",command=None)
e.add_command(label="Redo",command=None)
e.add_separator()
e.add_command(label="Cut",command=None)
e.add_command(label="Copy",command=None)
e.add_command(label="Paste",command=None)


w.config(menu=menuBar)


mainloop()