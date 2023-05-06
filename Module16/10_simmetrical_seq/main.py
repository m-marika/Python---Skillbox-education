def simmetric(massiv):
    count = 1
    if len(massiv) == 1:
        return True

    for i in massiv:
        if i == massiv[-count]:
            pass
        else:
            return False
        count += 1
    return True


amount = int(input("Кол-во чисел: "))
sequence = []

for i in range(amount):
    number = int(input("Число: "))
    sequence.append(number)

print("\nПоследовательность:", sequence)

result = simmetric(sequence)

helper = 0
sequence_result = []

while result is False:

    if result is False:
        sequence_result.insert(0, sequence[0])
        sequence.remove(sequence[0])
        helper += 1

    result = simmetric(sequence)

print("Нужно приписать чисел:", helper)
print("Сами числа:", sequence_result)

# зачтено
