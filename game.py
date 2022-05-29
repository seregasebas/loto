import random
import loto_card

# бочонки перемешали
def bochonki():
    barrels = [i for i in range(1,91)]
    random.shuffle(barrels)
    return barrels


def game_one_user():

    barrels = bochonki()
    user,computer = loto_card.start_card()

    #старт игры
    while len(barrels)>0:
        barell = barrels[0]
        barrels.pop(0)
        print(f'Новый бочонок: {barell} (осталось {len(barrels)})')

        loto_card.show_game(user,computer)

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
