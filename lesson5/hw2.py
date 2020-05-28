my_list = ['Привет как твои дела\n', 'Очень тяжелое утро\n', 'Коровавирус\n']
with open("hw2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("hw2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} букв в строке {line}")
    print(f"Количество строк равно {lines}")