#py07p03a_random.py
import random
def random_seq(N):
   L = [] 
   for n in range(N):
      L.append(random.randrange(1,21,2))
   return L
