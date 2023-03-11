#py09p11_NLE.py
import numpy as np
from scipy import optimize as opt

G=6.67e-11; Ms=1.98e30; Me= 5.98e24;
R=1.49e11; T=3.15576e7; w=2*np.pi/T
f = lambda r: G*(Ms/r**2 -Me/(R-r)**2) -r*w**2
# ~.fsolve() 함수를 사용한 비선형방정식 (P9.11.1)의 풀이
r0 = 1 # Initial guess
r = opt.fsolve(f,r0)
print('비선형 방정식의 해:\n', r)
print('그 잔류오차:', f(r))
# ~.roots() 함수를 사용한 다항방정식 (P9.11.2)의 풀이
A = [w**2, -2*R*w**2, w**2*R**2, G*(Me-Ms), 2*G*Ms*R, -G*Ms*R**2]
rr = np.roots(A)
print('다항방정식의 근들:\n', rr)
print('그 잔류오차들:\n', f(rr))
