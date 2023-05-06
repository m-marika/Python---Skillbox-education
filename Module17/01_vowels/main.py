user_string = input("Введите текст: ")
ok_symbol = ["е", "а", "о", "э", "я", "и", "ю", "у"]
result_string = [symbol for symbol in user_string if symbol in ok_symbol]

print("Список гласных букв: ", result_string)
print("Длина списка: ", len(result_string))

# зачтено
