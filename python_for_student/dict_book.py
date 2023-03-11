#dict_book.py
def change_price(book, 가격):
   book['price'] = 가격
   return book
def change_stock(book, 수량):
   book['stock'] += 수량
   return book
