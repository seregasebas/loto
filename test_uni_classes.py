import unittest
import loto_classes

# Для запуска через терминал
#python3 uni_test_classes.py -v

class Test_Lotto_Cards(unittest.TestCase):

    def setUp(self):
        self.a = loto_classes.Lotto_cards.create_card()

    #проверка функции генерации карты
    def test_create_card(self):
        self.assertEqual(len(self.a), 27)

    #проверка функции генерации карты
    def test_create_card_set(self):
        self.assertEqual(len(set(self.a)), 16)

class Test_Barrels(unittest.TestCase):

    # выполняется в каждой последующей функции
    def setUp(self):
        self.a = loto_classes.Barrels.bochonki()

    #проверка функции генерации бочонков
    def test_bochonki(self):
        self.assertEqual(len(self.a), 90)

class TestPlayers(unittest.TestCase):

    def test_start_card_user(self):
        self.user = loto_classes.Lotto_cards.create_card()
        self.assertEqual(len(set(self.user)), 16)

    def test_start_card_comp(self):
        self.computer = loto_classes.Lotto_cards.create_card()
        self.assertEqual(len(self.computer), 27)

if __name__ == '__main__':
    unittest.main()