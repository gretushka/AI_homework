from textblob import TextBlob

with open("text_4.txt", 'r', encoding='utf-8') as en_f, open("text_5.txt", 'w', encoding='utf-8') as ru_f:
    for line in en_f:
        words = line.split()
        words[0] = str(TextBlob(words[0]).translate(to='ru'))
        ru_f.write(f"{' '.join(words)}\n")
