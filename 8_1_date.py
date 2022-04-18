class Date:
    day = 1
    month = 1
    year = 1

    def __init__(self, day=1, month=1, year=1):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year:04}"

    @classmethod
    def reform(cls, str):
        day, month, year = str.split('-')
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except ValueError:
            day, month, year = [0, 0, 0]
        if cls.valid(day, month, year):
            return cls(day, month, year)
        return cls()

    @staticmethod
    def valid(day, month, year):
        if day > 0 and day < 31 and 12 > month > 0 and year > 0 and year < 3000:
            return True
        return False


dt = Date.reform('01-10-2012')
print(dt)

print(Date.reform('30-40-50'))
print(Date.reform('str-str-50'))
print(Date.reform('1-2-50'))
