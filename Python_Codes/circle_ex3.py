class Circle:
    PI = 3.14

    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
    
    # Circle class 변수 PI를 이용하여 면적을 구함
    def area(self):
        return Circle.PI * self.radius ** 2

c1 = Circle("C1", 4)
print("Properties of C1 is: ", c1.__dict__)
print("The variable value of name of c1: ", c1.__dict__['name'])
print("The variable value of radius c1: ", c1.__dict__['radius'])