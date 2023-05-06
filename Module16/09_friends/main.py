friends = int(input("Кол-во друзей: "))
debts = int(input("Долговых расписок: "))
debts_list = []

for i in range(1, debts + 1):
    print()
    print(i, "-я расписка")
    to_whom = int(input("Кому: "))
    from_who = int(input("От кого: "))
    amount = int(input("Сколько: "))
    debts_list.append([to_whom, from_who, amount])

result = []
for i in range(friends):
    result.append(0)

money = 0
helper = 0

for debt in debts_list:
    for j in debt:
        if helper == 0:
            result[j - 1] -= debt[2]
        elif helper == 1:
            result[j - 1] += debt[2]
        helper += 1
    helper = 0

helper = 1
print("\nБаланс друзей:")
for i in result:
    print(helper, ":", i)
    helper += 1

# зачтено
