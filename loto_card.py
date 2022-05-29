import random

'''класс генерации и вывыода игровых карт'''
class Lotto_cards():
    # генерация случайных цифр
    @staticmethod
    def random_numbers():
        numbers = []
        while len(set(numbers)) < 15:
            numbers = [random.randint(1,90) for i in range(15)]
        return numbers

    #функция создания карточки
    @staticmethod
    def create_card(list_new):
        card = []
        for i in range(15):
            r = random.randint(0,1)
            if r == 1:
                card.append(list_new[i])
                card.append(' ')
            else:
                card.append(list_new[i])
        while len(card) < 27:
            card.append(' ')
        return card
    
    #функция вывода карточки
    @staticmethod
    def show_card(card, name):
        print(f'{"-"*9} {name} {"-"*9}')
        print(*card[0:9])
        print(*card[9:18])
        print(*card[18:27])
        print('-'*25)

'''класс создания игроков и вывода их карт'''
class Players():
    @staticmethod
    def start_card():
        user = Lotto_cards.random_numbers()
        user = Lotto_cards.create_card(user)
        computer = Lotto_cards.random_numbers()
        computer = Lotto_cards.create_card(computer)
        return user, computer

    #вывод карт 1 игрока и 1 компьютера
    @staticmethod
    def show_game(user, computer): 
        Lotto_cards.show_card(user, 'юзер')
        Lotto_cards.show_card(computer, 'комп')

    #вывод карт 2 игроков и 2 компьютеров
    @staticmethod
    def show_game_2_users(user_1, computer_1, user_2, computer_2): 
        Lotto_cards.show_card(user_1, 'юзер_1')
        Lotto_cards.show_card(user_2, 'юзер_2')
        Lotto_cards.show_card(computer_1, 'комп_1')
        Lotto_cards.show_card(computer_2, 'комп_1')

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
    def game_one_user(barrels, user, computer):
        #старт игры
        while len(barrels)>0:
            barell = barrels[0]
            barrels.pop(0)
            print(f'Новый бочонок: {barell} (осталось {len(barrels)})')

            Players.show_game(user,computer)

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
                print('Человек победил!')
                Players.show_game(user,computer)
                break
            if len(computer_win) == 0:
                Players.show_game(user,computer)
                print('машинный разум сильнее!')
                break

    #2 игрока и 2 компьютера
    @staticmethod
    def game_two_users(barrels, user_1, computer_1, user_2, computer_2):
        #старт игры
        while len(barrels)>0:
            barell = barrels[0]
            barrels.pop(0)
            print(f'Новый бочонок: {barell} (осталось {len(barrels)})')

            Players.show_game_2_users(user_1,computer_1, user_2,computer_2)

            user_move_1 = input('Игрок 1, зачеркнуть цифру? (y/n): ')
            user_move_2 = input('Игрок 2, зачеркнуть цифру? (y/n): ')

            if user_move_1 == 'y':
                if barell in user_1:
                    ind = user_1.index(barell)
                    user_1[ind] = '-'
                else:
                    print(f'цифры {barell} нет в карточке 1 игрока - вы проиграли')
                    break
            elif user_move_1 == 'n':
                if barell not in user_1:
                    pass
                else:
                    print(f'цифра {barell} есть в карточке игрока 1 - вы проиграли')
                    break 

            if user_move_2 == 'y':
                if barell in user_2:
                    ind = user_2.index(barell)
                    user_2[ind] = '-'
                else:
                    print(f'цифры {barell} нет в карточке 2 игрока - вы проиграли')
                    break
            elif user_move_2 == 'n':
                if barell not in user_2:
                    pass
                else:
                    print(f'цифра {barell} есть в карточке игрока 2 - вы проиграли')
                    break

            if barell in computer_1:
                ind = computer_1.index(barell)   
                computer_1[ind] = '-'
            if barell in computer_2:
                ind = computer_2.index(barell)   
                computer_2[ind] = '-'

            #проверка выигрышной карты
            user_win_1 = []
            computer_win_1 = []
            user_win_2 = []
            computer_win_2 = []
            for us in user_1:
                if isinstance(us, int):
                    user_win_1.append(us)
            
            for us in user_2:
                if isinstance(us, int):
                    user_win_2.append(us)

            for comp in computer_1:
                if isinstance(comp, int):
                    computer_win_1.append(comp)

            for comp in computer_2:
                if isinstance(comp, int):
                    computer_win_2.append(comp)
            
            if len(user_win_1) == 0:
                print('Человек 1 победил!')
                Players.show_game_2_users(user_1,computer_1, user_2,computer_2)
                break
            if len(computer_win_1) == 0:
                Players.show_game_2_users(user_1,computer_1, user_2,computer_2)
                print('машинный разум 1 сильнее!')
                break
            if len(user_win_2) == 0:
                print('Человек 2 победил!')
                Players.show_game_2_users(user_1,computer_1, user_2,computer_2)
                break
            if len(computer_win_2) == 0:
                Players.show_game_2_users(user_1,computer_1, user_2,computer_2)
                print('машинный разум 2 сильнее!')
                break