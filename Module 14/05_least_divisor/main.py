def min_devision(number):
    result_1 = ""
    result_2 = ""
    flag = True

    for dev in range(2, number + 1):
        if number % dev == 0:
            return dev


user_number = int(input("Введите число: "))

result = min_devision(user_number)

print("Наименьший делитель, отличный от единицы:", result)

# зачтено
