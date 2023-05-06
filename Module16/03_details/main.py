shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_dig = input("Название детали: ")

count = 0
price = 0
for names in shop:
    for j in names:
        if j == name_dig:
            count += 1
            price += names[1]
            break

print("Кол-во деталей —", count)
print("Общая стоимость —", price)

# зачтено
