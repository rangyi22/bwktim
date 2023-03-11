#tk_그림판.py
# <https://cafe.naver.com/funcc/50889>
import tkinter as tk
win = tk.Tk() 
win.title("Paint App") 
WIDTH = 480;  HEIGHT = 360
canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack() 
def paint(event): 
   x1, x2 = (event.x - 1), event.x
   y1, y2 = (event.y - 1), event.y
   canvas.create_oval(x1, y1, x2, y2, fill="BLUE")
def delete_all(event):
   canvas.delete('all')
canvas.bind("<B1-Motion>", paint) # Left Mouse button click-drag
canvas.bind("<Button-3>", delete_all) # Right Mouse button click
label = tk.Label(win, text="Click and Drag to draw.") 
label.pack() 
win.mainloop()
