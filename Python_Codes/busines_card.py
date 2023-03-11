from tkinter import W

class BusinessCard:

	cardCount = 0	# Class 변수는 "class명.속성"으로 접근
	# cardCount는 BusinessCard Class의 속성
	# __init__() method는 생성자 또는 class의 초기화 method라고 한다.
	def __init__(self, name, email, addr):
		self.name = name
		self.email = email
		self.addr = addr
		BusinessCard.cardCount += 1
	
	def displayCard(self): # instance 변수는 self를 이용하여 접근
		print("--------------------------------------")
		print("Name: %s" % self.name)
		print("E-mail: %s" % self.email)
		print("Office Address: %s" % self.addr)
		print("--------------------------------------")

	def displayCount(self):
		print("The number of card is %d" % BusinessCard.cardCount)

# 객체화 또는 Instance화 하는 Code
business_card1 = BusinessCard("WK Bae", "wk.bae2020@gmail.com", "Suwon")
business_card1.displayCount()
business_card2 = BusinessCard("Bae, Rangyi", "rangyi.bae@gmail.com", "Gwanggyo")

business_card1.displayCard()
business_card2.displayCard()

business_card3 = BusinessCard("Lee, Youngeun", "young.lee@gmail.com", "Cheonan")

business_card2.displayCount()