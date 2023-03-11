#tk_Scrollbar.py
import tkinter as tk
win = tk.Tk()
def get_listbox_value(event):
   x = listbox.get(listbox.curselection())
   label.config(text = f"x = {x}")
   print(x)
listbox = tk.Listbox(win)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar = tk.Scrollbar(win) 
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
for n in range(20):
   listbox.insert(tk.END, "Item" + str(n))
label = tk.Label(win, text="Which item?")
label.pack() #side=tk.BOTTOM)
listbox.bind('<<ListboxSelect>>', get_listbox_value)
scrollbar.config(command=listbox.yview)
win.mainloop()
