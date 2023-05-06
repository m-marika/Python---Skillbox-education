user_str = input("Введите строку: ").split()

max_word = 0
result_word = ""

for word in user_str:
    if max_word < len(word):
        max_word = len(word)
        result_word = word

print("Самое длинное слово:", result_word)
print("Длина этого слова:", max_word)

# зачтено
