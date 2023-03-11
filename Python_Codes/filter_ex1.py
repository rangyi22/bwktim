def adult_func(n):
    if n >= 19:
        return True
    else:
        return False

ages = [34, 39, 20, 28, 18, 13, 10, 11, 54]

print("Adult List : ")
for a in filter(adult_func, ages):
    print(a)
        