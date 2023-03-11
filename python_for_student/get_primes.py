#get_primes.py
N = 7
primes = []
for n in range(2,N):    
   count = 0
   for i in range(2, n//2 + 1):
      if n % i == 0:
        count = count + 1
        break
   if count < 1:  primes.append(n)
