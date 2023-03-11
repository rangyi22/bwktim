#  Returns a matching string where every even letter is uppercase, and every odd letter is lowercase. 
def myfunc(str):
    out = []
    for i in range(len(str)):
        if i % 2 == 0:
            out.append(str[i].lower())
        else:
            out.append(str[i].upper())

    return ''.join(out)
a = myfunc('Anthropomorphism')
print(a)