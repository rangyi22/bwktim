#tk_Label_Entry.py
import tkinter as tk
win = tk.Tk()
entry_var = tk.StringVar()
entry = tk.Entry(win, textvariable=entry_var)
entry.insert(0, "entry")
label1 = tk.Label(win, text="label1") 
label2 = tk.Label(win, text="label2") 
entry.pack(); label1.pack(); label2.pack()
def entry_get(arg=None):
   label1.config(text="entry.get(): " + entry.get())
   label2.config(text="entry_var.get(): " + entry_var.get())
   entry.delete(0, tk.END)
# Enter Key event에 entry_get() 함수를 handler function으로 등록   
entry.bind("<Return>", entry_get) 
win.mainloop()
