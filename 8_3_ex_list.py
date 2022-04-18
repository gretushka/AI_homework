class NotNumberEx(Exception):
    def __init__(self, str):
        self.txt = f'Numbers only, {str} is not number!'

    def __str__(self):
        return self.txt


num_list = []
print('Input numbers for list by Enter, "q" - for quit\n')
num_simbols = [str(i) for i in range(10)]
while True:
    try:
        value = input()
        if value == 'q':
            break
        if value[0] not in num_simbols + ['-'] or set(value[1:]) - set(num_simbols + ['.']) or value.count('.') > 1:
            raise NotNumberEx(value)
        else:
            num_list.append(float(value))
    except NotNumberEx as err:
        print(err)

print(f"Your list: {num_list}")
