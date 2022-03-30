my_list = [5, False, None, 0.7, 2 - 3j, 'str', [0, 1, 1], ('s', 5, 0.1, None, False), {1, 2, 3},
           {'key1': 'value1', 'key2': 'value2'}, b'str', ZeroDivisionError]
for item in my_list:
    print(type(item))
