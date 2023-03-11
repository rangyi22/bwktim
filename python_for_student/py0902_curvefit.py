#py0902_curvefit.py
# Curve fitting
import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt

np.random.seed(0) # 동일한 난수 수열을 발생시키기 위해 seed를 지정한다.
N = 101 # data point의 개수
xdata = np.linspace(-5, 5, num=N)
ydata = 5*np.sin(1.5*xdata) + np.random.normal(size=N)
g = lambda x, a, b: a*np.sin(b*x) # fitting model function
po, po_cov = opt.curve_fit(g, xdata, ydata)
ao, bo = po  # a와 b의 추정치
print(f'ao = {ao:9.4f}, bo = {bo:9.4f}')
plt.scatter(xdata, ydata, s=6, label='Data')
plt.plot(xdata, g(xdata, ao, bo), label='Fitted function')
plt.legend(loc='best')
plt.show()
