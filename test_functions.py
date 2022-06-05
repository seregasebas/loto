import loto_classes

#проверка функции генерации бочонков
def test_bochonki():
    a = loto_classes.Barrels()
    a = a.bochonki()
    assert len(a) == 90

#проверка функции генерации карты
def test_create_card():
    a = loto_classes.Lotto_cards()
    a = a.create_card()
    assert len(set(a)) == 16

#проверка функции генерации карты
def test_player_create_card():
    a = loto_classes.Players()
    a = a.create_card()
    assert len(set(a)) == 16

#проверка функции генерации карты
def test_comp_create_card():
    a = loto_classes.Players()
    a = a.create_card()
    assert len(set(a)) == 16
