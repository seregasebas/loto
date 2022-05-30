import random
import time

'''класс генерации и вывыода игровых карт'''
class Lotto_cards():
    # генерация случайных цифр
    @staticmethod
    def create_card():
        numbers = []
        card = []
        while len(set(numbers)) < 15:
            numbers = [random.randint(1,90) for i in range(15)]
        for i in range(15):
            r = random.randint(0,1)
            if r == 1:
                card.append(numbers[i])
                card.append(' ')
            else:
                card.append(numbers[i])
        while len(card) < 27:
            card.append(' ')
        return card

    #функция вывода карточки
    @staticmethod
    def show_card(card, name):
        print(f'{"-"*9} {name} {"-"*9}')
        for i in range(0,27,9):
            print(*card[i:i+9])
        print('-'*25)

'''класс создания игроков и вывода их карт'''
class Players():
    @staticmethod
    def start_card_user():
        user = Lotto_cards.create_card()
        return user

    @staticmethod
    def start_card_comp():
        computer = Lotto_cards.create_card()
        return computer

    #вывод карт 
    #юзер
    @staticmethod
    def show_game_user(user): 
        Lotto_cards.show_card(user, 'юзер')
    #комп
    @staticmethod
    def show_game_comp(comp): 
        Lotto_cards.show_card(comp, 'комп')

'''класс генерации бочонков'''
class Barrels():
    # бочонки перемешали
    @staticmethod
    def bochonki():
        barrels = [i for i in range(1,91)]
        random.shuffle(barrels)
        return barrels

'''класс старта игры'''
class Start_game():
    #1 игрок и 1 компьютер
    @staticmethod
    def game_user_comp(barrels, user, computer):
        #старт игры
        while len(barrels)>0:
            barell = barrels[0]
            barrels.pop(0)
            print(f'Новый бочонок: {barell} (осталось {len(barrels)})')
            
            #выводим карточки
            Players.show_game_user(user)
            Players.show_game_comp(computer)

            user_move = input('Зачеркнуть цифру? (y/n): ')

            if user_move == 'y':
                if barell in user:
                    ind = user.index(barell)
                    user[ind] = '-'
                else:
                    print(f'цифры {barell} нет в карточке - вы проиграли')
                    break
            elif user_move == 'n':
                if barell not in user:
                    pass
                else:
                    print(f'цифра {barell} есть в карточке - вы проиграли')
                    break 

            if barell in computer:
                ind = computer.index(barell)   
                computer[ind] = '-'

            #проверка выигрышной карты
            user_win = []
            computer_win = []
            for us in user:
                if isinstance(us, int):
                    user_win.append(us)

            for comp in computer:
                if isinstance(comp, int):
                    computer_win.append(comp)
            
            if len(user_win) == 0:
                Players.show_game_user(user)
                Players.show_game_comp(computer)
                print('Человек победил!')
                break
            if len(computer_win) == 0:
                Players.show_game_user(user)
                Players.show_game_comp(computer)
                print('машинный разум сильнее!')
                break   

    #1 игрок и 1 игрок
    @staticmethod
    def game_user_user(barrels, user, user_1):
        #старт игры
        while len(barrels)>0:
            barell = barrels[0]
            barrels.pop(0)
            print(f'Новый бочонок: {barell} (осталось {len(barrels)})')

            #выводим карточки
            Players.show_game_user(user)
            Players.show_game_user(user_1)

            user_move_1 = input('Первый игрок зачеркнуть цифру? (y/n): ')
            user_move_2 = input('Второй игрок зачеркнуть цифру? (y/n): ')
            #проверка первого игрока
            if user_move_1 == 'y':
                if barell in user:
                    ind = user.index(barell)
                    user[ind] = '-'
                else:
                    print(f'цифры {barell} нет в карточке - 1 игрок проиграл')
                    break
            elif user_move_1 == 'n':
                if barell not in user:
                    pass
                else:
                    print(f'цифра {barell} есть в карточке - 1 игрок проиграл')
                    break 
            #проверка второго игрока
            if user_move_2 == 'y':
                if barell in user_1:
                    ind = user_1.index(barell)
                    user_1[ind] = '-'
                else:
                    print(f'цифры {barell} нет в карточке - 2 игрок проиграл')
                    break
            elif user_move_1 == 'n':
                if barell not in user_1:
                    pass
                else:
                    print(f'цифра {barell} есть в карточке - 2 игрок проиграл')
                    break 
           #проверка выигрышной карты
            user_1_win = []
            user_2_win = []
            for us in user:
                if isinstance(us, int):
                    user_1_win.append(us)

            for us in user_1:
                if isinstance(us, int):
                    user_2_win.append(us)
            
            if len(user_1_win) == 0:
                Players.show_game_user(user)
                Players.show_game_user(user_1)
                print('Человек 1 победил!')
                break
            if len(user_2_win) == 0:
                Players.show_game_user(user)
                Players.show_game_user(user_1)
                print('Человек 2 победил!')
                break   


    #1 компьютер и 1 компьютер
    @staticmethod
    def game_comp_comp(barrels, comp, comp_1):
        #старт игры
        while len(barrels)>0:
            barell = barrels[0]
            barrels.pop(0)
            print(f'Новый бочонок: {barell} (осталось {len(barrels)})')

            #задержка вывода, чтобы была видна игра компьютеров
            time.sleep(0.1)
            #выводим карточки
            Players.show_game_comp(comp)
            Players.show_game_comp(comp_1)

            if barell in comp:
                ind = comp.index(barell)   
                comp[ind] = '-'
            if barell in comp_1:
                ind = comp_1.index(barell)   
                comp_1[ind] = '-'

            #проверка выигрышной карты
            comp_1_win = []
            comp_2_win = []

            for computer in comp:
                if isinstance(computer, int):
                    comp_1_win.append(computer)
            for computer in comp_1:
                if isinstance(computer, int):
                    comp_2_win.append(computer)
            
            if len(comp_1_win) == 0:
                Players.show_game_comp(comp)
                Players.show_game_comp(comp_1)
                print('машинный разум 1 сильнее!')
                break
            if len(comp_2_win) == 0:
                Players.show_game_comp(comp)
                Players.show_game_comp(comp_1)
                print('машинный разум 2 сильнее!')
                break   