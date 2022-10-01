import unittest
from DP_money_change import DPmoneyChange, DPmoneyChange_naive


class MoneyChangeAgain(unittest.TestCase):
    def test_small(self):
        for money in range(1, 40):
            self.assertEqual(DPmoneyChange(money, [1,3,4]), DPmoneyChange_naive(money))

    def test_large(self):
        for money, answer in ((200, 50), (239, 60)):
            self.assertEqual(DPmoneyChange(money,[1,3,4]), answer)


if __name__ == '__main__':
    unittest.main()
