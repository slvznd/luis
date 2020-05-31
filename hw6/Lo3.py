class Worker:

    def __init__(self, name, surname, position, income, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": income, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, income, bonus):
        super().__init__(name, surname, position, income, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return f'{sum(self._income.values())}'


a = Position('Oleg', 'Petrov', 'Manager', 100000, 25000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())