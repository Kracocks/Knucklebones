import unittest
from knucklebones import Player

class TestStringMethods(unittest.TestCase):
    
    def test_get_ranged_value(self):
        player_test = Player()
        ennemy_test= Player()
        self.assertEqual(player_test.get_column_value(0), 0)
        player_test.put_value(ennemy_test,0,4)
        self.assertEqual(player_test.get_column_value(0), 4)
        player_test.put_value(ennemy_test,0,4)
        self.assertEqual(player_test.get_column_value(0), 16)
        player_test.put_value(ennemy_test,0,4)
        self.assertEqual(player_test.get_column_value(0), 36)
        
    def test_put_value(self):
        player_test = Player()
        ennemy_test = Player()
        self.assertEqual(player_test.put_value(ennemy_test, 2, 4), True)
        player_test.put_value(ennemy_test, 1, 4)
        player_test.put_value(ennemy_test, 1, 4)
        player_test.put_value(ennemy_test, 1, 4)
        self.assertEqual(player_test.put_value(ennemy_test, 1, 4), False)
        
    def test_remove_value(self):
        player_test = Player()
        ennemy_test = Player()
        player_test.put_value(ennemy_test, 0, 5)
        player_test.put_value(ennemy_test, 0, 1)
        player_test.put_value(ennemy_test, 0, 1)
        player_test.remove_values(0, 5)
        self.assertEqual(player_test.get_column(0), [1, 1, 0])
        
    def test_calc_total(self):
        player_test = Player()
        ennemy_test = Player()
        player_test.put_value(ennemy_test, 0, 6)
        player_test.calc_total()
        self.assertEqual(player_test.total_value, 6)
        player_test.put_value(ennemy_test, 1, 6)
        player_test.calc_total()
        self.assertEqual(player_test.total_value, 12)
        player_test.put_value(ennemy_test, 0, 6)
        player_test.calc_total()
        self.assertEqual(player_test.total_value, 30)
        player_test.put_value(ennemy_test, 0, 6)
        player_test.calc_total()
        self.assertEqual(player_test.total_value, 60)
        
    def test_winning(self):
        player_test = Player()
        ennemy_test = Player()
        player_test.put_value(ennemy_test,0,1)
        player_test.put_value(ennemy_test,0,1)
        player_test.put_value(ennemy_test,0,1)
        player_test.put_value(ennemy_test,1,1)
        player_test.put_value(ennemy_test,1,1)
        player_test.put_value(ennemy_test,1,1)
        player_test.put_value(ennemy_test,2,1)
        player_test.put_value(ennemy_test,2,1)
        player_test.put_value(ennemy_test,2,1)
        self.assertEqual(player_test.has_finished(), True)
        self.assertEqual(ennemy_test.has_finished(), False)

if __name__ == '__main__':
    unittest.main()