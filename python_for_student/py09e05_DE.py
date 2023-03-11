#py09e05_DE.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

dt = 0.02
t = np.arange(0, 20, dt) # 0~20미만 구간에서 0.02간격으로 위치한 수열

def dx(x, t):
   dxdt = [-0.2*x[0]+0.1*x[0]*x[1], 4*x[1]-x[0]*x[1]] # 식 (E9.5.2)
   return dxdt

#dx = lambda x, t: [-0.2*x[0]+0.1*x[0]*x[1], 4*x[1]-x[0]*x[1]]
x0 = [3, 2] # 초기치
x = odeint(dx, x0, t) 
plt.plot(t, x[:,0], label='x(t)')
plt.plot(t, x[:,1], label='y(t)')
plt.legend()
plt.grid()
plt.show()
