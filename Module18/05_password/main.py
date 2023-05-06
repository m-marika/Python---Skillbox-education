count_num = 0
flag_upper = False

while True:
    password = input("Придумайте пароль: ")

    for letter in password:
        if letter.isnumeric():
            count_num += 1
        elif letter.isupper():
            flag_upper = True
    if count_num > 2 and flag_upper and len(password) >= 8:
        print("Это надёжный пароль!")
        break
    else:
        print("Попробуйте ещё раз.")

# зачтено
