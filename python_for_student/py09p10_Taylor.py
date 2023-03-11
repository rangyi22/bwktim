#py09p10_Taylor.py
import numpy as np
from scipy.interpolate import approximate_taylor_polynomial
import matplotlib.pyplot as plt

f = lambda x: np.exp(-x)
x0 = 1 # Center of the Taylor series expansion
x = np.linspace(x0-3, x0+3, 400) # Range on the x-axis
plt.plot(x, f(x), label="f(x)=exp(-x) curve")
plt.plot(x0,f(x0),'o', label="Center of Taylor series expansion")
h = 0.0001 # 수치적 미분계수를 구하기 위한 step-size
for deg in [1,2,3]: 
   p_taylor = approximate_taylor_polynomial \
                (f, x0, degree=deg, scale=h)
   print(p_taylor)
   plt.plot(x, p_taylor(x-x0), label=f"degree={deg}")
plt.legend()
plt.show()
