def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res

def my_func2(x, y):
    return 1 / x ** abs(y)

print("Вариант 1: ", my_func(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
print("Вариант 2: ", my_func2(int(input("Введите первое число: ")), int(input("Введите второе число: "))))