#py09e04_DE.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g = 9.8; L = 2.45 # 중력가속도와 Rod 길이
dt = 0.02
t = np.arange(0, 20, dt) # 0~20미만 구간에서 0.02간격으로 위치한 수열
k = g/L
def dx(x, t, k): # 매개변수 k를 가진 미분방정식(DE)
    dxdt = [x[1], -k*np.sin(x[0])]  # 식 (E9.4.2)
    return dxdt
#dx = lambda x, t, k: [x[1], -k*np.sin(x[0])] # 식 (E9.4.2)
x0s = [[0, 1.99*np.sqrt(k)], [0, 2*np.sqrt(k)]] # 초기치들
labels = ['w(0)=1.99*sqrt(k)','w(0)=2*sqrt(k)'] # 각 그래프에 대한 딱지
for i,x0 in enumerate(x0s): # 초기치 하나하나에 대해
   x = odeint(dx, x0, t, args=(k,)) # 매개변수 k를 가진 미방의 해
   th = x[:,0]; # 식 (E9.4.2b) 각도 th, 각속도는 w = x[:,1]
   plt.plot(t, th, label=labels[i])
plt.ylim(-5,15)
plt.legend()
plt.show()
