# import math (Case1) import <module>

# r1 = math.ceil(1.5)
# r2 = math.floor(1.2)

# print(r1, r2)

# from math import ceil, floor (Case2) from module import function

# r1 = ceil(1.5)
# r2 = floor(1.2)

# print(r1, r2)

# from math import  (Case3) from module import *

# print(ceil(1.5))
# print(floor(1.5))
# print(factorial(8))

# import math as mm  (Case4) from module as alias
# print(mm.ceil(1.5))
# print(mm.floor(1.5))
# print(mm.factorial(8))

from math import ceil as c, floor as f # (Case5) from moudle import function as alias
print(c(1.5))
print(f(1.5))