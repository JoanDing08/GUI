from tkinter import *
from gtts import gTTS
import os

w=Tk()
w.title("TEXT-TO-SPEECH")

def speak():
  tts=gTTS(text=e1.get(),lang="en",slow=False)
  tts.save("audio.wav")
  os.system("audio.wav")


l1=Label(w,text="Enter something to read out loud",font=("calibri",30))
l1.grid(row=0,column=0,pady=25,padx=25)

e1=Entry(w,font=("calibri",30))
e1.grid(row=1,column=0,pady=25,padx=25)

b1=Button(w,text="READ",font=("calibri",30),command=speak)
b1.grid(row=2,column=0,pady=25,padx=25)

mainloop()
