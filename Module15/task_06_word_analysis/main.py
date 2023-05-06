def get_input_parameters():
    """
    Получаем входное слово

    :return: входное слово, например: "привет"
    :rtype: str
    """

    user_word = input("Введите слово: ")

    return user_word


def display_result(number_unique_letters):
    """
    Выводим количество уникальных букв в слове

    :param number_unique_letters: количество уникальных букв в слове, например: 6
    :type number_unique_letters: int
    """
    print("Кол-во уникальных букв:", number_unique_letters)


def count_number_unique_letters(word):
    """
    Считаем количество уникальных букв в слове.

    :param word: входное слово, например: "привет"
    :type word: str

    :return: количество уникальных букв в слове, например: 6
    :rtype: int
    """

    word_list = list(word)
    count = 1
    lenght_word = len(word_list)
    non_unic = []

    for sym in word:
        for i in range(count, lenght_word):
            if sym == word_list[i]:
                non_unic.append(sym)
        count += 1

    return lenght_word - 2 * len(non_unic)


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
