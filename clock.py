from tkinter import *
import time
import random

w=Tk()
w.config(bg="blue")
w.title("Clock app")

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

def randcolour():
  return f"#{r:02x}{g:02x}{b:02x}"

def clock():
  current_time=time.strftime("%H:%M:%S %p")
  l1.config(text=current_time)
  if int(time.strftime("%S"))%2==0:
    l1.config(bg=randcolour())
  else:
    l1.config(bg=randcolour())
  l1.after(1000,clock)
  


l1=Label(w,bg="blue",font=("calibri",25)) 
l1.pack()
clock()

mainloop()
