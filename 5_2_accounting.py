with open("text_4.txt", 'r', encoding='utf-8') as my_f:
    i = 0
    for line in my_f:
        i += 1
        print(f"In {i} line there are {len(line.split())} words")
    print(f'There are {i} lines in document')
