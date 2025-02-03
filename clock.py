from tkinter import *
import time
import random

w=Tk()
w.title("Clock app")

def rand_colour():
  return f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}"

def clock():
  current_time=time.strftime("%H:%M:%S %p")
  l1.config(text=current_time)
  l1.config(fg=rand_colour(),bg=rand_colour())
  l1.after(1000,clock)
  


l1=Label(w,font=("calibri",25)) 
l1.pack()
clock()

mainloop()
