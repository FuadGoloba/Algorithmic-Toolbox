# Implementing a unit test to stress test algorithms

import unittest
from fibonacci_number_last_digit import fib_last_digit_naive, fib_last_digit_fast

class TestLastDigitofFibonacciNumber(unittest.TestCase):
    
    def test_small(self):
        for n in range(20):
            self.assertEqual(fib_last_digit_naive(n), fib_last_digit_fast(n))
            
            
    def test_large(self):
       for (n, last_digit) in [(100, 5), (139, 1), (91239, 6), (500, 5)]:
           self.assertEqual(fib_last_digit_fast(n), last_digit)
           
if __name__ == "__main__":
    unittest.main()