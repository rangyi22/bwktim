#py0902_NLE.py
import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt

f = lambda x: np.tan(np.pi-x) - x  # 식 (9.20) 또는 (9.21)
x1 = opt.fsolve(f, 1.6) # 초기치를 x0=1.6으로 해서 
x2 = opt.fsolve(f, 1.5) # 초기치를 x0=1.5으로 해서
x = np.linspace(-2.5, 2.5, 501) # x-축상 구간
plt.plot(x,f(x), x1,f(x1),'o', x2,f(x2),'^')
plt.show()
