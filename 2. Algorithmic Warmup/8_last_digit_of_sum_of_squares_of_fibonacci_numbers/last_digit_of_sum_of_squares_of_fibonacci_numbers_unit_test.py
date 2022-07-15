from last_digit_of_sum_of_squares_of_fibonacci_numbers, import last_digit_of_sum_of_squares_of_fibonacci_numbers_naive, last_digit_of_sum_of_squares_of_fibonacci_numbers_fast
import unittest

class TestLastDigitOfSumOfSquaresOfFibonacciNumbers(unittest.TestCase):

    def test_small(self):
        for n in range(25):
            self.assertEqual(last_digit_of_sum_of_squares_of_fibonacci_numbers_fast(n), last_digit_of_sum_of_squares_of_fibonacci_numbers_naive(n))

    def test_large(self):
        for (n, result) in [(73, 1), (1234567890, 0)]:
            self.assertEqual(last_digit_of_sum_of_squares_of_fibonacci_numbers_fast(n), result)


if __name__ == "__main__":
    unittest.main()