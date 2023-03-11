class Human:
    # Initialization
    # 생성자: instance 생성 시 자동으로 호출됨 (객체의 초기화)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name :", self.name, " Age :", self.age)

    def call(self):
        print(self.name, "is called.")

person = Human("Suzy", 23)
person.info()
person.call()
guy = Human("Tim", 27)
guy.info()
guy.call()