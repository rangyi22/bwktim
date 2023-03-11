#tk_Label_Button.py
import tkinter as tk
from functools import partial # 5.10절 (Remark 5.2) 참조 
win = tk.Tk()
label = tk.Label(win, text="0")
label.pack()
def change_counter(num):
   counter = int(str(label['text'])) + num
   label.config(text=str(counter))
button1 = tk.Button(win, text="Up", width=10, # height=1,
                    command=partial(change_counter, 1))
button1.pack(side=tk.LEFT)
button2 = tk.Button(win, text="Down", width=10, # height=1,
                    command=lambda: change_counter(-1))
button2.pack(side=tk.LEFT)
win.mainloop()
