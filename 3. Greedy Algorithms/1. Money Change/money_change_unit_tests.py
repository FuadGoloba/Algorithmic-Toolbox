import unittest
from money_change import money_change

class TestMoneyChange(unittest.TestCase):

    def test(self):
        for (money, num_of_coins) in [(2,2), (25, 3), (28, 6), (1, 1)]:
            self.assertEqual(money_change(money), num_of_coins)

if __name__ == '__main__':
    unittest.main()