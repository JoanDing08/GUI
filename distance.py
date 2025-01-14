from tkinter import *

w=Tk()
w.title("distance calculator")
w.geometry("250x150")
w.config(bg="black")

def calculate():
  time=int(e1.get())
  speed=int(e2.get())
  distance=str(speed*time)
  l4.config(text=distance)

l1=Label(w,text="Time (hrs):",bg="black",fg="CadetBlue1")
l2=Label(w,text="Speed (km/h):",bg="black",fg="CadetBlue1")
l3=Label(w,text="Distance (km):",bg="black",fg="CadetBlue1")
l4=Label(w,text="",bg="black",fg="aquamarine")

e1=Entry(w,width=6,bg="black",fg="light salmon")
e2=Entry(w,width=6,bg="black",fg="light salmon")

b1=Button(w,text="Calculate",bg="black",fg="gold",command=calculate)


l1.place(x=10,y=10)
l2.place(x=10,y=60)
l3.place(x=10,y=110)
b1.place(x=180,y=30)

e1.place(x=120,y=10)
e2.place(x=120,y=60)
l4.place(x=120,y=110)

mainloop()
