from tkinter import *

w=Tk()
w.geometry("900x300")
w.config(bg="grey5")

riddles="riddles.txt"
Qs_and_As=[]
all=[]
curindex=0
qcount=1
streak=0

with open(riddles) as file:
  for i in file:
    Qs_and_As.append(i.split(":"))

for i in Qs_and_As:
  for j in i:
    all.append(j)
  
for i in all:
  print(i)
    
def checkA():
  global curindex,qcount,streak
  if answer.get()==all[curindex+1]:
    if curindex+2==len(all):
      answer.destroy()
      check.destroy()
      streak+=1
      question.config(text="You've completed all the riddles.\nWell done!")
    else:
      curindex+=2
      qcount+=1
      streak+=1
      question.config(text=all[curindex])
      progress.config(text=f"Riddle {qcount}/{int(len(all)/2)}")
      ans_streak.config(text=f"Answer streak: {streak}")
      answer.config(bg="forest green")
      answer.delete(0,END)
  else:
    answer.config(bg="firebrick")
    streak=0
    ans_streak.config(text="")

question=Label(w,text=all[curindex],font=("calibri",20),bg="grey5",fg="white")
answer=Entry(w,font=("calibri",20),bg="grey10",fg="white")
check=Button(w,text="check",font=("calibri",20),bg="grey5",fg="white",command=checkA)
progress=Label(w,text=f"Riddle {qcount}/{int(len(all)/2)}",bg="grey5",fg="white",font=("calibri",20))
ans_streak=Label(w,text="",bg="grey5",fg="white",font=("calibri",20))

question.grid(row=0,column=0,pady=10)
answer.grid(row=1,column=0,padx=10,pady=10)
check.grid(row=2,column=0,padx=10,pady=10)
progress.grid(row=3,column=0,padx=375,pady=10)
ans_streak.grid(row=4,column=0)

mainloop()
