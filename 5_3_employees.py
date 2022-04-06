with open("text_3.txt", 'r', encoding='utf-8') as my_f:
    i = 0
    sum = 0
    print(f"Employees with salary < 20000:\n")
    for line in my_f:
        i += 1
        name, salary = line.split()
        salary = float(salary)
        sum += salary
        if salary < 20000:
            print(f"{name}\n")
    print(f'Average salary is {sum / i:.2f}')
