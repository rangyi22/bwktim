#tk_Label_Button_Entry.py
import tkinter as tk
win = tk.Tk()
entry = tk.Entry(win)
entry.grid(row=0, column=0) 
label = tk.Label(win, width=10)
label.grid(row=1) 
def entry_to_label():
   val = entry.get()
   label.config(text=val)
button = tk.Button(win, text="Get this entry vale", width=15,
                   command=entry_to_label)
button.grid(row=0, column=1) 
win.mainloop()
