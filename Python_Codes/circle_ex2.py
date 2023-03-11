class Circle:
    PI = 3.1415 # Class Variable
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
    
    # By using the Circle class variable as PI, we can calculate the area.
    def area(self):
        return Circle.PI * self.radius ** 2
c1 = Circle("C1", 4)
print("area of c1:", c1.area())
c2 = Circle("C2", 6)
print("area of c1:", c2.area())
c3 = Circle("C3", 5)
print("area of c1:", c3.area())