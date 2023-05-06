number_rolls = int(input("Кол-во коньков: "))
size = 0
rolls_list = []

for i in range(1, number_rolls + 1):
    print("Размер", i, "-й пары:", end=" ")
    size = int(input())
    rolls_list.append(size)

people = int(input("\nКол-во людей: "))
people_list = []
people_size = 0

for j in range(1, people + 1):
    print("Размер ноги", j, "-го человека:", end=" ")
    people_size = int(input())
    people_list.append(people_size)

people_rolls = 0
for man in people_list:
    for roll in rolls_list:
        if roll >= man:
            rolls_list.remove(roll)
            people_rolls += 1

print("\nНаибольшее кол-во людей, которые могут взять ролики:", people_rolls)

# зачтено
