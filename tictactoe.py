from tkinter import *
from tkinter import messagebox

class tictactoe:
  def __init__(self,root):
    self.root=root
    self.root.title("Tic Tac Toe")
    self.defplayer="X"
    self.buttons=[[None for _ in range(3)] for _ in range(3)]
    self.makeButton()
  def makeButton(self):
    for row in range(3):
      for column in range(3):
        button=Button(self.root,text=" ",font=("Calibri",30),width=5,height=2,command=lambda r=row,c=column:self.clicked(r,c))
        button.grid(row=row,column=column)
        self.buttons[row][column]=button
  def clicked(self,row,column):
    if self.buttons[row][column]["text"]==" " and not self.check_winner():
      self.buttons[row][column]["text"]=self.defplayer
      if self.check_winner():
        messagebox.showinfo(message=f"GameOver. \nPlayer {self.defplayer} wins!")
      elif self.full_house():
        messagebox.showinfo(message="GameOver. It's a tie.")
      else:
        if self.defplayer=="X":
          self.defplayer="O"
        else:
          self.defplayer="X"
  def check_winner(self):
    for row in range(3):
      if self.buttons[row][0]["text"]==self.buttons[row][1]["text"]==self.buttons[row][2]["text"]!=" ":
        return True
    for column in range(3):
      if self.buttons[0][column]["text"]==self.buttons[1][column]["text"]==self.buttons[2][column]["text"]!=" ":
        return True
    if self.buttons[0][0]["text"]==self.buttons[1][1]["text"]==self.buttons[2][2]["text"]!=" ":
      return True
    if self.buttons[0][2]["text"]==self.buttons[1][1]["text"]==self.buttons[2][0]["text"]!=" ":
      return True
    return False

  def full_house(self):
    return all(self.buttons[row][column]["text"]!=" " for row in range(3) for column in range(3))
  
root=Tk()

game=tictactoe(root)

mainloop()
