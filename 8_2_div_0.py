class DivByZeroEx(Exception):
    def __init__(self):
        self.txt = 'Division by zero is forbidden'

    def __str__(self):
        return self.txt


try:
    div = float(input('Input divisor for number 10 '))
    if not div:
        raise DivByZeroEx()
    else:
        print(f'10/{div} = {10 / div:.2f}')
except ValueError:
    print('It should be a number')
except DivByZeroEx as err:
    print(err)
