def get_input_parameters():
    """
    Получаем список видеокарт

    :return: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :rtype: List[int]
    """

    result_list = []
    count = int(input("Кол-во видеокарт: "))
    for num in range(1, count + 1):
        print(num, "Видеокарта:", end=" ")
        video_card = int(input())
        result_list.append(video_card)
    return result_list


def display_result(old_video_cards, new_video_cards):
    """
    Выводим список оставшихся видеокарт

    :param old_video_cards: старый набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type old_video_cards: List[int]
    :param new_video_cards: новый набор видеокарт, например: [3070, 2060, 3070]
    :type new_video_cards: List[int]
    """

    print("\nСтарый список видеокарт:", end=" ")
    for num in old_video_cards:
        print(num, end=" ")

    print("\nНовый список видеокарт:", end=" ")
    for num in new_video_cards:
        print(num, end=" ")

def select_video_cards(video_cards):
    """
    Удаляем из списка видеокарт наибольшие элементы.

    :param video_cards: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type video_cards: List[int]

    :return: набор оставшихся видеокарт, например: [3070, 2060, 3070]
    :rtype: List[int]
    """

    max_result = 0
    result_list = []

    for num in video_cards:
        default = num
        if default >= max_result:
            max_result = default

    for num in video_cards:
        if num != max_result:
            result_list.append(num)

    return result_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
