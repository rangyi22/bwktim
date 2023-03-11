#graph_histogram.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(tight_layout=True) # create a canvas for plotting
Nx = 50000 # 발생시킬 Gaussian 난수(random number)들의 개수
m = 100  # 평균(Mean)
sigma = 15  # 표준편차(Standard deviation)
ys = m+sigma*np.random.randn(Nx) # Normal(Gaussian) 난수들
plt.subplot(2,2,1)
Nb = 16  # histogram에 대한 구간의 개수
plt.hist(ys, Nb)  # 그림 8.10(a)
plt.subplot(2,2,2)
plt.hist(ys, Nb, density=True) # 그림 8.10(b)
plt.subplot(2,2,3)
# ys에 담겨진 y값들 중 60미만은 60으로, 140 초과는 140으로 놓기 위해
# double list comprehension을 사용한다.
ys1=[60 if y<60 else y for y in [140 if y>140 else y for y in ys]]
# 계단형 도수분포도를 그리면서, 같은 데이터를 재사용하기 위해 뽑아놓는다.
ns, bins, patches = plt.hist(ys1, Nb, histtype='step') # 그림 (c)
# 이 중 각구간의 샘플 개수 ns와 구간의 경계값들인 bins list를 print한다.
print(f'ns={ns}\nbins={bins}')
bw = bins[1]-bins[0] # 이웃하는 경계값의 차이는 바로 각 막대의 폭이 된다.
xs = [x+bw/2 for x in bins[0:-1]] # 각 구간의 중심에 대한 x-좌표들
plt.plot(xs, ns, 'r:') # 그림 8.10(c)
plt.subplot(2,2,4)
plt.hist(ys, Nb, cumulative=True)  # 그림 8.10(d)
plt.show()
