#tk_Mouse_Key_Text.py
import tkinter as tk
from functools import partial
win = tk.Tk()
text = tk.Text(win, width=50, height=1)
text.insert(tk.END, "Click any point to see its x,y-coordinates.")
text.pack(side=tk.TOP)
label = tk.Label(win, text="Mouse pointer 좌표") 
label.pack()
def B1_callback(event):
   info = f"clicked at ({event.x},{event.y})" # 표 7.11 참조
   label.config(text=info)
def B3_callback(event):
   info = f"right-clicked at ({event.x},{event.y})."
   label_write(info)
def Key_callback(event):
   info = f"Key {event.keysym} has been pressed."
   label_write(info)
def ESC_callback(event):
   win.destroy()
def label_write(s, event=None): # event의 default값을 None으로 설정
   label.config(text=s)
win.bind("<Button-1>", B1_callback) # 좌-click event handler 등록 
win.bind("<Button-3>", B3_callback) # 우-click event handler 등록
win.bind("<Key>", Key_callback) # Any key event handler 등록 (표 7.12)
win.bind("<Escape>", ESC_callback) # ESC key event handler 등록
text.bind("<Enter>", partial(label_write, "<Enter> text")) # 표 7.12
win.mainloop()
