import unittest
from itertools import product
from least_common_multiple import lcm_naive, lcm_fast

class TESTLCM(unittest.TestCase):
    
    def test_small(self):
        for (a, b) in product(range(1, 15), repeat = 2):
            self.assertEqual(lcm_naive(a, b), lcm_fast(a, b))
            
            
    def test_large(self):
        for (a, b , res) in [(28851538, 1183019, 1933053046), (547503463, 462892, 253434972994996)]:
            self.assertEqual(lcm_fast(a, b), res)
            
            
if __name__ == "__main__":
    unittest.main()