#py09p15_opt.py
import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt

f = lambda x: ((x[0]+1.5)**2+5*(x[1]-1.7)**2)* \
         ((x[0]-1.4)**2+.6*(x[1]-.5)**2) # 목적함수 (P9.15.1a)
c1 = lambda x: 1-3*x[0]?4*x[1] +4*x[1]**2 # 부등식 (P9.15.1b1) 
c2 = lambda x: 7?3*x[0]+x[0]*x[1]-4*x[1] # 부등식 (P9.15.1b2)
c3 = lambda x: 3-2*x[0]?x[1] # 등식 (P9.15.1b3)
x0 = [0, 0] # Initial guess of the optimal point
bnds = [(0, np.inf), (0, np.inf)]
cstrs = [{'fun': c1, 'type':'ineq'},#부등식(inequality) 구속조건
         {'fun': c2, 'type':'????'},# 부등식(inequality) 구속조건
         {'fun': c3, 'type':'eq'}] # 등식(equality) 구속조건
result = opt.minimize(f, x0, method='trust-constr', #tol=1e-4,
                      bounds=bnds, constraints=cstrs)  
xo = result.x;  fo = result.fun
print(f'Constrained minimum: f({xo})={fo:9.4f}')
fig = plt.figure()
x1 = np.arange(0, 2.5, 0.025)
x2 = np.arange(-0.5, 2, 0.025)
X1, X2 = np.meshgrid(x1, x2)
F = f([X1,X2])
C1 = c1([X1,X2]); C2 = c2([X1,X2]); C3 = c3([X1,X2])
Ls = [0.1, 0.5, 1, 2, 3, 5, 10, 20, 30, 40] 
CS = plt.contour(X1, X2, F, levels=Ls)  # 목적함수 (P9.15.1a)
CS1 = plt.contour(X1, X2, C1, levels=[0]) # 식 (P9.15.1b1)
CS2 = plt.contour(X1, X2, C2, levels=[0]) # 식 (P9.15.1b2)
CS3 = plt.contour(X1, X2, C3, levels=[0], linestyles='dotted') 
                         # 식 (P9.15.1b3)에 대한 그래프
plt.plot([0, 2.5],[0, 0],'k')
plt.clabel(CS, fontsize=10)  
plt.plot(xo[0],xo[1],'o') # 그림 P9.15
plt.show()
