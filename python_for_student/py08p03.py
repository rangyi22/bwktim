#py08p03.py
import numpy as np
from scatterhist import scatterhist

N = 1000
x = np.random.randn(N) # Normal (Gaussian) 난수들 
y = np.random.rand(N)*2 # [0, 2] 구간에 분포하는 uniform 난수들
scatterhist(x, y)  # 그림 P8.3(a)
# x-축, y-축 범위와 histogram의 구간 수를 지정해 주고 싶다면
bs_x = [-4, 4];  bs_y = [0, 2] # x/y-축 범위 (x/y-limits)
Nbs = [20, 10] # 각 histogram의 구간(bin) 수
scatterhist(x, y, bs_x, bs_y, Nbs)  # 그림 P8.3(b)
