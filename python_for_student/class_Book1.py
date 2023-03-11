#class_Book1.py
# "class_Book.py"에 정의된 Book class로부터의 inheritance(상속)
from class_Book import Book
#from class_Book import * # 이렇게는 해도 돠는데
#import class_Book # 이건 곤란하다
class Book1(Book): # 'Book' class의 child class
  def __init__(self, book): # parent의 __init__ method를 override
     self.title = book[0] # 제목
     self.price = book[1] # 가격
     self.stock = book[2] # 재고
     if len(book) > 3: # 출판사가 제2 입력인자로 들어오면 넣고, 아니면 말고
       self.publisher = book[3] 
  def showinfo(self):
     print(f'{self.title}: {self.price:6.1f}원 {self.stock:3d}권')
