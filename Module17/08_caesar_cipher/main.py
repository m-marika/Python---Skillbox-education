alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
            'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы',
            'ь', 'э', 'ю', 'я']


def encryption(sentence, step_to):
    new_sentence_index = [alphabet[((alphabet.index(x) + step_to) % len(alphabet))]
                          if x in alphabet
                          else x for x in sentence]
    result = ''
    for el in new_sentence_index:
        result += el

    return result


sentences = input("Введите сообщение: ")
step = int(input("Введите сдвиг: "))

print("Зашифрованное сообщение: ", encryption(sentences, step))

# зачтено
