#tk_login.py
import tkinter as tk
from functools import partial
username_password = {'홍길동': 'hgd1234', '한석봉': 'hsb3456'} 
def verify(username, password):
   이름 = username.get(); 비번 = password.get()
   if 이름 in username_password:
     if 비번 == username_password[이름]:
       label3_var.set('Welcome')
     else:  label3_var.set('비번이 틀렸습니다.')
   else:  label3_var.set('회원이신가요?')
win = tk.Tk()  
win.title('Tkinter Login Form - pythonexamples.org')
label1 = tk.Label(win, text="User Name")
username = tk.StringVar()
entry1 = tk.Entry(win, textvariable=username)
label1.grid(row=0, column=0); entry1.grid(row=0, column=1)
entry1.focus() # 처음에 cursor가 여기서 깜박거리며 기다리게 한다.
label2 = tk.Label(win, text="Password")
password = tk.StringVar()
entry2 = tk.Entry(win, textvariable=password, show='*')
label2.grid(row=1, column=0); entry2.grid(row=1, column=1)
verify_ = partial(verify, username, password)
button = tk.Button(win, text="Login", command=verify_)
entry2.bind("<Return>", verify_)
label3_var = tk.StringVar() 
label3 = tk.Label(win, textvariable=label3_var)
button.grid(row=2, column=0); label3.grid(row=2, column=1)  
win.mainloop()
