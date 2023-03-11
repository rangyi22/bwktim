#class_Vector2D.py
import math
class Vector2D:  
  def __init__(self, x, y):  
     self.x = x  
     self.y = y 
  def __add__(self, other):  # Equivalent of + operator
     return Vector2D(self.x + other.x, self.y + other.y)
  def __sub__(self, other):  # Equivalent of - operator
     return Vector2D(self.x - other.x, self.y - other.y)
  def mag(self):  # Magnitude
     return math.sqrt(self.x**2 + self.y**2)
  def __repr__(self): # 이 class object가 호출/실행될 때 print된다.
     return f"({str(self.x)}, {str(self.y)})"
