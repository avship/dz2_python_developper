
people = [
    ["Лермонтов", 1814],
    ["Столыпин", 1862],
    ["Сталлоне", 1946],
    ["Высоцкий", 1938],
    ["Папанов", 1922],
]

while True:
    n_true = 0

    for item in people:
        year = input(f"Когда родился {item[0]} ")
        if year.isnumeric() and int(year) == item[1]:
            n_true += 1

    print(f"Количество правильных ответов: {n_true}")
    print(f"Количество неправильных ответов: {len(people)-n_true}")
    print(f"Процент правильных ответов: {n_true*100/len(people)}")
    print(f"Процент неправильных ответов: {(len(people)-n_true)*100/len(people)}")

    next_round = input("Введите 'да', если хотите повторить:")
    if next_round != 'да':
        break