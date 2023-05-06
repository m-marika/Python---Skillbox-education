string = input("Введите строку: ")

start = string.index("h")

end = string[::-1].index("h")
end = len(string) - end - 1

print("Развёрнутая последовательность между первым и последним h:", string[end - 1:start:-1])

# зачтено
