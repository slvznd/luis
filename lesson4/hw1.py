from sys import argv

name, hour, basemoney, bonus = argv
result = (int(hour) * int(basemoney)) + int(bonus)
print(f"Зарплата равна {result}")