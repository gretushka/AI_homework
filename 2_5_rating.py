rating = [8, 6, 5, 5, 2]
while True:
    res = input('Input integer number for rating or stop to exit \n')
    if res == 'stop':
        break
    res = int(res)
    if res < 0:
        continue
    for i, num in enumerate(rating):
        if num < res:
            rating.insert(i, res)
            break
        elif i == len(rating) - 1:
            rating.append(res)
            break
    print(rating)
