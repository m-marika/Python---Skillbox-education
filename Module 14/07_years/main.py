# TODO здесь писать код
def find_three_equally(start, end):
    print("Годы от", start, "до", end, "с тремя одинаковыми цифрами:")
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    zero = 0

    for year in range(start, end + 1):
        for i in str(year):
            if i == "1":
                one += 1
            elif i == "2":
                two += 1
            elif i == "3":
                three += 1
            elif i == "4":
                four += 1
            elif i == "5":
                five += 1
            elif i == "6":
                six += 1
            elif i == "7":
                seven += 1
            elif i == "8":
                eight += 1
            elif i == "9":
                nine += 1
            elif i == "0":
                zero += 1
        if one == 3 or two == 3 or three == 3 or four == 3 or five == 3 or six == 3 or seven == 3 or eight == 3 or nine == 3 or zero == 3:
            print(year)
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0
        seven = 0
        eight = 0
        nine = 0
        zero = 0


start_year = int(input("Введите первый год: "))
end_year = int(input("Введите второй год: "))

if start_year <= end_year:
    find_three_equally(start_year, end_year)
else:
    print("Вы ввели некорректные даты начала и конца промежутка")

# зачтено
