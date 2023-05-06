first_list = []
second_list = []

for i in range(1, 4):
    print("Введите", i, "-е число для первого списка:", end=" ")
    number = int(input())
    first_list.append(number)
for j in range(1, 8):
    print("Введите", j, "-е число для второго списка:", end=" ")
    number = int(input())
    second_list.append(number)

print("Первый список:", first_list)
print("Второй список:", second_list)

first_list.extend(second_list)

for i in first_list:
    while first_list.count(i) != 1:
        first_list.remove(i)

print("Новый первый список с уникальными элементами:", first_list)

# зачтено
