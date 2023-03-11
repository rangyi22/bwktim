ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x < 20:
        return False
    else:
        return True

adults = filter(myFunc, ages)

for x in adults:
    print(x)