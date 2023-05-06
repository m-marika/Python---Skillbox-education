user_str = input("Введите строку: ")
new_str = ""
prev_letter = ""
count = 0

for letter in user_str:
    if letter != prev_letter:
        if count == 0:
            pass
        else:
            new_str += str(count)
        new_str += letter
        count = 1
    else:
        count += 1
    prev_letter = letter
new_str += str(count)

print("Закодированная строка:", new_str)

# зачтено
