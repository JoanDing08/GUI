from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

w=Tk()

def save():
  files=asksaveasfile(defaultextension=".txt")
  if files is not None:
    for i in lb.get(0,END):
      print(i,file=files)
    lb.delete(0,END)

def open():
  files=askopenfile()
  if files is not None:
    lb.delete(0,END)
    item=files.readlines()
    for i in item:
      lb.insert(END,i)

b1=Button(w,text="Save",command=save)
b2=Button(w,text="Add")
b3=Button(w,text="Open",command=open)
b4=Button(w,text="Delete")

e=Entry(w,width=16)

lb=Listbox(w)
sb=Scrollbar(w)

b1.grid(row=0,column=0,pady=10,padx=10)
b2.grid(row=1,column=0,pady=5,padx=10)
b3.grid(row=0,column=1,pady=5,padx=10)
b4.grid(row=1,column=1,pady=5,padx=10)

e.grid(row=3,column=0,pady=10,padx=10)
lb.grid(row=4,column=0,pady=10,padx=5)
sb.grid(row=4,column=1)

for i in range(10):
  lb.insert(END,i)

mainloop()
