#py07p05_random.py
import random
import matplotlib.pyplot as plt
N = 100000 
(a, b, c) = (-1, 2, 1)  
# Uniform random numbers
xu = []
for n in range(N):
   xu.append(random.        (a, b))
# Triangular random numbers
xt = []
for n in range(N):
   xt.append(random.          (a, b, c))
Nb = 20  # histogram의 구간수(Number of bins)
plt.subplot(1,2,1); plt.hist(xu,     =  )
plt.subplot(1,2,2); plt.    (xt, bins=  )
plt.show()
