#tk_pack.py
import tkinter as tk
win = tk.Tk()
frame1 = tk.Frame(win)
frame1.pack(side=tk.LEFT) # win내 다음 widget frame2보다 왼쪽 
but1 = tk.Button(frame1, text="but1", fg="red")
but1.pack() # frame1내 다음 widget but2보다 위쪽
but2 = tk.Button(frame1, text="but2", fg="green")
but2.pack(side=tk.LEFT) # frame1내 다음 widget but3보다 왼쪽에
but3 = tk.Button(frame1, text="but3", fg="blue")
but3.pack(side=tk.RIGHT) # frame1내 다음 widget but4보다 오른쪽에
but4 = tk.Button(frame1, text="but4", fg="black")
but4.pack() 
frame2 = tk.Frame(win)
frame2.pack() 
but5 = tk.Button(frame2, text="but5", fg="black")
but5.pack(side=tk.LEFT) # frame2내 다음 widget but6보다 왼쪽에
but6 = tk.Button(frame2, text="but6", fg="red")
but6.pack() # frame2내 다음 widget but7보다 위쪽
but7 = tk.Button(frame2, text="but7", fg="blue")
but7.pack() 
win.mainloop()
