#hist_random.py
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(tight_layout=True) # 그래프를 그릴 canvas 생성
Nx = 50000 # 발생시킬 난수의 개수
m = 100  # 발생시킬 Gaussian 난수의 평균(mean)
sigma = 15  # 발생시킬 Gaussian 난수의 표준편차(standard deviation) 
xn = m + sigma*np.random.randn(Nx) # Normal(Gaussian) 난수 발생
plt.subplot(1,2,1) # 그래프창을 좌우 두 개로 나눠서 그 중 첫 번째 부분에
Nb = 50  # histogram 구간의 개수
ns, bins, patches = plt.hist(xn, Nb, density=True)
ys = (1/(np.sqrt(2*np.pi)*sigma) *
       np.exp(-((bins-m)/sigma)**2/2)) # Gaussian 밀도 함수 식 (9.5)
plt.plot(bins, ys, 'r--')  # bins에 대해 ys를 빨간 쇄선으로 그려
a = -1;  b = 2  # uniform 구간의 좌/우한을 각각 -1/2로 설정
xu = np.random.uniform(a,b,Nx) # Uniform 난수 발생
plt.subplot(1,2,2) # 그래프창을 좌우 두 개로 나눠서 그 중 첫 번째 부분에
Nb = 20  # histogram 구간의 개수
ns, bins, patches = plt.hist(xu, Nb, density=True)
ys = [1/(b-a) for bin in bins] # Uniform 밀도 함수 식 (9.6)
plt.plot(bins, ys, 'r--')  # bins에 대해 ys를 빨간 쇄선으로 그려
plt.show()
