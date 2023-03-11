#tk_Menu.py
import tkinter as tk
from functools import partial
win = tk.Tk()
def menu_callback(n):
   print("Menu", n)
def submenu_callback(n):
   print("Submenu", n)
menubar = tk.Menu(win)
submenu = tk.Menu(menubar, tearoff=False)
submenu.add_command(label="Submenu1",
                    command=partial(submenu_callback,1))
submenu.add_command(label="Submenu2",
                    command=partial(submenu_callback,2))
submenu.add_command(label="Exit", command=win.destroy)
menubar.add_cascade(label="Menu1", menu=submenu)
menubar.add_command(label="Menu2", command=partial(menu_callback,2))
menubar.add_command(label="Menu3", command=partial(menu_callback,3))
win.config(menu=menubar)
win.mainloop()
