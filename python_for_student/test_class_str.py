#test_class_str.py
class Student:
   def __init__(self, name, age, school=None):
      self.name = name
      self.age = age
      self.school = school
   def __str__(self): # allowed to return only a string
      dic = self.__dict__
      info = ', '.join([f'{key}={dic.get(key)}' for key in dic])
      return 'Student(' + info + ')'
   def __repr__(self): 
      return str(self.__dict__)
