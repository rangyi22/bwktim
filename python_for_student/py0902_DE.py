#py0902_DE.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

dt = 0.01 # 독립변수 간격
t = np.arange(0, 10, 0.01) # t=[0,10]에서 0.01씩 등간격을 가진 수열
def dx(x, t): # 상태변수 x, 독립변수 t에 관한 미분방정식 함수
    dxdt = [x[1], -3*x[1]-2*x[0]+10*np.sin(t)] # 상태방정식 (9.27a)
    return dxdt
# dx = lambda x, t: [x[1], -3*x[1]-2*x[0]+10*np.sin(t)]
x0 = [0, -3]  # 초기치 (9.27c)
x = odeint(dx, x0, t) # 미분방정식 함수 dx, 초기치 x0, 독립변수(벡터) t
y = x[:,0] # 출력식 (9.27b)
plt.plot(t, y)
plt.show()
