import unittest
from itertools import combinations
from last_digit_of_partial_sum_of_fibonacci_number import last_digit_of_partial_sum_of_fibonacci_numbers_naive, last_digit_of_partial_sum_of_fibonacci_numbers_fast

class TestLastDigitOfPartialSumOfFibonacciNumbers(unittest.TestCase):

    def test_small(self):
        for start, end in combinations(range(2, 15), 2):
            self.assertEqual(last_digit_of_partial_sum_of_fibonacci_numbers_naive(start, end), 
            last_digit_of_partial_sum_of_fibonacci_numbers_fast(start, end))

    def test_large(self):
        for (start, end, last_digit) in [(3, 7, 1), (10, 10, 5), (100, 200, 0),(17, 1700, 7),(19, 10000000000, 1)]:
            self.assertEqual(last_digit_of_partial_sum_of_fibonacci_numbers_fast(start, end), last_digit)

if __name__ == "__main__":
    unittest.main()