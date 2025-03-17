from tkinter import *
from tkinter.colorchooser import askcolor

class drawing:
  def __init__(self):
    self.w=Tk()
    self.pen=Button(self.w,text="PEN",command=self.draw)
    self.colour=Button(self.w,text="COLOUR",command=self.choosecolor)
    self.eraser=Button(self.w,text="ERASER",command=self.erase)
    self.clear_screen=Button(self.w,text="CLEAR",command=self.clear)
    self.pensize=Scale(self.w,from_=1,to=20,orient=HORIZONTAL)
    self.canvas=Canvas(self.w,bg="white",width=700,height=700)

    self.pen.grid(row=0,column=0)
    self.colour.grid(row=0,column=1)
    self.eraser.grid(row=0,column=2)
    self.clear_screen.grid(row=0,column=3)
    self.pensize.grid(row=0,column=4)
    self.canvas.grid(row=1,columnspan=5)

    self.setup()
  
  def setup(self):
    self.oldx=None
    self.oldy=None
    self.thickness=self.pensize.get()
    self.curcolor="black"
    self.curbutton=self.pen
    self.canvas.bind("<B1-Motion>",self.paint)
    self.canvas.bind("<ButtonRelease-1>",self.reset)

  def sink(self,btn):
    self.curbutton.config(relief=RAISED)
    btn.config(relief=SUNKEN)
    self.curbutton=btn

  def draw(self):
    self.sink(self.pen)
    self.curcolor="black" if self.curcolor=="white" else self.curcolor

  def erase(self):
    self.sink(self.eraser)
    self.curcolor="white"

  def choosecolor(self):
    self.curcolor=askcolor(color=self.curcolor)[1]

  def clear(self):
    self.canvas.delete("all")

  def paint(self,event):
    self.thickness=self.pensize.get()
    if self.oldx and self.oldy:
      self.canvas.create_line(self.oldx,self.oldy,event.x,event.y,width=self.thickness,fill=self.curcolor)
    self.oldx=event.x
    self.oldy=event.y
  
  def reset(self,event):
    self.oldx=None
    self.oldy=None

drawing()

mainloop()

