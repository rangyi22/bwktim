def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error occurred by dividing by zero.")
    else:
        print("Results :", result)
    finally:
        print("Division done!")

print('divide(100, 2) function called :')
divide(100, 2)
print('divide(100, 0) function called :')
divide(100, 0)