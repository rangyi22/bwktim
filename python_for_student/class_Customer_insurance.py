#class_Customer_insurance.py
from class_Customer import *
class Customer_insurance(Customer):
  def __init__(self, 이름, 잔고):
     Customer.__init__(self, 이름, 잔고) #parent class Customer
     self.insurance = [] # 의 __init__() method에 새 속성을 추가
  def buy_insurance(self, 보험, price):
     if price > self.balance:
       print("잔고부족으로 이 보험을 살 수 없습니다!")
     else:
       done = self.withdraw(price)
       if done: self.insurance.append(보험)
     return self.insurance, self.balance
