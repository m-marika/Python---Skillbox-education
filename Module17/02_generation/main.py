len_number = int(input("Введите длину списка: "))

result_list = [1 if x % 2 == 0 else x % 5 for x in range(len_number)]

print("Результат: ", result_list)

# зачтено
