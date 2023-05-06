def string_in_string(str1, str2):
    result = "Первую строку нельзя получить из второй с помощью циклического сдвига."

    if len(str1) != len(str2):
        return result
    help_1 = -1
    help_2 = -1
    count_eq = 0
    count = 0

    for i in str1:
        for j in str2:
            if i == j and (abs(str2.index(j) - str1.index(i)) == abs(help_1 - help_2) or help_1 == -1):
                help_1 = str1.index(i)
                help_2 = str2.index(j)
                count_eq += 1
        count += 1
        if count != count_eq:
            return result

    shift = abs(help_2 - help_1)
    result = "Первая строка получается из второй со сдвигом {shift}".format(shift=shift)

    return result


first_string = input("Первая строка: ")
second_string = input("Вторая строка: ")

answer = string_in_string(first_string, second_string)

print(answer)

"""
# another answer:

def is_cyclic_shift(s1, s2):
    n = len(s1)
    if n != len(s2):
        return False
    for i in range(n):
        if s1 == s2[i:] + s2[:i]:
            return i
    return False


s1 = input('Первая строка: ')
s2 = input('Вторая строка: ')
shift = is_cyclic_shift(s1, s2)
if shift is not False:
    print(f'Первая строка получается из второй со сдвигом {shift}.')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
"""

# зачтено
