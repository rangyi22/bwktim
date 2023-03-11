try:
    b = 2 / 0 # ZeroDivisionError
    a = 1 + "some"  # TypeError
except:
    print('Error')