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

class TestBarrels():

    # выполняется в каждой последующей функции
    def setup(self):
        self.a = loto_classes.Barrels.bochonki()

    #проверка функции генерации бочонков
    def test_bochonki(self):
        assert len(self.a) == 90

        #????????????
    #ошибки pytest.raises
    def test_bochonki_exception(self):
        with pytest.raises(Exception):
            assert len(self.a) == 91

class TestPlayers():

    def test_start_card_user(self):
        self.user = loto_classes.Lotto_cards.create_card()
        assert len(set(self.user)) == 16

    def test_start_card_comp(self):
        self.computer = loto_classes.Lotto_cards.create_card()
        assert len(self.computer) == 27