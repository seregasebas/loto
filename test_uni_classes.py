import unittest
import loto_classes

# Для запуска через терминал
#python3 test_uni_classes.py -v

class Test_Lotto_Cards(unittest.TestCase):

    def setUp(self):
        self.a = loto_classes.Lotto_cards()

    #проверка функции генерации карты
    def test_create_card(self):
        self.assertEqual(len(self.a.create_card()), 27)

    #проверка функции генерации карты
    def test_create_card_set(self):
        self.assertEqual(len(set(self.a.create_card())), 16)

class Test_Barrels(unittest.TestCase):

    # выполняется в каждой последующей функции
    def setUp(self):
        self.a = loto_classes.Barrels()

    #проверка функции генерации бочонков
    def test_bochonki(self):
        self.assertEqual(len(self.a.bochonki()), 90)

class TestPlayers(unittest.TestCase):

    def test_create_card_player_1(self):
        self.user = loto_classes.Players()
        self.user = self.user.create_card()
        self.assertEqual(len(set(self.user)), 16)

    def test_create_card_player_2(self):
        self.user = loto_classes.Players()
        self.user = self.user.create_card()
        self.assertEqual(len(self.user), 27)

if __name__ == '__main__':
    unittest.main()