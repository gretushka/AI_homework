def my_func(a, b, c):
    try:
        return a + b + c - min(a, b, c)
    except TypeError:
        print('Not numbers!')


arg_list = [
    (1, 2, 3),
    ('1', '2', '3'),
    (True, False, None)
]
for item in arg_list:
    if my_func(item[0], item[1], item[2]):
        print(my_func(item[0], item[1], item[2]))
