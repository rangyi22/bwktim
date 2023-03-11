#py05p01b.py
def mul(a=1):  # 입력인자 a의 default값을 1로 설정
   if type(a) != list:  y = a
   else:
     y = 1
     for x in a: 
        y = y * x
   return y
