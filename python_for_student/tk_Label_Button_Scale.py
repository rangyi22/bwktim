#tk_Label_Button.py
import tkinter as tk
from functools import partial # 5.10절 (Remark 5.2) 참조 
win = tk.Tk()
label = tk.Label(win, text="0")
label.pack()
def change_counter(num):
   counter = int(str(label['text'])) + num
   label.config(text=str(counter))

number = 0
button1 = tk.Button(win, text="Change", width=10, # height=1,
                   command=partial(change_counter, number))
button1.pack()
scale_var = tk.IntVar() # tkinter.IntVar(정수)형 변수
scale = tk.Scale(win, from_=-10, to=10, variable=scale_var,
                 orient= tk.HORIZONTAL)
scale.pack() 
def get_var():
   global number
   number = scale_var.get()
   label1.config(text= "number = " + str(number))
button2 = tk.Button(win, text="Scale value", command=get_var)
button2.pack(anchor=tk.CENTER)
label1 = tk.Label(win)
label1.pack()
win.mainloop()
