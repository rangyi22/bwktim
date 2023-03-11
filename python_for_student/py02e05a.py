#py02e05a.py 
primes = []
for n in range(2, 10):
   flag = 0
   for x in range(2, n):
      if n % x == 0:
        flag = 1  
        break
   if flag==0:
     primes.append(n)
print('prime numbers: ', primes)
