from tkinter import *
import random
import tkinter.messagebox

w=Tk()

def higher_lower():
  n=random.randint(1,20)
  guess=int(e2.get())
  if guess>n:
    tkinter.messagebox.showinfo(message="Too high.")
  if guess<n:
    tkinter.messagebox.showinfo(message="Too low.")
  if guess==n:
    tkinter.messagebox.showinfo(message="You got it! \nWell done.")

def name():
  player=e1.get()
  tkinter.messagebox.showinfo(message=f"Alright, {player}. \nI am thinking of a number between 1 and 20...")

l1=Label(w,text="Welcome to our game!")
l2=Label(w,text="Please enter your name:")
l3=Label(w,text="Take a guess: ")
l4=Label(w,text="     ")

e1=Entry(w,width=10)
e2=Entry(w,width=10)

b1=Button(w,text="    OK    ",command=name)
b2=Button(w,text="Submit",command=higher_lower)

l1.grid(row=0,column=0)
l4.grid(row=1,column=0)
l2.grid(row=2,column=0)
l3.grid(row=3,column=0)

e1.grid(row=2,column=1)
e2.grid(row=3,column=1)

b1.grid(row=2,column=2)
b2.grid(row=3,column=2)



mainloop()