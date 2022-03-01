class Time:

  def __init__(self, minute, sec):
    self.minute = minute +sec // 60
    self.sec = sec % 60
    
  def get_minute(self):
    return self.minute
    
  def get_sec(self):
    return self.sec
   
  def set_minute(self, new_minute):
    self.minute
    
  def __str__(self):
    minute = str(self.get_minute().rjust(2, '0'))
    sec = str(self.get_sec().rjust(2, '0'))
    
  def __str__(self):
    return f'{self.get_minute}:{self.get_sec}'
    
  def __add__(self, other):
    time_1 = self.get_minute() * 60 + self.get_sec()
    time_2 = other.get_minute() * 60 + other.get_sec()
    return Time(new_minute, new_sec)
  
  def __iadd__(self, other):
    minute = self.get_minute() + other.get_minute()
    sec = self.get_sec() + other.get_sec()
    minute += sec //60
    sec %= 60
    self.set_minute(minute)
    self.set_sec(sec)
    return self
    
  def __repr__(self):
    return 'Time({},{})'\
      .format(self.get_minute(),self.get_sec())
a=Time(5, 15)
b=Time(4, 89)
