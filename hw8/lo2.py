class Myexc(Exception):
    @staticmethod
    def dn(numbers):
        try:
            return int(numbers[0]) / int(numbers[1])
        except Exception as e:
            return f"Деление на ноль недопустимо ({e})"


while True:
    numbers = input("Введите два числа через пробел \n").split(' ')
    print(f'Результат {Myexc.dn(numbers):.02f}')
    decision = input("Продолжаем? y - да, n - нет \n Ответ: ")
    if decision.lower() == 'n':
        print("Окей выходим")
        break
    else:
        continue
