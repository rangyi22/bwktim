#test_global_nonlocal.py
def outer():
   x = 4; y = 5
   def inner():
      global x 
      nonlocal y
      x = 1; y = 2; z = 3
      print("x (inner): ", x)
      print("y (inner): ", y)
      print("z (inner): ", z)
   inner()
   print("x (outer): ", x)
   print("y (outer): ", y)
   try: print("z (inner): ", z)
   except: print(" z doesn't exist in outer().")
outer()
print('x =', x)
try: print("y (inner): ", y)
except: print(" y doesn't exist in main().")
