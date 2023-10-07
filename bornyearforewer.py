year_of_birth = input("Год рождения Пушкина?")
while not(year_of_birth.isdigit() and int(year_of_birth) == 1799):
    year_of_birth = input("Год рождения Пушкина?")
print('Верно')