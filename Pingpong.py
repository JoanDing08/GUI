from tkinter import *
import random
from tkinter import messagebox

w=Tk()
w.title("Ping-pong")

board=Canvas(w,bg="black",height=600,width=500,bd=1)
board.pack()

score=board.create_text(250,20,font=("consolas",12),text=" : ",fill="red")
board.create_line(250,0,250,600,fill="white")

class ball():
  def __init__(self,board,p1,p2):
    self.id=board.create_oval(10,10,50,50,fill="gold")
    self.board.move(self.id,250,300)
    self.x=random.randint(-3,3)
    self.y=random.randint(-3,3)
    self.p1score=0
    self.p2score=0
  def draw(self):
    self.board.move(self.id,self.x,self.y)
    pos=self.board.coords(self.id)
    if pos[1]<=0:
      self.y=4
    if pos[3]>=600:
      self.y=-4
    if pos[0]<=0:
      self.x=4
      self.p2score+=1
      board.itemconfig(score,text=f"{self.p1score}:{self.p2score}")
    if pos[2]>=500:
      self.x=-4
      self.p1score+=1
      board.itemconfig(score,text=f"{self.p1score}:{self.p2score}")
  def p1collide(self,pos):
    p1pos=self.board.coords(self.p1.id)
    if pos[1]>p1pos[1] and pos[1]<p1pos[3]:
      

class p1():
  def __init__(self,board):
    self.board=board
    self.id=board.create_rectangle(10,20,90,100)
    self.y=0
    self.height=self.board.winfo_height()
    self.width=self.board.winfo_width()
    self.board.bind_all("W",self.up)
    self.board.bind_all("S",self.down)
  def draw(self):
    self.board.move(self.id,self.y)
    pos=self.board.coords(self.id)
    if pos[1]<=0:
      self.y=0
    if pos[3]>=600:
      self.y=0
  def up(self,event):
    self.y=-4
  def down(self,event):
    self.y=4

class p2():
  def __init__(self,board):
    self.board=board
    self.id=board.create_rectangle(10,20,90,100)
    self.y=0
    self.height=self.board.winfo_height()
    self.width=self.board.winfo_width()
    self.board.bind_all("<KeyPress-Up>",self.up)
    self.board.bind_all("<KeyPress-Down>",self.down)
  def draw(self):
    self.board.move(self.id,self.y)
    pos=self.board.coords(self.id)
    if pos[1]<=0:
      self.y=0
    if pos[3]>=600:
      self.y=0
  def up(self,event):
    self.y=-4
  def down(self,event):
    self.y=4

mainloop()
