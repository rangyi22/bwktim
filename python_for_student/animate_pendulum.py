#animate_pendulum.py
#> pip install scipy
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.8; L = 2.45; k = g/L # 중력가속도와 진자막대의 길이

# 미분방정식 (P8.11.1)
def dxdt(x, t, k):
   th, w = x  # State vector
   dxdt = [w, -k*np.sin(th)] 
   return dxdt

t = np.arange(0, 9.8, 0.05) # 시간 벡터
x0 = [0, 2*np.sqrt(k)] # 각도와 각속도의 초기치
# scipy.integrate.odeint() 함수를 이용한 미분방정식의 풀이
x = odeint(dxdt, x0, t, args=(k,))
# 진자막대 끝점의 좌표
xt = L*np.sin(x[:, ?]);  yt = -L*np.cos(x[?, 0]) # 식 (P8.11.2)
fig = plt.figure()
ax = plt.subplot(1,2,1, xlim=(-3, 3), ylim=(-3, 3)) 
ax.set_aspect('?????') # x-축과 y-축의 scale을 똑같게
line, = ax.plot([], [], 'o-', lw=2)

def animate(n): 
   xn = [0, xt[n]]
   yn = [0, yt[n]]
   line.set_data(xn, yn) 
   return line,

ani = FuncAnimation(fig, animate, range(1,len(x)), interval=10)
ax1 = plt.subplot(1,2,2, xlim=(0, 10), ylim=(0, 7))
ths = x[:,0];  ws = x[:,1]
ax1.plot(t, ths, t, ws)
plt.show()
