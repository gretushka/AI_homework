season_dict = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter',
}
season_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn',
               'autumn', 'winter']

month_number = 0

while month_number < 1 or month_number > 12:
    month_number = int(input("Input number of month (1-12) "))

print(f"Dictionary says that it's a {season_dict[month_number]}")
print(f"And list says that it's a {season_list[month_number-1]}" )
