def raiseError(inNum):
    arr = [1, 2, 3]
    if inNum in arr:
        print("This input is okay.")
    else:
        # Exception object created.
        raise ValueError("Please check the input value you entered.")

while(True):
    try:
        inNum = int(input("Choose one number from 1 or 2 or 3. ==> "))
        raiseError(inNum)
        break
    except Exception as e:
        print('error', e)