from tkinter import *


c=Tk()
c.title("CALENDAR")
c.config(bg="grey30")
c.geometry("440x330")


t=Label(c,text="  CALENDAR   ",font=("Constantia",50,"bold"),bg="grey20",fg="grey10")
t.place(x=0,y=0)

t2=Label(c,text="Enter Year",font=("Palatino Linotype",25),bg="grey30",fg="grey15")
t2.place(x=135,y=88)


box=Entry(c,width=4,font=("Times New Roman",20),bg="grey40",fg="grey25")
box.place(x=180,y=138)


b=Button(c,text="Show Calendar",font=("Palatino Linotype",20),bg="grey15",fg="grey9")
b.place(x=110,y=185)

exit=Button(c,text="Exit",font=("Palatino Linotype",20),bg="grey15",fg="grey9",command=c.destroy)
exit.place(x=175,y=255)


mainloop()
