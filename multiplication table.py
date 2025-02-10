from tkinter import *
from tkinter.ttk import *

w=Tk()

num1=IntVar()
num2=IntVar()

def generate():
  tables=""
  for i in range(num2.get()+1):
    tables+=f"{int(num1.get())}x{int(i)}={int(num1.get())*int(i)}\n"
  l3.config(text=tables)

l1=Label(w,text="Multiplication Table",font=("calibri",10))
l1.grid(row=0,column=0,pady=20)

l2=Label(w,text="Number and Range: ",font=("calibri",10))
l2.grid(row=1,column=0,pady=20)

c1=Combobox(w,textvariable=num1,width=5)
c1["values"]=tuple(range(101))
c1.grid(row=1,column=1,padx=10)

r1=Radiobutton(w,text="10",variable=num2,value=10)
r1.grid(row=1,column=2,padx=10)

r2=Radiobutton(w,text="20",variable=num2,value=20)
r2.grid(row=2,column=2,pady=2)

r3=Radiobutton(w,text="30",variable=num2,value=30)
r3.grid(row=3,column=2,pady=2)

b1=Button(w,text="Generate",command=generate)
b1.grid(row=2,column=0,pady=2)

l3=Label(w,text="",font=("calibri",10))
l3.grid(row=4,column=1,pady=5)

mainloop()
