class checklist(Exception):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка")

            if input(f'Продолжаем? Y/N \n').lower() == 'n':
                return print(f'Вы вышли')


try_except = checklist()
try_except.my_input()
