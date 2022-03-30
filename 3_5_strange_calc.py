def my_sum(values):
    sum = 0
    i = 0
    for value in values:
        if value != 'q':
            try:
                sum += float(value)
                i += 1
            except:
                pass
        else:
            i += 1
    if i < len(values):
        print('Your input is incorrect, we can summarize numbers only!')
    return sum


total_sum = 0
while True:
    values = input('Enter numbers in row, "q" - for quit ').lower().split()
    if values:
        last_sum = my_sum(values)
        total_sum += last_sum
        print(f'Last sum = {last_sum}, total sum = {total_sum}')
        if 'q' in values:
            break
