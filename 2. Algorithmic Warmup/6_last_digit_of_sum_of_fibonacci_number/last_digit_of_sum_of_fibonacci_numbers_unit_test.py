import unittest
from last_digit_of_sum_of_fibonacci_numbers import last_digit_of_sum_of_fibonacci_numbers_fast, last_digit_of_sum_of_fibonacci_numbers_naive


class TestLastDigitOfSumOfFibonacciNumbers(unittest.TestCase):
    def test_small(self):
        for n in range(20):
            self.assertEqual(last_digit_of_sum_of_fibonacci_numbers_naive(n), last_digit_of_sum_of_fibonacci_numbers_fast(n))

    def test_large(self):
        for (n, r) in [(100, 5),(2560,5)]:
            self.assertEqual(last_digit_of_sum_of_fibonacci_numbers_fast(n), r)

if __name__ == "__main__":
    unittest.main()
