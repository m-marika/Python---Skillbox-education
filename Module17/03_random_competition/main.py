import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

results = [first_team[item] if first_team[item] > second_team[item]
           else second_team[item]
           for item in range(20)]

print("Первая команда:", first_team)
print("Вторая команда:", second_team)
print("Победители тура:", results)

# зачтено
