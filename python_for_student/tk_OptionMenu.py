#tk_OptionMenu.py
import tkinter as tk
win = tk.Tk()
win.geometry("200x100"); 
option_var = tk.StringVar()# Option menu variable
option_var.set("Item1") # and its default value
option = tk.OptionMenu(win, option_var, "Item1", "Item2", "Item3")
option.grid(column=0)
def show():
   print("Selected item :", option_var.get())
but = tk.Button(win, text="Show", command=show)
but.grid(row=0, column=1)
win.mainloop()
