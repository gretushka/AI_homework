from random import randint, random

with open("text_2.txt", 'w+', encoding='utf-8') as num_f:
    for _ in range(randint(100, 200)):
        num_f.write(f"{random() * 100 - 50:.2f} ")
    num_f.seek(0)
    num_list = num_f.read().split()
    sum = 0
    for num in num_list:
        sum += float(num)
    print(sum)
