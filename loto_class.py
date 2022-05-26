import random

# бочонки перемешали
barrels = [i for i in range(1,91)]
random.shuffle(barrels)

# бочонки из мешка
while len(barrels) > 0:
    barell = barrels[0]
    barrels.pop(0)
    print(f'Новый бочонок: {barell} (осталось {len(barrels)})') 

# генерация случайных цифр
user = []
while len(set(user)) < 15:
    user = [random.randint(1,91) for i in range(15)]
computer = []
while len(set(computer)) < 15:
    computer = [random.randint(1,91) for i in range(15)]