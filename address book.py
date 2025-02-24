from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

w=Tk()

info={}

def open():
  files=askopenfile()
  if files is not None:
    lb.delete(0,END)
    info=eval(files.read())
    for i in info:
      lb.insert(END,i)
  else:
    messagebox.showinfo(message="You have not selected a file.\n Please select a file to continue.")

def save():
  files=asksaveasfile(defaultextension=".txt")
  if files is not None:
    print(info,file=files)
  else:
    messagebox.showinfo(message="You have not selected a file.\n Please select a file to continue.")

def add():
  key=e1.get()
  if key=="":
    messagebox.showinfo(message="Please enter a name.")
  else:
    if key not in info:
      lb.insert(END,key)
    info[key]=(e2.get(),e3.get(),e4.get(),e5.get())
    clear()

def clear():
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)
  e4.delete(0,END)
  e5.delete(0,END)





lb=Listbox(w)

l1=Label(w,text="Address Book")
l2=Label(w,text="Name: ")
l3=Label(w,text="Address: ")
l4=Label(w,text="Mobile: ")
l5=Label(w,text="Email: ")
l6=Label(w,text="Birthdate: ")

e1=Entry(w)
e2=Entry(w)
e3=Entry(w)
e4=Entry(w)
e5=Entry(w)

b1=Button(w,text="Open",command=open)
b2=Button(w,text="Edit")
b3=Button(w,text="Delete")
b4=Button(w,text="Add/Update",command=add)
b5=Button(w,text="Save",command=save)

l1.grid(row=0,column=0,pady=10,padx=10)
b1.grid(row=0,column=1,padx=60)
lb.place(x=15,y=50)
b2.grid(row=6,column=1,padx=10,pady=10)
b3.grid(row=7,column=1,pady=10)
l2.grid(row=1,column=1)
l3.grid(row=2,column=1)
l4.grid(row=3,column=1)
l5.grid(row=4,column=1)
l6.grid(row=5,column=1)
e1.grid(row=1,column=2,padx=10)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)
e4.grid(row=4,column=2)
e5.grid(row=5,column=2)
b4.grid(row=6,column=2)
b5.grid(row=7,column=2)

mainloop()
