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

    def test_str(self):
        self.card = loto_classes.Lotto_cards()
        self.assertEqual(str(self.card), 'create_card(self) создает карту игрока(компа), show_card(self, card, name) выводит карту')

    def test_eq(self):
        a = loto_classes.Barrels()
        b = loto_classes.Barrels()
        res_a = a.bochonki()
        res_b = b.bochonki()
        self.assertEqual(set(res_a), set(res_b))
        
class Test_Barrels(unittest.TestCase):

    # выполняется в каждой последующей функции
    def setUp(self):
        self.a = loto_classes.Barrels()

    #проверка функции генерации бочонков
    def test_bochonki(self):
        self.assertEqual(len(self.a.bochonki()), 90)

    def test_str(self):
        self.a = loto_classes.Barrels()
        self.assertEqual(str(self.a), 'количсечтво бочонков в мешке в начале игры = 90')

    def test_len(self):
        self.a = loto_classes.Barrels()
        self.assertEqual(len(self.a.bochonki()), 90)
    
    def test_eq(self):
        a = loto_classes.Barrels()
        b = loto_classes.Barrels()
        res_a = a.bochonki()
        res_b = b.bochonki()
        self.assertEqual(set(res_a), set(res_b))

class TestPlayers(unittest.TestCase):

    def test_create_card_player_1(self):
        self.user = loto_classes.Players()
        self.user = self.user.create_card()
        self.assertEqual(len(set(self.user)), 16)

    def test_create_card_player_2(self):
        self.user = loto_classes.Players()
        self.user = self.user.create_card()
        self.assertEqual(len(self.user), 27)

    def test_str(self):
        self.player = loto_classes.Players()
        self.assertEqual(str(self.player), 'Имя игрока: игрок, имя компьтера: комп')

if __name__ == '__main__':
    unittest.main()