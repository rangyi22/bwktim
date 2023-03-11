#py02e05b.py 
primes = []
for n in range(2, 10):
   for x in range(2, n):
      if n % x == 0:
        break
   else:
      primes.append(n)
print('prime numbers: ', primes)
