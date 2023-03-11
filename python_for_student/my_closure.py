#my_closure.py
def my_closure(n):
   def mul_by(x): 
      return x * n
   return mul_by   #return lambda x : x * n
