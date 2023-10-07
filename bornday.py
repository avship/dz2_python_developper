year_of_birth = input("Год рождения Пушкина?")
if year_of_birth.isdigit() and int(year_of_birth) == 1799:
    day_of_birth = input("День рождения Пушкина?")
    if day_of_birth.isdigit() and int(day_of_birth) == 6:
        print("Верно")
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')