from tkinter import *
from tkinter.ttk import *

w=Tk()
w.title("Pizza App")
w.config(bg="black")

text1=StringVar()
text2=StringVar()
num1=IntVar()
pizzas="Cheese","Margherita","Peperoni","Hawaiian","BBQ","Vegetarian"

def setOrder():
  l3.config(text=f"Order set\n{num1.get()} {text2.get()} {text1.get()} pizza(s)")

l1=Label(w,text="Select Item:",background="black",foreground="white")
l1.grid(row=0,column=0,padx=5,pady=5)

l2=Label(w,text="Select Amount:",background="black",foreground="white")
l2.grid(row=1,column=0,padx=5,pady=5)

l3=Label(w,text="",background="black",foreground="white")
l3.grid(row=4,column=1,pady=5)

c1=Combobox(w,textvariable=text1,width=10)
c1["values"]=tuple(pizzas)
c1.grid(row=0,column=1,padx=10)

c2=Combobox(w,textvariable=num1,width=10)
c2["values"]=tuple(range(11))
c2.grid(row=1,column=1,padx=10)

r1=Radiobutton(w,text="S",variable=text2,value="small")
r1.grid(row=0,column=3,padx=10)

r2=Radiobutton(w,text="M",variable=text2,value="medium")
r2.grid(row=1,column=3,padx=5)

r3=Radiobutton(w,text="L",variable=text2,value="large")
r3.grid(row=2,column=3,padx=5,pady=5)

b=Button(w,text="Order",command=setOrder)
b.grid(row=2,column=0,padx=5,pady=5)

mainloop()
