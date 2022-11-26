import pytest
import loto_classes

# Для запуска через терминал
#$ pytest --cov=src
#pytest -q test_py_classes.py

class TestLottoCards():
    #выполняется в каждой последующей функции
    def setup(self):
        self.a = loto_classes.Lotto_cards()

    #проверка функции генерации карты
    def test_create_card(self):
        assert len(set(self.a.create_card())) == 16

    #проверка функции генерации карты
    def test_player_create_card(self):
        assert len(self.a.create_card()) == 27

    #проверка функции генерации карты
    def test_comp_create_card(self):
        assert len(set(self.a.create_card())) == 16

    def test_str(self):
        self.card = loto_classes.Lotto_cards()
        assert 'create_card(self) создает карту игрока(компа), show_card(self, card, name) выводит карту' == str(self.card)
    
    def test_eq(self):
        a = loto_classes.Barrels()
        b = loto_classes.Barrels()
        res_a = a.bochonki()
        res_b = b.bochonki()
        assert set(res_a) == set(res_b)

class TestBarrels():

    # выполняется в каждой последующей функции
    def setup(self):
        self.a = loto_classes.Barrels()

    #проверка функции генерации бочонков
    def test_bochonki(self):
        assert len(self.a.bochonki()) == 90

    #     #????????????
    # #ошибки pytest.raises
    # def test_bochonki_exception(self):
    #     with pytest.raises(Exception):
    #         assert len(self.a) == 91

    def test_str(self):
        self.a = loto_classes.Barrels()
        assert str(self.a) == 'количсечтво бочонков в мешке в начале игры = 90'

    def test_len(self):
        self.a = loto_classes.Barrels()
        assert len(self.a.bochonki()) == 90
    
    def test_eq(self):
        a = loto_classes.Barrels()
        b = loto_classes.Barrels()
        res_a = a.bochonki()
        res_b = b.bochonki()
        assert set(res_a) == set(res_b)

class TestPlayers():

    def test_create_card_player_1(self):
        self.user = loto_classes.Players()
        self.user = self.user.create_card()
        assert len(set(self.user)) == 16

    def test_create_card_player_2(self):
        self.user = loto_classes.Players()
        self.user = self.user.create_card()
        assert len(self.user) == 27

    def test_str(self):
        self.player = loto_classes.Players()
        assert str(self.player) == 'Имя игрока: игрок, имя компьтера: комп'