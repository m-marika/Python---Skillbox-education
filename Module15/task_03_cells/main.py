def get_input_parameters():
    """
    Получаем набор клеток

    :return: набор клеток, например: [3, 0, 6, 2, 10]
    :rtype: List[int]
    """

    result_list = []
    count = int(input("Кол-во клеток: "))
    for num in range(1, count + 1):
        print(f"Эффективность {num} клетки:", end=" ")
        efficiency = int(input())
        result_list.append(efficiency)
    return result_list


def display_result(cells):
    """
    Выводим список клеток у которых значение меньше индекса

    :param cells: набор клеток, например: [0, 2]
    :type cells: List[int]
    """

    print("\nНеподходящие значения:", end=" ")
    for num in cells:
        print(num, end=" ")


def select_cells(cells):
    """
    Отбираем список клеток, у которых значение меньше индекса.

    :param cells: набор клеток, например: [3, 0, 6, 2, 10]
    :type cells: List[int]

    :return: набор подходящих клеток, например: [0, 2]
    :rtype: List[int]
    """

    result = []
    count = 1
    for cel in cells:
        if cel < count:
            result.append(cel)
        count += 1
    return result


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
