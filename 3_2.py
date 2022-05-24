class AmericanDate:
    def __init__(self, year, month, day):
        lenm = len(str(month))
        lend = len(str(day))
        self.year = year
        if lenm == 1:
            month = '0' + str(month)
        self.month = month
        if lend == 1:
            day = '0' + str(day)
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    def format(self):
        return (str(self.month) + '.' + str(self.day) + '.' + str(self.year))

class EuropeanDate:
    def __init__(self, year, month, day):
        lenm = len(str(month))
        lend = len(str(day))
        self.year = year
        if lenm == 1:
            month = '0' + str(month)
        self.month = month
        if lend == 1:
            day = '0' + str(day)
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def set_year(self, new_year):
        self.year = new_year

    def set_month(self, new_month):
        self.month = new_month

    def set_day(self, new_day):
        self.day = new_day

    def format(self):
        return (str(self.day) + '.' + str(self.month) + '.' + str(self.year))

american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())
