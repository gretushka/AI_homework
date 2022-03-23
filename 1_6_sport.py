import math

a = 1
b = 0
while b < a:
    a = float(input('Input a '))
    b = float(input('Input b '))
n = 1 + math.ceil(math.log(b / a, 1.1))
print(f"Number of goal achievement day is {n}")
