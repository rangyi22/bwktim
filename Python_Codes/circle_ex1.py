class Circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.PI = 3.14

    def area(self):
        return self.PI * self.radius ** 2

c1 = Circle("C1", 4)
print("Area of c1 is: ", c1.area())
c2 = Circle("C2", 6)
print("Area of c2 is: ", c2.area())
c3 = Circle("C3", 5)
#c3.PI = 3.1415
print("Area of c3 is: ", c3.area())