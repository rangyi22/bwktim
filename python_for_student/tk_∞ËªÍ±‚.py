#tk_계산기.py
import tkinter as tk
from functools import partial
from math import *
def compute(n, event=None):
   A = entryA.get();  B = entryB.get()
   A = float(A);  B = float(B)
   if n==1:  result = A + B
   elif n==2:  result = A - B
   elif n==3:  result = A * B
   else:  result = A / B
   write_entry(result)
def write_entry(value):
   entryC.delete(0, 'end')
   entryC.insert(tk.END, str(value))
win = tk.Tk()
win.title('My Calculator')
frame1 = tk.Frame(win); frame1.pack()
labelA = tk.Label(frame1, text='A').pack(side=tk.LEFT)
entryA = tk.Entry(frame1, width=12)
entryB = tk.Entry(frame1, width=12)
entryA.pack(side=tk.LEFT); entryB.pack(side=tk.RIGHT)
labelB = tk.Label(frame1, text='B').pack(side=tk.RIGHT)
frame2 = tk.Frame(win)
frame2.pack()
but1 = tk.Button(frame2, text='A+B', command=partial(compute,1))
but2 = tk.Button(frame2, text='A-B', command=partial(compute,2))
but3 = tk.Button(frame2, text='A*B', command= partial(compute,3))
but4 = tk.Button(frame2, text='A/B', command= partial(compute,4))
but1.pack(side=tk.LEFT); but2.pack(side=tk.LEFT)
but3.pack(side=tk.LEFT); but4.pack(side=tk.LEFT)
frame3 = tk.Frame(win)
frame3.pack()
label1=tk.Label(frame3, text='Result or Your expression').pack()
entryC =tk.Entry(frame3, width=32)
entryC.pack()    
win.mainloop()
