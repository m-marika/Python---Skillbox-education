def get_input_parameters():
    """
    Получаем сдвиг и начальны список

    :return: например: [3, [1, 4, -3, 0, 10]]
    :rtype: List[int, List[int]]
    """
    result_list = []
    shift = int(input("Сдвиг: "))
    result_list = [1, 4, -3, 0, 10]
    print("Изначальный список:", result_list)

    return [shift, list(result_list)]


def display_result(shifted_list):
    """
    Выводим получившиеся список

    :param shifted_list: сдвинутый список, например: [5, 1, 2, 33, 4]
    :type shifted_list: List[int]
    """
    print("Сдвинутый список:", shifted_list)


def shift_list(shift, original_list):
    """
    Сдвигаем список на определённое количество элементов в право

    :param shift: сдвиг: 3
    :type shift: int
    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: сдвинутый список, например: [5, 1, 2, 3, 4]
    :rtype: List[int]
    """

    count = 0
    first_part = []
    second_part = []
    lenght = len(original_list)
    for num in original_list:
        if count + shift >= lenght:
            first_part.append(num)
        else:
            second_part.append(num)
        count += 1

    for num1 in second_part:
        first_part.append(num1)
    return first_part


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
