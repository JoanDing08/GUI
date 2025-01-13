from tkinter import *

w=Tk()
w.title("Celcius -> Fahrenheit")
w.config(bg="floral white")

def converted():
  fahrenheit=(float(c.get())*(9/5))+32

  f.delete("1.0",END)
  f.insert(END,fahrenheit)

t1=Label(w,text="    Temperature (C)    ",font=("arial",15),bg="floral white",fg="PeachPuff4")
t2=Label(w,text="New Temp. (F)",font=("arial",15),bg="floral white",fg="PeachPuff4")
blank1=Label(w,text="    ",bg="floral white")
blank2=Label(w,text="   ",bg="floral white")

c=Entry(w,font=("arial",20),bg="white",fg="PeachPuff3",width=6)

f=Text(w,height=1,width=6,font=("arial",20),bg="white",fg="PeachPuff3")

convert=Button(w,text="Convert",font=("arial",15),bg="PeachPuff2",fg="PeachPuff4",command=converted)

t1.grid(row=0,column=0)
c.grid(row=1,column=0)
convert.grid(row=2,column=0)
blank1.grid(row=3,column=0)
t2.grid(row=4,column=0)
f.grid(row=5,column=0)
blank2.grid(row=6,column=0)

mainloop()
