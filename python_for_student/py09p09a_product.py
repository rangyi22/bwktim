#py09p09a_product.py
import numpy as np

p1 = np.array([2, 1, 0])
p2 = np.array([0, 1, 1])
p3 = np.array([1, 3, 2])
n = np.?????(p1-p2, p3-p1) # Normal vector
print('Normal vector n =', n)
dot_product1 = np.???(p2-p1, n)  # zero?
print('dot(p2-p1, n) =', dot_product1)
dot_product2 = np.???(p3-p1, n)  # zero?
print('dot(p3-p1, n) =', dot_product2)
