import loto_classes
import time

'''старт игры'''

#перемешаем бочонки в мешке
barrels = loto_classes.Barrels()
barrel = barrels.bochonki()
#создадим экземпляр класса player
player = loto_classes.Players()

#1 игрок и 1 компьютер
def game_user_comp():

    user = player.create_card()
    comp = player.create_card()
    
    #старт игры
    
    while len(barrel)>0:
        item_barrel = barrel[0]
        barrel.pop(0)
        print(f'Новый бочонок: {item_barrel} (осталось {len(barrel)})')
        
        #выводим карточки
        player.show_card(user, player.name_user)
        player.show_card(comp, player.name_comp)

        user_move = input('Зачеркнуть цифру? (y/n): ')
        if user_move == 'y':
            if item_barrel in user:
                ind = user.index(item_barrel)
                user[ind] = '-'
            else:
                print(f'цифры {item_barrel} нет в карточке - вы проиграли')
                break
        elif user_move == 'n':
            if item_barrel not in user:
                pass
            else:
                print(f'цифра {item_barrel} есть в карточке - вы проиграли')
                break 
        if item_barrel in comp:
            ind = comp.index(item_barrel)   
            comp[ind] = '-'
        #проверка выигрышной карты
        user_win = []
        computer_win = []
        for us in user:
            if isinstance(us, int):
                user_win.append(us)
        for co in comp:
            if isinstance(co, int):
                computer_win.append(co)
        
        if len(user_win) == 0:
        #выводим карточки
            player.show_card(user, player.name_user)
            player.show_card(comp, player.name_comp)
            print('Человек победил!')
            break
        if len(computer_win) == 0:
        #выводим карточки
            player.show_card(user, player.name_user)
            player.show_card(comp, player.name_comp)
            print('машинный разум сильнее!')
            break   

#1 игрок и 1 игрок
def game_user_user():

    user = player.create_card()
    user_1 = player.create_card()

    #старт игры
    while len(barrel)>0:
        item_barrel = barrel[0]
        barrel.pop(0)
        print(f'Новый бочонок: {item_barrel} (осталось {len(barrel)})')
        #выводим карточки
        player.show_card(user, player.name_user)
        player.show_card(user_1, player.name_user)
        #зачеркиваем цифры
        user_move_1 = input('Первый игрок зачеркнуть цифру? (y/n): ')
        user_move_2 = input('Второй игрок зачеркнуть цифру? (y/n): ')
        #проверка первого игрока
        if user_move_1 == 'y':
            if item_barrel in user:
                ind = user.index(item_barrel)
                user[ind] = '-'
            else:
                print(f'цифры {item_barrel} нет в карточке - 1 игрок проиграл')
                break
        elif user_move_1 == 'n':
            if item_barrel not in user:
                pass
            else:
                print(f'цифра {item_barrel} есть в карточке - 1 игрок проиграл')
                break 
        #проверка второго игрока
        if user_move_2 == 'y':
            if item_barrel in user_1:
                ind = user_1.index(item_barrel)
                user_1[ind] = '-'
            else:
                print(f'цифры {item_barrel} нет в карточке - 2 игрок проиграл')
                break
        elif user_move_1 == 'n':
            if item_barrel not in user_1:
                pass
            else:
                print(f'цифра {item_barrel} есть в карточке - 2 игрок проиграл')
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
            player.show_card(user, player.name_user)
            player.show_card(user_1, player.name_user)
            print('Человек 1 победил!')
            break
        if len(user_2_win) == 0:
            player.show_card(user, player.name_user)
            player.show_card(user_1, player.name_user)
            print('Человек 2 победил!')
            break   

#1 компьютер и 1 компьютер
def game_comp_comp():

    comp = player.create_card()
    comp_1 = player.create_card()

    #старт игры
    while len(barrel)>0:
        item_barrel = barrel[0]
        barrel.pop(0)
        print(f'Новый бочонок: {item_barrel} (осталось {len(barrel)})')
        #задержка вывода, чтобы была видна игра компьютеров
        time.sleep(0.1)
        #выводим карточки
        player.show_card(comp, player.name_comp)
        player.show_card(comp_1, player.name_comp)
        if item_barrel in comp:
            ind = comp.index(item_barrel)   
            comp[ind] = '-'
        if item_barrel in comp_1:
            ind = comp_1.index(item_barrel)   
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
            player.show_card(comp, player.name_comp)
            player.show_card(comp_1, player.name_comp)
            print('машинный разум 1 сильнее!')
            break
        if len(comp_2_win) == 0:
            player.show_card(comp, player.name_comp)
            player.show_card(comp_1, player.name_comp)
            print('машинный разум 2 сильнее!')
            break