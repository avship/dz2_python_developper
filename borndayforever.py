year_of_birth = input("Год рождения Пушкина?")

while not(year_of_birth.isdigit() and int(year_of_birth) == 1799):
    year_of_birth = input("Год рождения Пушкина?")

day_of_birth = input("День рождения Пушкина?")
while not(day_of_birth.isdigit() and int(day_of_birth) == 6):
    day_of_birth = input("День рождения Пушкина?")
print('Верно')