from tkinter import *

w=Tk()
w.title("Weight converter")
w.config(bg="black")

def convert():
  gram=float(e.get())*1000
  pounds=float(e.get())*2.205
  ounces=float(e.get())*35.274

  g.delete("1.0",END)
  g.insert(END,gram)
  lb.delete("1.0",END)
  lb.insert(END,pounds)
  oz.delete("1.0",END)
  oz.insert(END,ounces)

t1=Label(w,text="Enter weight (Kg)",font=("calibri",18),bg="black",fg="white")
t2=Label(w,text="Gram(s)",font=("calibri",15),bg="black",fg="white")
t3=Label(w,text="Pound(s)",font=("calibri",15),bg="black",fg="white")
t4=Label(w,text="Ounce(s)",font=("calibri",15),bg="black",fg="white")

e=Entry(w,font=("calibri",18),bg="black",fg="white")

b=Button(w,text="Convert",font=("calibri",18),bg="black",fg="white",command=convert)

g=Text(w,height=1,width=15)
lb=Text(w,height=1,width=15)
oz=Text(w,height=1,width=15)

t1.grid(row=0,column=0)
e.grid(row=0,column=1)
b.grid(row=0,column=2)

t2.grid(row=1,column=0)
t3.grid(row=1,column=1)
t4.grid(row=1,column=2)

g.grid(row=2,column=0)
lb.grid(row=2,column=1)
oz.grid(row=2,column=2)

mainloop()