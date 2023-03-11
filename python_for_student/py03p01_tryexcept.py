#py03p01_tryexcept.py
L = [(1, 2), (3, 0), ('x', 4)] 
n = 0
while n <= len(L):
   try: 
        x = L[n][0];  y = L[n][1]
        z = x/y        
   except Exception as e:
          print(f'{type(e)}: {e}')
   else:  print(f'{x}/{y} = {z}')
   finally:  n = n + 1
