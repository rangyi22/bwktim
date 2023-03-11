#tk_Radiobutton.py
import tkinter as tk
win = tk.Tk() 
v1 = tk.IntVar(); v2 = tk.IntVar(); v3 = tk.IntVar()
def show():
   v1 = v1.get();  v2 = v2.get();  v3 = v3.get()
   if v1==0: gender='?' # rbut1과 rbut2 둘 다 check되지 않았으면
   else: gender='M' if v1==1 else 'F'
   if v2==0: marital='?' # rbut3과 rbut4 둘 다 check되지 않았으면
   else: marital='Single' if v2==3 else 'Married'
   infection = 'uninfected' if v3==0 else 'infected'
   print(gender, marital, infection)
rbut1 = tk.Radiobutton(win, text='Male', variable=v1, value=1,  
                       command=show)
rbut2 = tk.Radiobutton(win, text='Female', variable=v1, value=2,           
                       command=show)
rbut1.pack(side=tk.LEFT); rbut2.pack(side=tk.LEFT)
rbut3 = tk.Radiobutton(win, text='Single', variable=v2, value=3, 
                       command=show)
rbut4 = tk.Radiobutton(win, text='Married', variable=v2, value=4, 
                       command=show)
rbut4.pack(side=tk.RIGHT); rbut3.pack(side=tk.RIGHT)
cbut = tk.Checkbutton(win, text='Infected?', variable=v3, 
                      command=show)
cbut.pack(side=tk.BOTTOM, padx=30)
cbut.invoke() # cbut가 (default로) check되게 한다.
win.mainloop()  
