# swap using temporary variable 'temp'
a = 100
b = 200
print('Before swapping : a=', a, 'b=', b)
temp = a
a = b
b = temp
print('After swapping : a=', a, 'b=', b)

# simple swap using tuple
a = 100
b = 200
print('Before swapping : a=', a, 'b=', b)
a, b = b, a
print('Swap results using tuple : a=', a, 'b=', b)