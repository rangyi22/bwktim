lst = [3, 2, 4, 1, 5, 6, 7]
inNum = int(input("Enter the number you are finding : "))

i = 0
while i < len(lst):
    if lst[i] == inNum:
        print("%d번째 입니다."%(i+1))
        break
    print("Searching for...")
    i += 1