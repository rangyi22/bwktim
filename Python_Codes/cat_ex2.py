class Cat:
    def info(self): # info() method
        self.name = "Navi"
        self.color = "Black"
        print("The name of a cat is", self.name, "Her color is", self.color)

cat = Cat() # instance created
cat.info() # method of the instance called