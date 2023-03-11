try:
    #b = 2 /0    # ZeroDivisionError
    a = 1 + "some"  #TypeError
except Exception as e:
    print('error', e)