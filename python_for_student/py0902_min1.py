#py0902_min1.py
import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt

f = lambda x: x**4 +3*(x-2)**3 -15*x**2 +1  # 식 (9.28)
# Unconstrained minimization (구속조건없는 최소화)
result = opt.minimize_scalar(f, method='Brent') # 'golden'도 좋아
xo = result.x;  fo = result.fun  # f를 최소화하는 x값과 최소화된 f값 f(xo)
print(f'Minimum: f({xo})={fo}')
# Constrained minimization (구속조건부 최소화)
result1 = opt.minimize_scalar(f, method='bounded', bounds=[0, 6])
xo1 = result1.x;  fo1 = result1.fun # [0,6]구간 내 f의 최소점과 최소값
print(f'Minimum 1: f({xo1})={fo1}') 
x = np.linspace(-8, 5, 100)
plt.plot(x,f(x), xo,f(xo),'o', xo1,f(xo1),'^')
plt.show()
