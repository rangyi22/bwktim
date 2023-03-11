#mycal.py
def mul(x, y): # 곱셈(Multiplication)
   return x * y
def div(x, y): # 나눗셈(Division)
 return x / y
def circle_area(r): # 반경 r인 원의 면적
 return pi*r**2
from math import pi  # math module로부터 원주율 pi를 import
if __name__ == "__main__":
  print("circle_area(10) in 'mycal.py' =", circle_area(10))
