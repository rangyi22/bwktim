#class_Customer.py
class Customer:
  def __init__(self, 이름, 잔고):
     self.name = 이름
     self.balance = 잔고
  def deposit(self, amount):
     self.balance += amount
     return self.balance
  def withdraw(self, amount):
     done = False
     if amount > self.balance:
       print("You can't withdraw {amount} > {self.balance}!")
     else:
       self.balance -= amount
       done = True
     return done
