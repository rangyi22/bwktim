def shortCircuitTest():
    print("shortCircuitTest() is run!")
    return True

if True and shortCircuitTest():
    print("Executed when True!")
else:
    print("Executed when False!")