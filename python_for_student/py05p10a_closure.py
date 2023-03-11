#py05p10a_closure.py
def outer(n):
   result = 0
   def inner(x):
      nonlocal result
      while x > 0:
         result += x ** n
         x -= 1
      return result
   return inner
f3 = outer(3)
print(f3(2))
f2 = outer(2)
print(f2(3))
