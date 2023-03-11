#py05p01f.py
def fb(n): # Fibonacci number를 계산하기 위한 재귀적(recursive) 함수
   if n==0:  x = 0
   elif n==1: x = 1
   else: 
      x = fb(n-1) + fb(n-2)
   return x
