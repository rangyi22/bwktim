#test_class_error.py
class UserException(Exception):
   def __init__(self, name):
      self.name = name
   def __repr__(self):
      return self.name + " exception"
try:
   raise UserException('Yang') # A user-defined exception
except UserException as er: # er is an instance of UserException class
   print(er,'has been handled in the except clause.')
raise UserException('My Exception')
