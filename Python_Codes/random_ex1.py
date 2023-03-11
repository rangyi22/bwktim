import random

def rangeNum(s, e):
    if s > e:
        prevS = s
        s = e
        e  = prevS
    return int(random.random()* (e - s + 1)) + s

number1 = rangeNum(1, 5)
print(number1)
number2 = rangeNum(10, 15)
print(number2)
number3 = rangeNum(100, 200)
print(number3)
number4 = rangeNum(10, 5)
print(number4)