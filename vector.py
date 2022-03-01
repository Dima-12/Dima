class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
    
  def get_x(self):
    return self.x
  
  def get_y(self):
    return self.y
  
  
  def __str__(self):
    return 'Вектор (0, 0)->({},{})'.format(self.get_x(), self.get_y())
  
  def __repr__(self):
    
  def __add__(self, other):
    x = self.get_x() + other.get_x()
    y = self.get_y() + other.get_y()
    return Vector(x, y)
  
  def __sub__(self, other):
    x = self.get_x() - other.get_x()
    y = self.get_y() - other.get_y()
    return Vector(x, y)
  
  def __mul__(self, other):
    x = self.get_x() * other
    y = self.get_y() * other
    return Vector(x, y)
  
  
  def __rmul__(self, other):
    return self.__mul__(other)
  
x = Vector(4,5)
a = x * 5
print(a)
