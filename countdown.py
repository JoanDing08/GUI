from tkinter import *
from tkinter import messagebox
import time

w=Tk()

#declaration of variables

hour=StringVar()
minute=StringVar()
second=StringVar()

#setting default value of variables

hour.set("0")
minute.set("0")
second.set("0")

def link():
  total=int(hour.get())*3600+int(minute.get())*60+int(second.get())
  while total>=0:
    m,s=divmod(total,60)
    h=0
    if m>=60:
      h,m=divmod(m,60)
    hour.set(h)
    minute.set(m)
    second.set(s)
    w.update()
    time.sleep(1)
    if total==0:
      messagebox.showinfo(message="Time's up.")
    total-=1 

a=Entry(w,width=2,font=("Calibri",30),textvariable=hour)
b=Entry(w,width=2,font=("Calibri",30),textvariable=minute)
c=Entry(w,width=2,font=("Calibri",30),textvariable=second)

strt=Button(w,text="Start \nCountdown",font=("Calibri",10),command=link)

a.grid(row=0,column=0,padx=5)
b.grid(row=0,column=1,padx=5)
c.grid(row=0,column=2,padx=5)
strt.grid(row=1,column=1,pady=10)

mainloop()
