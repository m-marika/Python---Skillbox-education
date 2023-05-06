user_str = input("Введите строку: ").split()
result = [word[0].upper() + word[1:] for word in user_str]

print("Результат:", " ".join(result))

# зачтено
