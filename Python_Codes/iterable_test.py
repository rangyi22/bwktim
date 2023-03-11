# Check whether the list is the iterable object
try:
    l = [1, 2, 3, 4]
    iterator = iter(l)
    #print(iterator)
except TypeError:
    print('list is not the iterable object.')
else:
    print('list is the iterable object.')

# Check whether the tuple is the iterable object
try:
    t = ("WK Bae", 45, 174.0)
    iterator = iter(t)
    #print(iterator)
except TypeError:
    print('tuple is not the iterable object.')
else:
    print('tuple is the iterable object.')

# Check whether the integer is the iterable object
try:
    n = 100
    iterator = iter(n)
    #print(iterator)
except TypeError:
    print('n is not the iterable object.')
else:
    print('n is the iterable object.')