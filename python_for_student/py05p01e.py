#py05p01e.py
def sum_upto(k): # A recursive function
if k <= 0:  
  return 0
else:
  return k + sum_upto(k-1)
