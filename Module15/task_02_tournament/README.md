## Задача 2. Турнир
Для турнира по волейболу необходимо сформировать турнирнирную
сетку из 8 человек на 2 дня. На первый день из списка участников
решили выбрать каждого второго.

Дан список из 8 имён: Артемий, Борис, Влад, Гоша, Дима, 
Евгений, Женя, Захар. Напишите программу, которая выводит
элементы списка только с чётными индексами.

```
Первый день: ['Артемий', 'Влад', 'Дима', 'Женя']
```
ВАЖНО!
Чтобы корректно отработали автотесты, структура вашей
программы должна быть следующей:
```python
def display_result(participants_names):
    """
    Выводим список имён участников в первый день
    
    :param participants_names: список имён участников, например: ["Артемий", "Влад", "Дима", "Женя"]
    :type participants_names: List[str]
    """
    # TODO: в этой функции пишем весь необходимый код 
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def get_participants_names(names):
    """
    Получаем элементы списка только с чётными индексами.
    
    :param names: список имён, например: ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    :type names: List[str]
    
    :return: список имён с чётными индексами , например: ["Артемий", "Влад", "Дима", "Женя"]
    :rtype: List[str]
    """
    # TODO: в этой функции получаем элементы списка только с чётными индексами..
    #  print'ов и input'ов тут не должно быть. 
    #  Функция на вход принимает ранее инициализированные данные
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_participants_names и display_result
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
```