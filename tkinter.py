from tkinter import *

"""window=Tk()
window.geometry("300x300")
window.config(bg="black")

button1=Button(window,text="Hello",font=("Calibri",30,"bold"),foreground="white",bg="blue",bd=5,relief="raised")
button1.place(x=50,y=50)"""

#creating a simple login page

window=Tk()
window.geometry("500x300")
window.config(bg="light blue")
window.title("Login")

l1=Label(window,text="User:",font=("Calibri",30,"bold"),bg="light blue",fg="white")
l1.place(x=20,y=20)

l2=Label(window,text="Password:",font=("Calibri",30,"bold"),bg="light blue",fg="white")
l2.place(x=20,y=100)

t1=Entry(window,font=("calibri"),bg="white")
t1.place(x=200,y=40)

t2=Entry(window,show="*",font=("calibri"),bg="white")
t2.place(x=200,y=120)

confirm=Button(window,text="Log In",font=("Calibri",30),fg="white",bg="light pink",command=window.destroy)
confirm.place(x=20,y=180)
