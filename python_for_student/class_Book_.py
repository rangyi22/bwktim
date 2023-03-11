#class_Book_.py
class Book_:
  def __init__(self, 제목, 단가, 재고):
     self.title = 제목 
     self.price = 단가 
     self.__stock = 재고 # stock은 private로 해서 감춘다.
  def change_price(self, 가격):
     self.price = 가격
  def change_stock(self, 수량):
     self.__stock += 수량  # stock은 감춘다.
  def show_stock(self):
     print(self.__stock)  # stock을 print한다.
