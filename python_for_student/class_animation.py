#class_animation.py
from tkinter import *
class Ball:
  def __init__(self, xspeed, yspeed, size, color):
     self.shape=canvas.create_oval(10,10,size,size, fill=color)
     self.xspeed = xspeed 
     self.yspeed = yspeed
  def move(self):
     canvas.move(self.shape, self.xspeed, self.yspeed)
     pos = canvas.coords(self.shape)
     # pos[0:3]: shape의 좌상우하 좌표 xLeft,yTOP,xRight,yBottom
     if pos[3] >= HEIGHT or pos[1] <= 0:
       self.yspeed = -self.yspeed # 하한이나 상한에 부딪치면 반사
     if pos[2] >= WIDTH or pos[0] <= 0:
       self.xspeed = -self.xspeed  # 우한이나 좌한에 부딪치면 반사
WIDTH = 480;  HEIGHT = 360
win = Tk() # 폭이 480, 높이가 360인 최상위 그래픽 window 
win.title("Bouncing ball")
canvas = Canvas(win, width=WIDTH, height=HEIGHT) # Canvas widget
canvas.pack() # widget(들)을 win에 채워 넣어
ball1 = Ball(1, 2, 30, "red")
ball2 = Ball(2, 1, 50, "blue")
while True:
   ball1.move();  ball2.move() 
   canvas.update()
   canvas.after(10) # 10ms 동안 기다려
win.mainloop()
