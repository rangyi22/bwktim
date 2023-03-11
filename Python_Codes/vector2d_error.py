class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __ster__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
print('v1 =', v1, ', v2 =', v2)

v3 = v1 + v2 # + operator of Vector2D is not defined.
print('v1 + v2 =', v3) 