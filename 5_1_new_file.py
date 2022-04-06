with open("text.txt", 'w', encoding='utf-8') as my_f:
    content = 'some_text'
    print('Введите текст, пустая строка  - конец ввода текста')
    while content:
        content = input()
        my_f.write(f'{content}\n')
