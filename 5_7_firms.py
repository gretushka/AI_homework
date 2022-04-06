import json

with open("text_7.txt", 'r', encoding='utf-8') as firms_f:
    average = 0
    pos_num = 0
    firms_dict = {}
    for line in firms_f:
        firm = line.split()
        firms_dict[firm[0]] = float(firm[2]) - float(firm[3])
        if firms_dict[firm[0]] > 0:
            pos_num += 1
            average += firms_dict[firm[0]]
    firms_list = [firms_dict, {'average': average / pos_num}]
    with open('text_7.json', 'w', encoding='utf-8') as out_f:
        json.dump(firms_list, out_f, ensure_ascii=False, separators=(',\n', ': '))
