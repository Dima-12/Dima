class Date:
  def __init__(self, month, day):
    self.month = month
    self.day = day
  
  def __sub__(self, other):
     dt_1 = d.date(2022, self.month, self.day)
     dt_2 = d.date(2022, other.month, other.day)
       if dt_1 == dt_2:
          return 0
       return  ((str(dt_1 - dt_2)).split())[0]
jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)
print()
