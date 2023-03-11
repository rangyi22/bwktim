#tk_Menu_popup.py
import tkinter as tk
from functools import partial
win = tk.Tk()
win.geometry("400x100"); 
label = tk.Label(win, text="Right-click to display menu")
label.pack()
but = tk.Button(win, text="Quit", command=win.destroy)
but.pack()
popup = tk.Menu(win, tearoff=0)
popup.add_command(label="Next", command=partial(print,'Next'))
popup.add_command(label="Prev", command=partial(print,'Prev'))
popup.add_separator()
popup.add_command(label="Home", command=partial(print,'Home'))
def do_popup(event):
   popup.tk_popup(event.x_root, event.y_root)
   # popup.grab_release()
win.bind("<Button-3>", do_popup)
win.mainloop()
