list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list1:
    print("list1 and list1 are the same instance.")

if list1 == list2:
    print("Data value of list1 and list2 is the same.")
    if list1 is list2:
        print("list1 and list1 are the same instance.")
    else:
        print("But the list1 and list2 are the different instances.")
