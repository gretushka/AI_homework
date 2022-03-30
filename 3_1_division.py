def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Divide by zero is not good idea')
    except TypeError:
        print('Your numbers are not numbers =)')


a = 3
b = 0.44
div_list = [('a', 5), (3, 0), (3.2222, -12), (a, b), (False, True), (True, False)]
i = 1
for item in div_list:
    print(f'{i})')
    i += 1
    if division(item[0], item[1]) is not None:
        print(division(item[0], item[1]))
