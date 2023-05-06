number_people = int(input("Кол-во человек: "))
number_to_leave = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", number_to_leave, "-й человек")

list_people = list(range(1, number_people + 1))
remove_number = 0
count_remove = 0

while len(list_people) != 1:
    print("\nТекущий круг людей:", list_people)
    print("Начало счёта с номера", list_people[count_remove])

    if number_to_leave > len(list_people):
        count_remove = (number_to_leave % len(list_people)) + count_remove - 1
    else:
        if (count_remove + number_to_leave - 1) <= len(list_people) - 1:
            count_remove = count_remove + number_to_leave - 1
        else:
            count_remove = (len(list_people) - count_remove) - 2
    remove_number = list_people[count_remove]
    list_people.remove(remove_number)
    print("Выбывает человек под номером", remove_number)
    if count_remove == len(list_people):
        count_remove = 0

print("\nОстался человек под номером", list_people[0])

# зачтено
