year_of_birth = input("Год рождения Пушкина?")
if year_of_birth.isdigit() and int(year_of_birth) == 1799:
    print('Верно')
else:
    print('Неверно')