class Cat:
    # Intialize the method
    #def __init__(self, name="Navi", color="white"):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    # Method that prints the information of Cat class
    def info(self):
        print('The name of cat is ==>', self.name, 'and its color is ==>', self.color)

cat1 = Cat("Nero", "black")
cat2 = Cat("Mimi", "brown")

cat1.info()
cat2.info()