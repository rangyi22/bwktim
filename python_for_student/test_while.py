#test_while.py
# 최소 양수를 얻기 위해 2로 나누는 것을 반복한다.
x=1 
while x/2>0: # 2로 나눈 값이 0보다 큰 한
   x=x/2 # 나누기 2를 반복한다.
x_min=x
print(f'x_min ={x_min: 27.20e}')
# 최대 양수를 얻기 위해 2를 곱하는 것을 반복한다. 
x=1.
inf = float('inf')  
while 2*x<inf: # 2를 곱한 값이 inf보다 작은 한
   x = x*2 # 곱하기 2를 반복한다.
x_max0 = x # 2의 배수 중 Python에서 표현될 수 있는 최대 수
print(f'x_max0 ={x_max0: 27.20e}')
tmp=1
while x_max0*(2-tmp/2)<inf: # (2-tmp/2)를 곱한 값이 inf보다 작은 한
   tmp = tmp/2  # tmp를 2로 나누는 작업을 반복한다.
x_max = x*(2-tmp) # Python에서 표현될 수 있는 최대 수
print(f'x_max ={x_max: 27.20e}')
