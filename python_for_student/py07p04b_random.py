#py07p04b_random.py
import random
from math import factorial
event_freq = {'모': 0, '도': 0, '개': 0, '걸': 0, '윷': 0}
events = list(event_freq.keys())
(PH, PT) = (0.51, 0.49)
for i in range(1000000):
   outcome = random.       (['H','T'], weights=[     ], k= )
   event = events[outcome.count('H')]
   event_freq[event] += 1
print(event_freq)
def comb(n, k):
   return factorial(n)/factorial(k)/factorial(n-k)
P = []
for n in range(5):
   P.append(comb(4,n)*PH**n*PT**(4-n)) # 식 (P7.4.1)
print(P)
