guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

command = ""

while command != "Пора спать":
    print("\nСейчас на вечеринке", len(guests), "человек:", guests)
    command = input("Гость пришёл или ушёл? ")
    if command != "Пора спать":
        name = input("Имя гостя: ")
    if command == "пришёл":
        if len(guests) == 6:
            print("Прости,", name, "но мест нет.")
        else:
            guests.append(name)
            print("Привет,", name, "!")
    elif command == "ушёл":
        guests.remove(name)
        print("Пока,", name, "!")

print("Вечеринка закончилась, все легли спать.")

# зачтено
