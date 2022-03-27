items_number = int(input('Please input number of items in your list '))
user_list = []
for i in range(items_number):
    user_list.append(input(f'Input item of list with number {i} '))

print(f'Your list: {user_list}')

for i in range(int(items_number / 2)):
    exchange_var = user_list[2 * i]
    user_list[2 * i] = user_list[2 * i + 1]
    user_list[2 * i + 1] = exchange_var

print(f'List after exchange operation: {user_list}')
