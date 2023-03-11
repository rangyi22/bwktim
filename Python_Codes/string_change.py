import re

def multiple10(m):
    #print(m.group())
    n = int(m.group())
    return str(n * 10)

print(re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8'))