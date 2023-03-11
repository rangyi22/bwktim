#fibonacci.py
xs = []
x, y = 0, 1
xs.append(x) 
for _ in range(5): # _는 익명의 변수
   x, y = y, x+y
   xs.append(x) 
