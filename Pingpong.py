from tkinter import *
import random
from tkinter import messagebox
import time

w=Tk()
w.title("Pingpong")

board=Canvas(w,bg="black",height=600,width=500,bd=1)
board.pack()

score=board.create_text(250,20,font=("consolas",12),text="   ",fill="white")
board.create_line(250,0,250,600,fill="white")

class ball():
  def __init__(self,board,p1,p2):
    self.board=board
    self.p1=p1
    self.p2=p2
    self.id=board.create_oval(10,10,50,50,fill="cornflower blue")
    self.board.move(self.id,250,300)
    self.x=random.randint(-3,3)
    self.y=random.randint(-3,3)
    self.canvas_height=self.board.winfo_height()
    self.canvas_width=self.board.winfo_width()
    self.p1score=0
    self.p2score=0
  def update(self):
    score.config(text=f"{self.p1score} {self.p2score}")
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
      board.itemconfig(score,text=f"{self.p1score} {self.p2score}")
    if pos[2]>=500:
      self.x=-4
      self.p1score+=1
      board.itemconfig(score,text=f"{self.p1score} {self.p2score}")
    if self.p1collide(pos)==True:
      self.x=4
    if self.p2collide(pos)==True:
      self.x=-4
  def p1collide(self,pos):
    ppos=self.board.coords(self.p1.id)
    if pos[1]>=ppos[1] and pos[1]<=ppos[3]:
      if pos[0]>=ppos[0] and pos[0]<=ppos[2]:
        return True
      return False
  def p2collide(self,pos):
    ppos=self.board.coords(self.p2.id)
    if pos[1]>=ppos[1] and pos[1]<=ppos[3]:
      if pos[0]>=ppos[0] and pos[0]<=ppos[2]:
        return True
    return False


class paddle1():
  def __init__(self,board):
    self.board=board
    self.id=board.create_rectangle(10,180,20,250,fill="white")
    self.y=0
    self.height=self.board.winfo_height()
    self.width=self.board.winfo_width()
    self.board.bind_all("w",self.up)
    self.board.bind_all("s",self.down)
  def draw(self):
    self.board.move(self.id,0,self.y)
    pos=self.board.coords(self.id)
    if pos[1]<=0:
      self.y=0
    if pos[3]>=600:
      self.y=0
  def up(self,event):
    self.y=-4
  def down(self,event):
    self.y=4

class paddle2():
  def __init__(self,board):
    self.board=board
    self.id=board.create_rectangle(470,390,480,490,fill="white")
    self.y=0
    self.height=self.board.winfo_height()
    self.width=self.board.winfo_width()
    self.board.bind_all("<KeyPress-Up>",self.up)
    self.board.bind_all("<KeyPress-Down>",self.down)
  def draw(self):
    self.board.move(self.id,0,self.y)
    pos=self.board.coords(self.id)
    if pos[1]<=0:
      self.y=0
    if pos[3]>=600:
      self.y=0
  def up(self,event):
    self.y=-4
  def down(self,event):
    self.y=4

player1=paddle1(board)
player2=paddle2(board)
circle=ball(board,player1,player2)

while True:
  if circle.p1score==10 or circle.p2score==10:
    messagebox.showinfo(message=f"Gameover. {circle.p1score}:{circle.p2score}")
    break
  circle.draw()
  player1.draw()
  player2.draw()
  w.update_idletasks()
  w.update()
  time.sleep(0.01)

mainloop()
