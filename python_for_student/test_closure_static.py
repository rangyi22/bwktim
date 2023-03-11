#test_closure_static.py
def closure_summer():
   S = 0
   def summer(val):
      nonlocal S
      S = S + val
      return S
   return summer
