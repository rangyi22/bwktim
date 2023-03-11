#graph_3D_bar_and_histogram.py
import matplotlib.pyplot as plt
import numpy as np
from hist3d_my import * # 다른 파일에 정의된 내 함수를 사용하기 위해
from bar3d_my import * # 다른 파일에 정의된 내 함수를 사용하기 위해

dx = 0.5;  dy = 1 # Grid interval
x = np.arange(-2.5, 2.51, dx)
y = np.arange(-1, 1.1, dy)
X,Y = np.meshgrid(x, y)  # Grid 행렬들 (그림 8.18(a))
Z = np.exp(-X**2 - Y**2)
ax1 = plt.subplot(1,2,1, projection='3d')
bar3d_my(X, Y, Z, wx=dx/2, wy=dy/2, ax=ax1) # 그림 8.23(a)
#bar3d_my(X,Y,Z, ax=ax1)
ax2 = plt.subplot(1,2,2, projection='3d')  
x, y = np.random.rand(2, 100) * 4 # 숫자들의 범위를 0~4로 하기 위해
hist3d_my(x, y, Nb=8, ax=ax2)  # 그림 8.23(b)
