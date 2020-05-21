def viewdata(name, surname, birthdate, email, tel):
    print(f"Вы ввели имя {name} {surname}, дата рождения: {birthdate}, e-mail: {email}, телефон: {tel}")


viewdata(name=input("Введите имя: "),
         surname=input("Введите фамилию: "),
         birthdate=input("Введите дату рождения: "),
         email=input("Введите эл. адрес почты: "),
         tel=input("Введите телефон: "))
