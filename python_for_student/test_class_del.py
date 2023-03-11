#test_class_del.py
class Fwrite:
  def __init__(self, filename): # Class (instance) initializer 
     self.fname = filename
     self.fw = open(filename, "w") # Open file
     print('__init__ method has been executed.')
  def write(self, data):
     self.fw.write(data) # Write data
  def __del__(self):  # Class (instance) destructor(소멸자)
     self.fw.close() # Close file
     print('__del__ method has been executed.')
