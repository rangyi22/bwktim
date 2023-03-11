#py0902_min3.py
# Constrained minimization
import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt

f = lambda x: x[0]**2 -x[0]*x[1] -4*x[0] +x[1]**2 -x[1] # 식 (9.30a)
c1 = lambda x: 3 -0.7*(x[0]-1)**2 -x[1] # 부등식 구속조건 식 (9.30c1)
c2 = lambda x: (x [0]-1)**2 +x[1]**2 -4 # 등식 구속조건 식 (9.30c2)
x0 = [0, 0] # 최적점(optimal point)에 대한 초기 짐작(Initial guess)
bnds = [(0,5), (0,4)] # x[0]=x 및 x[1]=y 자체에 대한 제한조건
cstrs = [{'fun': c1, 'type':'ineq'}, # 부등식 (inequality) 구속조건
           {'fun': c2, 'type':'eq'}] # 등식(equality) 구속조건
result = opt.minimize(f, x0, method='trust-constr', #tol=1e-4,
                           bounds=bnds, constraints=cstrs)  
xo = result.x;  fo = result.fun
print(f'Minimum: f({xo})={fo:10.4f}')
x1 = np.arange(0,6,0.05)
x2 = np.arange(0,4,0.05)
X1, X2 = np.meshgrid(x1, x2)
F = f([X1,X2])
C1 = c1([X1,X2])
C2 = c2([X1,X2])
CS = plt.contour(X1, X2, F)  # 목적함수 (9.30a)에 대한 등고선
CS1 = plt.contour(X1, X2, C1, levels=[0]) # 식 (9.30b1)에 대한 그래프
CS2 = plt.contour(X1, X2, C2, levels=[0]) # 식 (9.30b2)에 대한 그래프
plt.clabel(CS, fontsize=10)  
plt.plot(xo[0],xo[1],'o') # 그림 9.14(a)
plt.show()
