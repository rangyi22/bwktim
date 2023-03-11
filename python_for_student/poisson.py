#poisson.py
import math
lam = 2
term = math.exp(-lam)
S = 0
for k in range(100):
   S = S + term    # 식 (E2.3.2)
   term = term*lam/(k+1) # 식 (E2.3.3)
print(S)
