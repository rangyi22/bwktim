def a_calculateRectangleArea():
    print(5*7)
def b_calculateRectangleArea(x,y):
    print(x*y)
def c_calculateRectangleArea():
    return 5*7
def d_calculateRectangleArea(x,y):
    return (x*y)

a_calculateRectangleArea()
result = b_calculateRectangleArea(5,7)
print(result) # result = None
result = c_calculateRectangleArea()
print(result)
print(c_calculateRectangleArea())
result = d_calculateRectangleArea(5,3)
print(result)