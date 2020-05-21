def divide(arg1, arg2):
    try:
        print(f"Результат равен: {int(arg1) / int(arg2)}")
    except ZeroDivisionError:
        print("Деление на ноль!")
        return

x,y = input("Введите числа через пробел: ").split()
divide(x, y)
