#mymain2.py
from mypkg.math.cal import *  # cal module 파일
from mypkg.math.area import * # area module 파일
print(mul(3, 4)) # cal module의 mul() 함수 사용
print(div(7, 2)) # cal module의 div() 함수 사용
print(circle(10)) # area module의 circle() 함수 사용
print(triangle(5,4)) # area module의 triangle() 함수 사용
