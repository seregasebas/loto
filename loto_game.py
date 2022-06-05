import game_functions

#кто играет
who_vs_who = int(input('1 - человек против человека/ 2 - человек против компьютера/ 3 - комп против компа введите 1/2/3?: '))

#создадим карточки игрока(ов)    
if who_vs_who == 1:
    #старт игры
    game_functions.game_user_user()
elif who_vs_who == 2:
    #старт игры
    game_functions.game_user_comp()
elif who_vs_who == 3:
    #старт игры
    game_functions.game_comp_comp()





