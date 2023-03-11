#py02p35a_while.py
X, y = 8, 12
while(y):
   x, y = y, x % y  # %는 나머지(modulo/remainder) 연산자
print(x)
