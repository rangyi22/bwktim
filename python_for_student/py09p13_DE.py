#py09p13_DE.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t0=0; tf=8; dt=0.01  # 초기시점, 종료시점, 시간간격
t = np.arange(t0, tf, dt) # 시간 벡터
V0=1 
dx=lambda x, t: \
      [V0*(1-(x[0]**2-x[1]**2)/(x[0]**2+x[1]**2)**2),
       -2*V0*x[0]*x[1]/(x[0]**2+x[1]**2)**2] # DE (P9.13.1)
x0s = [[-4,0.5],[-4,0.2], [-4,-0.2], [-4,-0.5]] # 초기치들
labels = ['(-4,0.5)','(-4,0.2)','(-4,-0.2)','(-4,-0.5)']
for i,x0 in enumerate(x0s): 
   x = odeint(dx, x0, t)
   plt.plot(x[:,0],x[:,1], label=labels[i])
plt.axis('equal')
plt.legend()
plt.show()
