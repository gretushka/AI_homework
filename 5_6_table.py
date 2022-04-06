with open("text_6.txt", 'r', encoding='utf-8') as table_f:
    table = table_f.readlines()
    hours_dict = {disc.split()[0]:
                      sum([int(num.split('(')[0]) if num != '-' else 0 for num in disc.split()[1:]]) for disc in table}
    print(hours_dict)
