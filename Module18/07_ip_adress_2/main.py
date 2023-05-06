user_ip = input("Введите IP: ").split(".")
flag_ok = True

for num in user_ip:
    if not num.isnumeric():
        flag_ok = False
        print(num, "— это не целое число.")
        break
    elif 0 > int(num) or int(num) > 255:
        flag_ok = False
        print(num, "превышает 255.")
        break
    elif len(user_ip) != 4:
        flag_ok = False
        print("Адрес — это четыре числа, разделённые точками.")
        break

if flag_ok:
    print("IP-адрес корректен.")

# зачтено
