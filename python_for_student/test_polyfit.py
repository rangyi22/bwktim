#test_polyfit.py
import numpy as np
import matplotlib.pyplot as plt

a = [2,-3,1]  # 한 다항함수 식 (E9.1.1)의 참(true) 계수벡터
fa = np.poly1d(a)  # 계수(벡터)가 a인 다항함수 식
print('True polynomial =\n', fa)
x = np.arange(-1, 2, 0.1)  # data point들의 x값들
Nx = len(x) # data point의 개수
sigma = 0.3 # fa(x)에 더해질 잡음의 표준편차(standard deviation)
y = fa(x) + sigma*np.random.randn(Nx) # fa(x)에 Gaussian 잡음을 더해 
# Data point들 (x,y)에 맞는 2차 다항함수의 계수를 추정한다.
a2 = np.polyfit(x,y, deg=2) # (x,y)에 맞는 2차 다항함수의 계수를 추정해
# 계수(벡터)가 a2인 다항함수 식을 만든다.
fa2 = np.poly1d(a2)  # 계수(벡터)가 a2인 다항함수 식
print('\n 추정된 fitting polynomial =\n', fa2)
plt.plot(x, y, 'bo', label="Data")
plt.plot (x, fa2(x), 'b-', label="Polyfit")
plt.xlabel('x'); plt.ylabel('y');  plt.legend()
plt.show()
