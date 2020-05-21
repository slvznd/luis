def init_func():
    output = 0
    work = True
    while work == True:
        numbers = input("Введите числа через пробел или Q для выхода: ").split()
        res = 0
        for number in range(len(numbers)):
            if numbers[number] == 'q' or numbers[number] == 'Q' or numbers[number] == 'й' or numbers[number] == 'Й':
                work = False
                break
            else:
                res = res + int(numbers[number])
        output = output + res
        print(f"Текущая сумма равна: {output}")
    print(f"В итоге: {output}")

init_func()