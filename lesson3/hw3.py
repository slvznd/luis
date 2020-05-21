def my_func(x, y, z):
    numbers = [x, y, z]
    answer = []
    number1 = max(numbers)
    answer.append(number1)
    numbers.remove(number1)
    number2 = max(numbers)
    answer.append(number2)
    print(f"Сумма двух самых больших чисел = {sum(answer)}")

my_func(2, 6, -5)