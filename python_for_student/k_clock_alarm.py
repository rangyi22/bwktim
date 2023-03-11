#tk_clock_alarm.py
import tkinter as tk
from datetime import datetime, timedelta
import os, re, winsound

def update_clock():
   now = datetime.now()
   now_str = now.strftime("%Y-%m-%d %H:%M:%S")
   label.config(text=now_str)
   win.after(1000, update_clock) #1000ms후 update_clock() 함수 실행
   if type(alarm_time)==datetime:
     if alarm_time<now<alarm_time+timedelta(seconds=2):
       beep(1)
       entry.delete(0, tk.END)     
def set_alarm(arg=None):
   global alarm_time
   time_str = entry_var.get()
   L = re.split(':', time_str)
   if len(L)<3: entry_var.set("00:00:00"); beep(1); return
   now = datetime.now()
   Y = now.year; M = now.month; D = now.day
   H, m, s = int(L[0]), int(L[1]), int(L[2])
   alarm_time = datetime(Y, now.month, now.day, H, m, s)
   if alarm_time < now:
     entry_var.set("Already passed."); beep(1,500)
def beep(ts=1, freq=2000):
   duration = ts*1000  # Convert ts[sec] into Duration[ms] 
   winsound.Beep(freq, duration) # beep 
win = tk.Tk()
win.geometry("230x50"); win.title("Tk clock")
label = tk.Label(win, fg="Red", font=("Helvetica", 18))
label.pack()  
but1 = tk.Button(win, text="Alarm(hh:mm:ss)", command=set_alarm)
but1.pack(side=tk.LEFT)
entry_var = tk.StringVar()
entry = tk.Entry(win, textvariable=entry_var)
entry.pack(side=tk.RIGHT)
entry.bind("<Return>", set_alarm)
win.after(1000, update_clock)
win.mainloop()
