def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


for i, el in enumerate(fact(12)):
    print(f"{i + 1}! = {el}")
