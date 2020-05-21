def int_func(word):
    first_symbol = word[0]
    big_symbol = chr(ord(first_symbol) - ord('a') + ord('A'))
    return big_symbol + word[1:]


user_input = input("Введите слова: ").split()
output = []
for word in user_input:
    output.append(int_func(word))
print(" ".join(output))