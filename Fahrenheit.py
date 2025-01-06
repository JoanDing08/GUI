from tkinter import *

w=Tk()
w.title("Celcius -> Fahrenheit")
w.config(bg="black")

def converted():
  fahrenheit=(float(c.get())*(9/5))+32

  f.delete("1.0",END)
  f.insert(END,fahrenheit)

t1=Label(w,text="    Temperature (C)    ",font=("arial",20),bg="black",fg="purple1")
t2=Label(w,text="New Temp. (F)",font=("arial",20),bg="black",fg="dark orange")
blank1=Label(w,text="    ",bg="black")
blank2=Label(w,text="   ",bg="black")

c=Entry(w,font=("arial",20),bg="black",fg="magenta",width=6)

f=Text(w,height=1,width=6,font=("arial",20),bg="black",fg="yellow")

convert=Button(w,text="Convert",font=("arial",20),bg="black",fg="blue",command=converted)

t1.grid(row=0,column=0)
c.grid(row=1,column=0)
convert.grid(row=2,column=0)
blank1.grid(row=3,column=0)
t2.grid(row=4,column=0)
f.grid(row=5,column=0)
blank2.grid(row=6,column=0)

mainloop()
