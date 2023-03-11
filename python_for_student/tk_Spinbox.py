#tk_Spinbox.py
import tkinter as tk
win = tk.Tk()
sp_var = tk.DoubleVar()
xmin, xmax, inc = -10, 10, 2
spbox = tk.Spinbox(win, from_=xmin, to=xmax, increment=inc,
                   textvariable=sp_var, width=10)
def show_spbox_value():
   x = spbox.get()
   label.config(text=f"x = {x}")
txt = f"Click to get x from spbox({xmin}:{inc}:{xmax})!"
button = tk.Button(win, text=txt, width=30,
                   command = show_spbox_value)
spbox.grid(row=0, column=0); button.grid(row=0, column=1)
label = tk.Label(win, text="0")
label.grid(row=1)
win.mainloop()
