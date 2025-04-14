from tkinter import *

w=Tk()

def colour_quiz():
  import colourquiz

def places_quiz():
  import placequiz

l1=Label(w,text="select a topic",font=("consolas",30,"italic"))
l1.grid(row=0,columnspan=2,padx=30,pady=10)

colors=Button(w,text="Colours",bg="grey80",font=("consolas",20),command=colour_quiz)
colors.grid(row=1,column=0,padx=15,pady=10)

places=Button(w,text="Places",bg="grey80",font=("consolas",20),command=places_quiz)
places.grid(row=1,column=1,padx=15,pady=10)

mainloop()
