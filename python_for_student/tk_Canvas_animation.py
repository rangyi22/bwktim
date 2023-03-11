#tk_Canvas_animation.py
# <https://www.magicmathmandarin.org/2017/05/17/python-for-fun-3-animation>
import tkinter as tk
import time
win = tk.Tk()
win.title("Bouncing ball")
WIDTH = 300;  HEIGHT = 150
canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()
ball = canvas.create_oval(10, 10, 30, 30, fill="orange")
xspeed = 1;  yspeed = 2
while True:
  canvas.move(ball, xspeed, yspeed)
  pos = canvas.coords(ball) # xLeft, yTOP, xRight, yBottom
if pos[2] >= WIDTH or pos[0] <= 0: xspeed = -xspeed 
if pos[3] >= HEIGHT or pos[1] <= 0: yspeed = -yspeed  
  win.update()
  time.sleep(0.01)
win.mainloop()
