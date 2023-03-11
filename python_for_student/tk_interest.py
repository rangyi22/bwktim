#tk_interest.py
# https://www.python-course.eu/tkinter_entry_widgets.php
import tkinter as tk
from functools import partial
fields=['원금','이자율','Period 수','이자']
def makeform(win, fields):
   entries = {}
   for field in fields:
      frame = tk.Frame(win)
      frame.pack()
      ent = tk.Entry(frame)
      ent.insert(0, "0")
      lab=tk.Label(frame, width=15, text=field+": ", anchor='w')
      lab.pack(side=tk.LEFT)
      ent.pack(side=tk.RIGHT)
      entries[field] = ent
   return entries
def comp_int(entries): 
   P = float(entries['원금'].get())
   i = float(entries['이자율'].get())
   n = int(entries['Period 수'].get())
   Interest = P*(1+i)**n - P  # Compound interest(복리이자)
   entries['이자'].insert(0, Interest)
win = tk.Tk()
ents = makeform(win, fields)
button1 = tk.Button(win, text='Compound Interest',
                    command=(lambda e=ents: comp_int(e)))
                    #command=partial(comp_int, ents))
button1.pack(side=tk.LEFT, padx=5, pady=5)
win.mainloop()
