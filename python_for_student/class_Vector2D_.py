#class_Vector2D_.py
from class_Vector2D import * # 6.1.4절 Vector2D class를 정의한 파일
class Vector2D_(Vector2D): # Vector2D class를 parent로 
  def __eq__(self, other):  # == (equality) operator
     return (self.x, self.y) == (other.x, other.y)
  def __gt__(self, other):  # > (greater than) operator
     return Vector2D.mag(self) > Vector2D.mag(other)
  def __ge__(self, other): # >= (greater than or equal to) operator
     return Vector2D.mag(self) >= Vector2D.mag(other)
  def __lt__(self, other): # < (less than) operator
     return Vector2D.mag(self) < Vector2D.mag(other)
  def __le__(self, other): # <= (less than or equal to) operator
     return Vector2D.mag(self) <= Vector2D.mag(other)
if __name__ == "__main__":
  v1 = Vector2D_(1,2); v2 = Vector2D_(3,4)
  v3 = Vector2D_(2,2); v0 = Vector2D_(0,0)
  print(v1 - v2 + v3 == v0, v1 >= v2, v1 < v3, v1)
