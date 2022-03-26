text = input('Input text \n')
word_list = text.split()
for i, word in enumerate(word_list):
    print(f'{i+1}) {word[:10]}')