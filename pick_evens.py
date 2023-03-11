def myfunc(*args):
    empty_list = []     # create an empty list
    for i in args:
        if i % 2==0:
            empty_list.append(i)    # append i not args into the empty_list
    return empty_list     # return the empty_list after the for loop
 
a = myfunc(2,3,4,5,6)
print(a)