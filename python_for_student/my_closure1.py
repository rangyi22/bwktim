#my_closure1.py 
def my_closure1(func):
   def f(x):
       return func(list(map(abs, x)))
   return f
   #return lambda x : func(list(map(abs, x)))
