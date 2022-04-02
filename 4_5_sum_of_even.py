from functools import reduce


def prod(a, b):
    return a * b


even_list = [n for n in range(100, 1001) if not n % 2]

print(reduce(prod, even_list))
