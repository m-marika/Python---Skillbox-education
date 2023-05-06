def get_input_parameters():
    """
    Получаем список фильмов, которые пользователь хочет добавить в "любимые"

    :return: добавляемые фильмы, например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    :rtype: List[str]
    """
    result_list = []
    count = int(input("Сколько фильмов хотите добавить? "))
    for num in range(1, count + 1):
        print("Введите название фильма:", end=" ")
        movie = input()
        result_list.append(movie)
    return result_list


def display_result(favorite_films, errors):
    """
    Выводим список ошибок и список любимых фильмов

    :param favorite_films: список любимых фильмов, например: ["Леон", "Мементо"]
    :type favorite_films: List[str]
    :param errors: список ненайденных фильмов, например: ["Безумный Макс", "Царь горы"]
    :type errors: List[str]
    """
    print()

    for err in errors:
        print("Ошибка: фильма", err, "у нас нет :(")

    for like in favorite_films:
        print("Ваш список любимых фильмов:", like, end=" ")



def add_favorite_film(new_favorite_films, available_films):
    """
    Добавляем фильмы в список "любимых".

    :param new_favorite_films: фильмы, которые нужно добавить в "любимые",
           например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    :type new_favorite_films: List[str]
    :param available_films: фильмы, которые есть на киносайте,
           например: ["Леон", "Назад в будущее", "Мементо"]
    :type available_films: List[str]

    :return: Список фильмов в списке "любимых" и список не найденных фильмов,
             например: (["Леон", "Мементо"], ["Безумный Макс", "Царь горы"])
    :rtype: Tuple[List[str], List[str]]
    """

    like_list = []
    error_list = []

    for movie in new_favorite_films:
        for like in available_films:
            if movie == like:
                like_list.append(movie)
                break
        else:
            error_list.append(movie)

    return like_list, error_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист",
        "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(
        new_favorite_films,
        available_films
    )  # добавлем фильмы в список "любимых".
    display_result(favorite_films, errors)  # выводим результат
