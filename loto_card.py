import random

class Lotto_cards():
    
    def __init__(self):
        pass
    
    # генерация случайных цифр
    def random_numbers(self):
        numbers = []
        while len(set(numbers)) < 15:
            numbers = [random.randint(1,90) for i in range(15)]
        return numbers

    #функция создания карточки
    def create_card(self, list_new):
        self.list_new = list_new
        card = []
        for i in range(15):
            r = random.randint(0,1)
            if r == 1:
                card.append(self.list_new[i])
                card.append(' ')
            else:
                card.append(self.list_new[i])
        while len(card) < 27:
            card.append(' ')
        return card
    
    #функция вывода карточки
    def show_card(self, card, name):
        self.card = card
        self.name = name
        print(f'{"-"*9} {self.name} {"-"*9}')
        print(*self.card[0:9])
        print(*self.card[9:18])
        print(*self.card[18:27])
        print('-'*25)

a = Lotto_cards()

def start_card():
    user = a.random_numbers()
    user = a.create_card(user)
    computer = a.random_numbers()
    computer = a.create_card(computer)
    return user, computer
    
def show_game(user, computer): 
    a.show_card(user, 'юзер')
    a.show_card(computer, 'комп')