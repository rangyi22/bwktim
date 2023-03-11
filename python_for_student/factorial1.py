def factorial1(n): # Loop iteration 이용
   f = 1  # 0! (zero factorial) 값을 1로 초기화한다.
   for i in range(1, n+1):  f = f*i
   return f

print(factorial1(12))