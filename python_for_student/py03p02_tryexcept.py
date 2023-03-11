#py03p02_tryexcept.py
import numpy as np
def my_sqrt(x):
   try: y = np.sqrt(x)     
   except Exception as e:
      print(f'{type(e)}: x must be a number!')
      y = '????'
   else:
      if x < 0:
        print('x must be nonnegative!')       
   finally: return y 
