#py08p02_random.py
import matplotlib.pyplot as plt
import random

N = 100000 
(a, b, c) = (-1, 2, 1)  
# 확률밀도함수가 균등(평평)한 높이를 갖는 난수들(Uniform random numbers)
xu = []
for n in range(N):
   xu.append(random.uniform(a, b)) # Uniform 난수 발생
# 확률밀도함수가 삼각형인 난수들 (Triangular random numbers)
xt = []
for n in range(N):
   xt.append(random.triangular(a, b, c)) # Triangular 난수 발생
Nb = 20  # histogram의 구간 수
plt.subplot(1,2,1); plt.hist(xu, bins=Nb)  # 그림 P8.2(a)
plt.subplot(1,2,2); plt.hist(xt, bins=Nb)  # 그림 P8.2(b)
plt.show()
