#tk_Canvas.py
# <https://www.python-course.eu/tkinter_canvas.php>
import tkinter as tk
WIDTH = 250;  HEIGHT = 180
win = tk.Tk()
win.title("Widgets available in tk.Canvas")
canvas = tk.Canvas(win, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.create_oval(10, 10, 90, 50, fill="orange")
canvas.create_rectangle(10, 10, 90, 50, dash=1) 
canvas.create_text(90,50, text="(90,50)")
좌표 = 10, 70, 110, 170
canvas.create_arc(좌표, start=0, extent=135, fill="red")
canvas.create_polygon(10,70, 110,70, 110,170, 10,170, 
                      fill='', outline='Red')
canvas.create_line(180, 100, 230, 130, 200, 160, 
               fill='Blue', width=2) 
fname = tk.PhotoImage(file="풍경.gif") 
canvas.create_image(250, 10, anchor=tk.NE, image=fname)
label = tk.Label(win, text='text widget in Canvas.window')
canvas.create_window(100, 150, window=label)
canvas.create_text(110,170, text="(110,170)")
