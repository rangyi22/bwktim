#py09p12_NLE.py
import numpy as np
from scipy import optimize as opt

c = 299792.458e3
A = np.array([15600, 18760, 17610, 19170])*1e3
B = np.array([7540, 2750, 14630, 610])*1e3
C = np.array([20140, 18610, 13480, 18390])*1e3
T = np.array([0.07074, 0.0722, 0.0769, 0.07242])
f = lambda x: \
      [np.sqrt((x[0]-A[?])**2+(x[?]-B[i])**2+(x[2]-C[?])**2) \
        -c*(T[i]-x[?]) for i in range(4)]  # 식 (P9.12.1)
x0 = [0, 0, 0, 0] # Initial guess
x = opt.fsolve(f,x0)
print('비선형 방정식의 해(fsolve):\n', x)
print('잔류오차:', f(x))
