#py07p21_messagebox.py
# https://www.youtube.com/watch?v=bKPIcoou9N8: 나도코딩 유튜브강의  
import tkinter.messagebox as msgbox
import tkinter as tk
win = tk.Tk()
win.geometry("500x50"); 
def info():
   resp = msgbox.showinfo("알림", "예약 완료")
   print("응답:", resp) # ok 
def warn():
   resp = msgbox.showwarning("경고", "해당 도서 대출중")
   print("응답:", resp) # ok
def error():
   resp = msgbox.showerror("에러", "결제 오류 발생")
   print("응답:", resp) # ok
def okcancel():
   resp = msgbox.askokcancel("확인/취소", "대출하시겠습니까?")
   print("응답:", resp) # True(1)/False(0)
def retrycancel():
   resp = msgbox.askretrycancel("재시도/취소",
               "일시적 오류\n재시도하시겠습니까?")
   print("응답:", resp) # True(1)/False(0)
def yesno():
   resp = msgbox.askyesno("예/아니오", "예약하시겠습니까?")
   print("응답:", resp) # True(1)/False(0)
def yesnocancel():
   response = msgbox.askyesnocancel(title=None, 
                message="신청결과를 저장하고\n종료하시겠습니까?")
   print("응답:", response) # True(1)/False(0)/None
   if response == 1: print("저장후 종료")
   elif response == 0: print("저장하지 않고 종료")
   else: print("종료 최소")   
tk.Button(win, command=info, text="알림").pack(side=tk.LEFT)
tk.Button(win, command=warn, text="경고").pack(side=tk.LEFT)
tk.Button(win, command=error, text="에러").pack(side=tk.LEFT)
tk.Button(win, command=okcancel, 
          text="확인/취소").pack(side=tk.LEFT)
tk.Button(win, command=retrycancel, text="재시도/취소")
         .pack(side=tk.LEFT)
tk.Button(win, command=yesno, text="예/아니오").pack(side=tk.LEFT)
tk.Button(win, command=yesnocancel, 
          text="예/아니오/취소").pack(side=tk.LEFT)
win.mainloop()
