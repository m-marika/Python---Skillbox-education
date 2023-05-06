def get_input_parameters():
    """
    Получаем входное слово

    :return: например: abccba
    :rtype: str
    """
    user_word = input("Введите слово: ")
    return user_word


def display_result(is_palindrome):
    """
    Выводим информацию является ли строка палиндромом

    :param is_palindrome: является ли палиндромом, например: True
    :type is_palindrome: bool
    """
    if is_palindrome:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")


def check_palindrome(word):
    """
    Проверяем является ли слово палиндромом.

    :param word: слово, например: abccba
    :type word: str

    :return: является ли слово палиндром, например: True
    :rtype: bool
    """

    count_end = len(word) - 1
    palindrome = True

    for sym in word:
        if sym == word[count_end]:
            pass
        else:
            palindrome = False
            break
        count_end -= 1

    return palindrome

if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
