#class_Person.py
class Person:  
  def __init__(self, name, 취미=None, 전공=None, 계급=None):
    self.이름 = name; self.취미 = 취미
    self.major = 전공; self.rank = 계급
  def greeting(self): 
    print(f'{self.hi}, 내 이름은 {self.이름}, 취미는 {self.취미}야.')
  hi = '안녕'
class Programmer(Person): 
  def show_major(self): 
     print(f'내 전공은 {self.major}이지.')
class Soldier(Person): 
  def show_rank(self): 
     print(f'내 계급은 {self.rank}이지.')
if __name__ == "__main__":
  홍길동 = Programmer('홍길동','낚시', 전공='Python')
  홍길동.greeting();  홍길동.show_major()
