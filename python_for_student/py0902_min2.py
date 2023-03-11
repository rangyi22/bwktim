#py0902_min2.py
import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt

f = lambda x: x[0]**2 -x[0]*x[1] -4*x[0] +x[1]**2 -x[1]  # 식 (9.29)
x0 = [0, 0]  # 최적점(optimal point)에 대한 초기 짐작(Initial guess)
ps = [x0]

def reporter(p): # 최적화 과정의 단계 단계를 capture하기 위해
    global ps
    ps.append(p)
    
result = opt.minimize(f, x0, tol=1e-4, callback=reporter)
xo = result.x;   fo = result.fun # 최소점 xo와 최소값 fo
print(f'Minimum: f({xo})={fo}')
ps = np.array(ps) # 해를 향한 여정의 발자취를 list에서 ndarray로 정렬시켜 
print(ps)  # 그 숫자의 기록을 보고 싶으면 몰라도 꼭 실행시킬 필요는 없다.
x1 = np.arange(0,6,0.05)
x2 = np.arange(0,4,0.05)
X1, X2 = np.meshgrid(x1, x2)
F = f([X1,X2])
#levels = np.arange(-6, 1)
CS = plt.contour(X1, X2, F) #, levels)  # 그림 9.13
plt.clabel(CS, fontsize=10);  
plt.plot(xo[0],xo[1],'o', ps[:,0],ps[:,1],':')
plt.grid()
plt.show()
