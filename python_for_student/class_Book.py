#class_Book.py
class Book:
  def __init__(self, 제목, 단가, 재고):
     self.title = 제목 # title
     self.price = 단가 # price
     self.stock = 재고 # stock
  def change_price(self, 가격):
     self.price = 가격
  def change_stock(self, 수량):
     self.stock += 수량
  def show_stock(self):
     print(self.stock)
