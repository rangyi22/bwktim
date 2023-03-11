#py0902_spline.py
import numpy as np
from scipy.interpolate import CubicSpline, UnivariateSpline
import matplotlib.pyplot as plt

x = np.array([0, 0.8, 1.5, 2.1, 3])
y = np.array([0, 1, 4, 2, 1]) #5, 4])
xi = np.linspace(0, x[-1], 301)
spl = CubicSpline(x, y) #, extrapolate=1)
S = spl.c # 각 구간에 대한 3차 다항함수 계수들
plt.plot(x,y,'o', xi,spl(xi), ms=5) # ms = Markersize
plt.show()
