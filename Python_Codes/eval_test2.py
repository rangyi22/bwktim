def shortCircuitTest():
    print("shortCircuitTest() is run!")
    return True

if False and shortCircuitTest():
    print("Executed when True!")
else:
    print("Executed when False!")