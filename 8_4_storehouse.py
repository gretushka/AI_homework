from abc import ABC, abstractmethod

TYPES = ['ink-jet', 'laser']
FORMATS = ['A0', 'A1', 'A2', 'A3', 'A4']


class NotPositiveNum(Exception):
    def __init__(self):
        self.txt = 'Need positive integer number'

    def __str__(self):
        return self.txt


class NotInValues(Exception):
    def __init__(self, value, values=[]):
        self.txt = f'{value} - unexpected value, need one of {values}'

    def __str__(self):
        return self.txt


class OfficeEquip(ABC):
    size = []
    name = ''

    def __init__(self, size=[], name=''):
        self.size = size
        self.name = name

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @staticmethod
    def change_cart(resource, can_print):
        try:
            resource = int(resource)
            if resource > 0:
                print('Cartridge is successfully exchanged')
                return resource
            else:
                print('The cartridge is defective')
                return can_print
        except ValueError:
            print('Resource must be a number!')
            return can_print


class Printer(OfficeEquip):
    type = 'ink-jet'
    can_print = 1000

    def __init__(self, name='Canon', size=[100, 100, 100], type='ink-jet', can_print=1000):
        try:
            if type not in TYPES:
                raise NotInValues(type, TYPES)
            self.type = type
            self.can_print = can_print
            super().__init__(size, name)
        except NotInValues as err:
            print(err)

    def __str__(self):
        return f"{self.name} - is {self.type} printer " \
               f"{', with resource - ' + str(self.can_print) + ' pages' if self.type == 'ink-jet' else ''}"

    def run(self, pg=1):
        try:
            if not isinstance(pg, int) or pg < 1:
                raise NotPositiveNum()
            else:
                if self.type == 'ink-jet':
                    if self.can_print <= pg:
                        print(f'Print {self.can_print} pages, now cartridge is empty, please change it')
                        self.can_print = 0
                    else:
                        self.can_print -= pg
                        print(f'Print {pg} pages')
                else:
                    print(f'Print {pg} pages')
        except NotPositiveNum as err:
            print(err)

    def change_cart(self, resource=1000):
        if self.type == 'ink-jet':
            self.can_print = super().change_cart(resource, self.can_print)
        else:
            print("It's a laser printer =)")


class Scaner(OfficeEquip):
    object_size = 'A4'

    def __init__(self, name='Canon', size=[100, 100, 100], object_size='A4'):
        try:
            if object_size not in FORMATS:
                raise NotInValues(object_size, FORMATS)
            self.size = object_size
            super().__init__(size, name)
        except NotInValues as err:
            print(err)

    def __str__(self):
        return f"{self.name} - is scaner for objects of size not greater than {self.object_size} "

    def run(self, obj_s='A4'):
        try:
            if obj_s not in FORMATS:
                raise NotInValues(obj_s, FORMATS)
            else:
                if FORMATS.index(obj_s) >= FORMATS.index(self.object_size):
                    print(f'Successfully scanned')
                else:
                    print(f'Scanning is failed, size of the object too big!')
        except NotInValues as err:
            print(err)


class Copier(OfficeEquip):
    name = 'Canon'
    is_color = False
    can_print = 1000

    def __init__(self, name='Canon', size=[100, 100, 100], is_color=False, can_print=1000):
        self.is_color = is_color
        self.can_print = can_print
        super().__init__(size, name)

    def __str__(self):
        return f"{self.name} - is {'color' if self.is_color else 'black and white'} copier" \
               f", with resource - {self.can_print} pages"

    def run(self):
        if not self.can_print:
            print(f'Cartridge is empty, please change it')
        else:
            self.can_print -= 1
            print(f'Successfully copied')

    def change_cart(self, resource=1000):
        self.can_print = super().change_cart(resource, self.can_print)


class Stock:
    eq_list = []
    capacity = 100

    def __init__(self, capacity=100, eq_list=[]):
        try:
            if capacity < 0:
                raise NotPositiveNum()
            # else:
            self.capacity = capacity
            self.eq_list = []
            i = 0
            for one in eq_list:
                if isinstance(one, OfficeEquip):
                    self.eq_list.append(one)
                    i += 1
                    if i == capacity:
                        print('Stock is full')
                        break
            print(f'Stock has {self.capacity - i} empty cells')
        except NotPositiveNum as err:
            print(err)

    def __str__(self):
        return f"Stock of office equipment with capacity {self.capacity}. Hold {len(self.eq_list)} units of equipment: " \
               f"{str([one.name for one in self.eq_list])}"

    def acceptance(self, eq_list):
        start_count = len(self.eq_list)
        i = 0
        if start_count == self.capacity:
            print('Stock is full')
        else:
            for one in eq_list:
                if isinstance(one, OfficeEquip):
                    self.eq_list.append(one)
                    i += 1
                    if i + start_count == self.capacity:
                        if one != eq_list.last():
                            print("Stock not rubber, we can acceptance only {i} units")
                        else:
                            print('Stock is full')
                        break
            print(f'Stock has {self.capacity - i - start_count} empty cells')

    def issue(self, one):
        if one in self.eq_list:
            self.eq_list.remove(one)
            print(f'{one.name} successfully issued from stock')
        else:
            print(f'There is no such unit {one} in the stock')


pr = Printer()
sc = Scaner()
cop = Copier()
print(pr, sc, cop)
stock = Stock(15, [pr, sc, cop])
print(stock)
stock1 = Stock(-2)
pr.run(0)
pr.run()
pr.run(10)
pr.run(1000)
pr.change_cart(0)
pr.change_cart(15)
pr.run(1000)
pr1 = Printer('HP', [1, 1, 1], 'str')
sc1 = Scaner('HP', [1, 1, 1], 'str')
sc.run()
sc.run('str')
sc.run('A3')
sc.object_size = 'A0'
sc.run('A0')
stock.acceptance([pr1, sc1])
stock.issue(pr)
stock.issue(pr)
