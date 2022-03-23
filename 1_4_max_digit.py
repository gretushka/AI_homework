num = int(input('Input your number n '))
max_num = 0
while num > 0:
    if max_num < num % 10:
        max_num = num % 10
    num = num // 10
print(
    f"Max figure is {max_num}")
