import loto_card

#перемешаем бочонки в мешке
barrels = loto_card.Barrels.bochonki()

value = int(input('Сколько будет человеческих игроков? 1/2: '))
if value == 1:
    #создадим карточки игрока и компьютера
    user,computer = loto_card.Players.start_card()
    #да начнется игра
    loto_card.Start_game.game_one_user(barrels, user, computer)
elif value == 2:
    #создадим карточки игрокков и компьютеров
    user_1,computer_1 = loto_card.Players.start_card()
    user_2,computer_2 = loto_card.Players.start_card()
    loto_card.Start_game.game_two_users(barrels, user_1, computer_1, user_2, computer_2)



