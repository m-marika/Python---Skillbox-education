def calculate_sum_of_number(number):
    sum_result = 0
    for num in str(number):
        sum_result += int(num)
    print("Сумма чисел:", sum_result)
    return sum_result


def calculate_number_of_digits(number):
    result = 0
    for _ in str(number):
        result += 1
    print("Количество цифр в числе:", result)
    return result


user_number = int(input("Введите число: "))
sum_number = calculate_sum_of_number(user_number)
count_number = calculate_number_of_digits(user_number)
print("Разность суммы и количества цифр:", sum_number - count_number)

# зачтено
