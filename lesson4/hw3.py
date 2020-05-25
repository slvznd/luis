numbers = range(20, 241)
result = [el for el in numbers if el % 20 == 0 or el % 21 == 0]
print(result)