#py05p09_callback.py
my_sum = lambda x1, x2: x1 + x2
my_mul = lambda x1, x2: x1 * x2
def my_calc(x1, x2, callback): 
   return callback(x1, x2)
