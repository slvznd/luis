from itertools import count
from itertools import cycle


def generator_one(number1, number2):
    for el in count(number1):
        if el > number2:
            break
        else:
            print(el)


def generator_two(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1


generator_one(number1=int(input("Введите начальное число: ")), number2=int(input("Введите конечное число: ")))
generator_two(my_list=[4, 9], iteration=int(input("Введите шаг: ")))
