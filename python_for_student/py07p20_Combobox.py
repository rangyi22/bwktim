#py07p20_Combobox.py
# https://www.youtube.com/watch?v=bKPIcoou9N8: 나도코딩 유튜브강의 
from tkinter.ttk import Combobox
import tkinter as tk
win = tk.Tk()
win.geometry("400x100"); 
vals = [str(i) + '점' for i in range(0,11)]
combobox = Combobox(win, width=10, height=5, values=vals, 
                    state='readonly')
combobox.current(0) # default로 0번째 값 설정
combobox.pack(side=tk.LEFT)
combobox.set("점수")
def butcmd():
   print('평점 =', combobox.get())
but = tk.Button(win, text="평가", command=butcmd)
but.pack(side=tk.LEFT)
win.mainloop()
