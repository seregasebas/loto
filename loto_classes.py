import random

'''класс генерации и вывыода игровых карт'''
class Lotto_cards():
    # генерация случайных цифр
    def create_card(self):
        self.numbers = []
        self.card = []
        while len(set(self.numbers)) < 15:
            self.numbers = [random.randint(1,90) for i in range(15)]
        for i in range(15):
            r = random.randint(0,1)
            if r == 1:
                self.card.append(self.numbers[i])
                self.card.append(' ')
            else:
                self.card.append(self.numbers[i])
        while len(self.card) < 27:
            self.card.append(' ')
        return self.card

    #функция вывода карточки
    def show_card(self, card, name):
        self.card = card
        self.name = name
        print(f'{"-"*9} {self.name} {"-"*9}')
        for i in range(0,27,9):
            print(*self.card[i:i+9])
        print('-'*25)

    def __str__(self):
        return f'create_card(self) создает карту игрока(компа), show_card(self, card, name) выводит карту'

    def __eq__(self, other):
        return len(self) == len(other)

'''класс создания игроков и вывода их карт'''
class Players(Lotto_cards):

    def __init__(self, name = 'игрок', name_1 = 'комп'):
        self.name_user = name
        self.name_comp = name_1

    def __str__(self):
        return f'Имя игрока: {self.name_user}, имя компьтера: {self.name_comp}'

'''класс генерации бочонков'''
class Barrels():
    # бочонки перемешали
    def bochonki(self):
        barrels = [i for i in range(1,91)]
        random.shuffle(barrels)
        self.barrels = barrels
        return self.barrels

    def __str__(self):
        res = Barrels()
        self.res = res.bochonki()
        return f'количсечтво бочонков в мешке в начале игры = {len(self.res)}'

    def len(self):
        res = Barrels()
        self.res = res.bochonki()
        return len(self.res)

    def __eq__(self, other):
        return len(self) == len(other)

    

