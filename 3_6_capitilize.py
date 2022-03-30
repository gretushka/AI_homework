def int_func(word):
    if max(word) <= 'z' and min(word) >= 'a':
        return word.capitalize()
    return ''


word_list = input('Enter text in English ').split()
new_text = ''
for word in word_list:
    new_word = int_func(word)
    if new_word:
        new_text += new_word + ' '
new_text = new_text[:-1]
print(new_text)
