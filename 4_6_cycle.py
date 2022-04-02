from itertools import count, cycle, islice


def my_iterator(start):
    if int(start) != start:
        print('Number must be integer')
    for num in count(start):
        if num > abs(start * 2):
            break
        yield num


def my_cycle(object):
    с = 0
    stop = len(object) * 5
    for el in cycle(object):
        if с == stop:
            break
        с += 1
        yield el


print(list(my_iterator(-15)))
print(list(my_cycle('string')))
print(list(islice(my_cycle('string'), 14)))
