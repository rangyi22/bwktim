#tk_grid.py
import tkinter as tk
win = tk.Tk()
for r in range(2):
   for c in range(3):
      tk.Button(win, text=f'row={r},column={c}',
                borderwidth=1).grid(row=r,column=c)
win.mainloop()
