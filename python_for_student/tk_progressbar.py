#tk_progressbar.py
import tkinter as tk
from tkinter.ttk import Progressbar
import time
win = tk.Tk() 
progress = Progressbar(win, orient=tk.HORIZONTAL, length=100,  
                  mode='determinate') # mode='indeterminate') 
def bar(): 
   s = 0
   for n in range(101):
      s += n
      progress['value'] = n
      win.update_idletasks() 
      time.sleep(0.02)
      label['text'] = str(n)
tk.Button(win, text='Start', command=bar).pack() 
label = tk.Label(win, text='n')
progress.pack()
label.pack()
win.mainloop()
