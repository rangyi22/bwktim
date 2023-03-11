#area.py
from mypkg.math.cal import mul
def triangle(b,h): # 밑변이 b, 높이가 h인 삼각형의 면적
   return mul(b,h)/2 # 'math.cal' module에 정의된 mul() 함수 사용 
def circle(r): # 반경이 r인 원의 면적
   return pi*r**2
from math import pi  # 원주율
