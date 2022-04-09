class Worker:
    name = 'name'
    surname = 'surname'
    position = 'position'
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position = Position('Nastya', 'Art', 'designer', 20000, 5000)
print(
    f"{position.name} {position.surname} is a {position.position}, and earns {position._income['wage'] + position._income['bonus']} tugriks")
print('Some of this info can be obtained by methods')
print(f"{position.get_full_name()} is a {position.position}, and earns {position.get_total_income()} tugriks")
print('And this road is better')
