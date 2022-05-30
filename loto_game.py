import loto_classes

#перемешаем бочонки в мешке
barrels = loto_classes.Barrels.bochonki()

who_vs_who = int(input('1 - человек против человека/ 2 - человек против компьютера/ 3 - комп против компа 1/2/3?: '))

#создадим карточки игрока(ов)    
if who_vs_who == 1:
    user = loto_classes.Players.start_card_user()
    user_1 = loto_classes.Players.start_card_user()
    #старт игры
    loto_classes.Start_game.game_user_user(barrels, user, user_1)
elif who_vs_who == 2:
    user = loto_classes.Players.start_card_user()
    computer = loto_classes.Players.start_card_comp()
    #старт игры
    loto_classes.Start_game.game_user_comp(barrels, user, computer)
elif who_vs_who == 3:
    computer = loto_classes.Players.start_card_comp()
    computer_1 = loto_classes.Players.start_card_comp()
    #старт игры
    loto_classes.Start_game.game_comp_comp(barrels, computer, computer_1)





