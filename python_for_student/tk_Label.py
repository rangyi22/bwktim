#tk_Label.py
import tkinter as tk
win = tk.Tk()
label1 = tk.Label(win, text="label1")
label1.pack()
#label1["text"] = "text"
#label1.config(text="label1.config")
label2_var = tk.StringVar()
label2 = tk.Label(win, textvariable=label2_var)
label2.pack()
label2_var.set("label2_var.set")
#label2.config(text="label2.config")
win.mainloop()
