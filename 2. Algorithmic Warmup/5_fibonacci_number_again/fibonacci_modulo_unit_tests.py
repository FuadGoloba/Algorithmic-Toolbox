import unittest
from itertools import product
from fibonacci_modulo import fibonacci_nth_modulo_naive, fibonacci_nth_modulo_fast

class TestFibonacciModulo(unittest.TestCase):
    
    def test_small():
        for n, m in product(range(2, 15), repeat=2):
            self.assertEqual(fibonacci_nth_modulo_naive(n, m), fibonacci_nth_modulo_fast(n, m))

    def test_large():
        for n, m, res in [((115, 1000, 885), (2816213588, 239, 151))]:
            self.assertEqual(fibonacci_nth_modulo_fast(n, m), res)

if __name__ == '__main__':
    unittest.main()