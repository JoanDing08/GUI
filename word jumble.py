from tkinter import *
from tkinter import messagebox
import random

w=Tk()
w.title("WORD JUMBLE")
w.config(bg="black")

unjumbled=["green","deoxyribose","strawberry","midday","water","phosphodiester","computer","tkinter","plum","cinnamaldehyde","coat","maze","odessy","indoor","contradict","bell","atrioventricular","march","embark","arrange","radio","budget","beef","height","misfortunate","flight","fight","whole","rain","baron","barren","lump"]
jumbled=[]
count=0

for i in unjumbled:
  jumbled.append("".join(random.sample(i,len(i))))

def next():
  answer_box.delete(0,END)
  score.config(text=count)
  jumbled_word.config(text=random.choice(jumbled))

def checked():
  global count
  if answer_box.get() in unjumbled:
    count+=1
    next()
    if count>=10:
      w.destroy()
      messagebox.showinfo(message="CONGRATULATIONS!\nYOU WIN")
  else:
    next()

jumbled_word=Label(w,text=random.choice(jumbled),font=("calibri",25),bg="black",fg="white")
score=Label(w,text=count,font=("calibri",25),bg="black",fg="white")
answer_box=Entry(w,font=("calibri",25),width=16,bg="grey10",fg="white")
check=Button(w,text="CHECK",font=("calibri",25),command=checked,bg="grey5",fg="white")
reset=Button(w,text="RESET",font=("calibri",25),command=next,bg="grey5",fg="white")

jumbled_word.grid(row=0,column=0,pady=10,padx=15)
answer_box.grid(row=1,column=0,pady=10,padx=15)
check.grid(row=2,column=0,pady=10,padx=15)
reset.grid(row=3,column=0,pady=10,padx=15)
score.grid(row=4,column=0,pady=10,padx=15)

mainloop()
