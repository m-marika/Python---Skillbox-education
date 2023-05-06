def get_input_parameters():
    """
    Получаем неотсортированный список чисел

    :return: неотсортированный список чисел, например: [1, 4, -3, 0, 10]
    :rtype: List[int]
    """

    result_list = [1, 4, -3, 0, 10]
    print("Изначальный список:", result_list)

    return result_list


def display_result(sorted_list):
    """
    Выводим отсортированный список

    :param sorted_list: отсортированный список, например: [-3, 0, 1, 4, 10]
    :type sorted_list: List[int]
    """
    print("Отсортированный список:", sorted_list)


def sort_list(original_list):
    """
    Сортируем список

    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: отсортированный, например: [-3, 0, 1, 4, 10]
    :rtype: List[int]
    """
    count = 0
    move = 0
    close_index = len(original_list) - 1

    for i in original_list:
        if close_index >= i:
            for j in original_list:
                if close_index >= j:
                    if count != len(original_list) - 1 and original_list[count] > original_list[count + 1]:
                        original_list[count], original_list[count + 1] = original_list[count + 1], original_list[count]
                        move += 1
                    count += 1

            count = 0
            close_index -= 1
            if move == 0:
                break
            move = 0
        else:
            break
    return original_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
