#class_Person_inheritance1.py
from class_Person import *
class Student(Person):  
def __init__ (self, name, 취미=None, 학교=None):
   Person.__init__(name, 취미=None)
   self.school = 학교
  def show_school(self): 
     print(f'내 학교는 {self.school}지.')
