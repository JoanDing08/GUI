from tkinter import *
from tkinter.ttk import *

score=0
progress=0

quests=["Which city is in France?","Which country is in Europe?","Which landmark is in Africa?","Which country is shaped like a boot?","Which country is the biggest?"]

ans1=["Paris","Singapore","Eiffel Tower","Korea","Russia"]
ans2=["London","Finland","Great wall of China","Uganda","Canada"]
ans3=["Tokyo","Brazil","Taj Mahal","Italy","China"]
ans4=["Lubbock","Australia","Piramids of Giza","Vietnam","United States"]

correctAnswers=["Paris","Finland","Piramids of Giza","Italy","Russia"]

quiz=Tk()
quiz.title("Place Quiz")
text1=StringVar()

def next():
  global progress,score
  if text1.get() in correctAnswers:
    score+=1
  if progress<=len(quests):
    progress+=1
    if progress==len(quests):

      a1.destroy()
      a2.destroy()
      a3.destroy()
      a4.destroy()
      n.destroy()
      q.config(text=f"You've reached the end\nYour score was {score}/{len(quests)}")
  q.config(text=quests[progress])
  a1.config(text=ans1[progress],value=ans1[progress])
  a2.config(text=ans2[progress],value=ans2[progress])
  a3.config(text=ans3[progress],value=ans3[progress])
  a4.config(text=ans4[progress],value=ans4[progress])

q=Label(quiz,text=quests[progress])
a1=Radiobutton(quiz,text=ans1[progress],variable=text1,value=ans1[progress])
a2=Radiobutton(quiz,text=ans2[progress],variable=text1,value=ans2[progress])
a3=Radiobutton(quiz,text=ans3[progress],variable=text1,value=ans3[progress])
a4=Radiobutton(quiz,text=ans4[progress],variable=text1,value=ans4[progress])
n=Button(quiz,text="next",command=next)

q.grid(row=0,columnspan=2)
a1.grid(row=1,column=0,padx=2,pady=2)
a2.grid(row=1,column=1,padx=2,pady=2)
a3.grid(row=2,column=0,padx=2,pady=2)
a4.grid(row=2,column=1,padx=2,pady=2)
n.grid(row=3,columnspan=2,padx=2,pady=4)

mainloop()
