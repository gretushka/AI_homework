def my_func(x, y):
    if y >= 0 or int(y) != y:
        print('Y must be integer number <0!')
    else:
        res = 1
        i = 0
        while i < abs(y):
            res *= 1 / x
            i += 1
        return res


arg_list = [
    (10, -1),
    (10, 1),
    (7, -2),
    (0.5, -0.5),
    (-0.5, -4)
]
for item in arg_list:
    if my_func(item[0], item[1]):
        print(my_func(item[0], item[1]))
