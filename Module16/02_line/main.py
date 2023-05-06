def sort(massiv):
    for i in range(len(massiv)):
        for j in range(i, len(massiv)):
            if massiv[j] < massiv[i]:
                massiv[j], massiv[i] = massiv[i], massiv[j]

    return massiv


first_grade = list(range(160, 177, 2))
second_grade = list(range(162, 181, 3))

first_grade.extend(second_grade)

print("Отсортированный список учеников:", sort(first_grade))

# зачтено
