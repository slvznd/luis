from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def something(number1, number2):
    return number1 * number2


print(reduce(something, my_list))