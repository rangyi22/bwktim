class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{}(Age {} years old)".format(self.name, self.age)

person = Human("Suzy", 23)
print(person)