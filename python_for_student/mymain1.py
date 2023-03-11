#mymain1.py
from mypkg.book.class_Book1 import * # class_Book1 module 파일
book0 = Book1(['Math1', 95, 14]) # Book class instance 생성
book0.change_price(97);  book0.change_stock(9)                        
book0.showinfo()
