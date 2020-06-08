class Backpack:
    my_store_full = []

    def __init__(self, name="", price=0, quantity=0, number_of_lists=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            self.numb = int(input(f'Введите параметр обрабатываемых листов '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        if input(f'Для выхода - Q, продолжение - Enter \n').lower() == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return self.reception()


class Printer(Backpack):
    def my_parameter(self):
        return f'печатает {self.numb} листов в минуту'


class Scanner(Backpack):
    def my_parameter(self):
        return f'сканирует {self.numb} листов в минуту'


class Copier(Backpack):
    def my_parameter(self):
        f'копирует {self.numb} листов в минуту'


print("Добро пожаловать на склад техники! \n")
unit_1 = Printer()
unit_1.reception()
#print(unit_1.my_parameter())
'''
print()
unit_2 = Copier()
unit_2.reception()
print(unit_2.my_parameter())

print()
unit_3 = Scanner()
unit_3.reception()
print(unit_3.my_parameter())
'''
