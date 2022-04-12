import html


class Cell:
    number = 0

    def __init__(self, n=0):
        try:
            if int(n) == n and n >= 0:
                self.number = n
        except ValueError:
            pass

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        number = self.number - other.number
        return Cell(number) if number > 0 else Cell(0)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def __str__(self):
        return str(self.number)

    def make_order(self, n=5):
        try:
            if int(n) == n:
                hole_row_number = self.number // n
                last_row = self.number % n
                print(html.unescape(('&#128579;' + ' ') * n + '\n') * hole_row_number + ('\U0001F600' + ' ') * last_row)
            else:
                print(f"Can't make order with {n} for a number")
        except ValueError:
            print(f"Can't make order with {n} for a number")


print(Cell(0) + Cell(5))
print(Cell(-1) - Cell(2))
print(Cell(2) - Cell(0))
Cell(10).make_order(3)
(Cell(5) * Cell(6)).make_order(11)
print(Cell(5) / Cell(2))
Cell(10).make_order(2.2)
