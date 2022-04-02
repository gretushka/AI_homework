my_list = [1, 3, 12, 5, 4, 7, 6, 9, 10, 2, 12]
new_list = [n for i, n in enumerate(my_list) if i and n > my_list[i - 1]]
print(new_list)
