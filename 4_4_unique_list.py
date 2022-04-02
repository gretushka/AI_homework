list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_list = [n for n in list if list.count(n) == 1]
print(unique_list)
