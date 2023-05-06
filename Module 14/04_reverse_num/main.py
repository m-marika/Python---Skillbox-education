def reverse_number(number):
    result_1 = ""
    result_2 = ""
    flag = True

    for num in str(number):
        if num != "." and flag:
            result_1 = num + result_1
        else:
            if num == ".":
                pass
            else:
                result_2 = num + result_2
            flag = False

    result = float(result_1 + "." + result_2)
    return result


first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

result_first = reverse_number(first_number)
result_second = reverse_number(second_number)

print("Первое число наоборот:", result_first)
print("Второе число наоборот:", result_second)
print("Сумма:", result_second + result_first)

# зачтено
