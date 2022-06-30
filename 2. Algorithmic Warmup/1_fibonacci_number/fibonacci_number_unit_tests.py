# Unit test to test and stress test solution of fibonaci
import unittest
from fibonacci_number import fibonacci_number_naive, fibonacci_number

class TestFibonacciNumber(unittest.TestCase):
    
    # Stress testing on a small dataset
    def test_small(self):
        for n in range(8):
            self.assertEqual(fibonacci_number(n), fibonacci_number_naive(n))
            
    # testing ob a large dataset
    def test_large(self):
        for (n, Fn) in [(30, 832040), (35, 9227465), (40, 102334155)]:
            self.assertEqual(fibonacci_number(n), Fn)
            
            
if __name__ == "__main__":
    unittest.main()