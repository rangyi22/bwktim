#tk_Listbox.py
import tkinter as tk 
win = tk.Tk()
list_var = tk.StringVar() # 문자열형 tkinter 변수 
list_var.set(('Python', 'Java', 'C++'))
listbox = tk.Listbox(win, listvariable=list_var)
listbox.pack()
def select():
   print(listbox.curselection())
   if len(listbox.curselection()) < 1: # 아무것도 선택되지 않았으면
     val = "Choose one, please."
   else:  # 뭔가 선택된 게 있다면
     val = listbox.get(listbox.curselection()) # 그걸 잡아서 val에 저장
   label_var.set(val)  
button = tk.Button(win, text='Select', width=15, height=1,
                   command=select)
button.pack()
label_var = tk.StringVar() # 문자열형 tkinter 변수
label = tk.Label(win, width=20, textvariable=label_var)
label.pack() 
win.mainloop()
