#py09p16_opt.py
import numpy as np
from scipy import optimize as opt

f = lambda x: x[0]**3-5*x[0]**2+6*x[0]+x[1]**2-2*x[1]+x[2] 
c1 = lambda x: -x[0]**2-x[1]**2+x[2] # 구속조건 식 (P9.16b1) 
c2 = lambda x: x[0]**2 +x[1]**2 +x[2]**2 -6 # 식 (P9.16b2)
x0 = [1, 1, 1] # Initial guess of the optimal point (state)
bnds = [(0,np.inf), (0,np.inf), (0,5)] # 식 (P9.16b3, c)
cstrs = [{'fun': ??, 'type':'ineq'}, #부등식(inequality) 구속조건
         {'fun': c2, 'type':'????'}] #부등식(inequality) 구속조건
result = opt.minimize(f, x0, method='trust-constr', #tol=1e-4,
                      bounds=bnds, constraints=cstrs)
xo = result.x;  fo = result.fun
print(f'Constrained minimum: f({xo})={fo:9.4f}')
print(result.constr)
