#tk_grid_keypad.py
#https://www.youtube.com/watch?v=bKPIcoou9N8: 나도코딩 유튜브강의 
import tkinter as tk
win = tk.Tk()
win.geometry("210x180")
win.title("Keypad")
N=tk.N; E=tk.E; W=tk.W; S=tk.S; 
tk.Button(win, text="1", width=4, height=2).grid(row=0, 
          column=0, sticky=N+E+W+S)  
tk.Button(win, text="2").grid(row=0, column=1, sticky=N+E+W+S)
tk.Button(win, text="3").grid(row=0, column=2, sticky=N+E+W+S)
tk.Button(win, text="+").grid(row=0, column=3, sticky=N+E+W+S)
tk.Button(win, text="4").grid(row=1, column=0, sticky=N+E+W+S)
tk.Button(win, text="5", width=4, height=2).grid(row=1, 
          column=1, sticky=N+E+W+S)
tk.Button(win, text="6").grid(row=1, column=2, sticky=N+E+W+S)
tk.Button(win, text="-").grid(row=1, column=3, sticky=N+E+W+S)
tk.Button(win, text="7").grid(row=2, column=0, sticky=N+E+W+S)
tk.Button(win, text="8").grid(row=2, column=1, sticky=N+E+W+S)
tk.Button(win, text="9", width=4, height=2).grid(row=2,    
          column=2, sticky=N+E+W+S)
tk.Button(win, text="Enter", width=4, height=2).grid(row=2, 
          column=3, rowspan=2, sticky=N+E+W+S)
tk.Button(win, text="0", width=4, height=2).grid(row=3, 
          column=0, sticky=N+E+W+S)
tk.Button(win, text="*").grid(row=3, column=1, sticky=N+E+W+S)
tk.Button(win, text="/").grid(row=3, column=2, sticky=N+E+W+S)
win.mainloop()
