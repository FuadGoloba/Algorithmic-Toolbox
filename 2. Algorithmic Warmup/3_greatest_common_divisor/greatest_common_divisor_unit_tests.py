import unittest
from greatest_common_divisor import gcd_naive, gcd_fast

class TestGCD(unittest.TestCase):
    
    def test_small(self):
        for (a, b) in [(1, 2), (12, 8), (6, 30)]:
            self.assertEqual(gcd_naive(a,b), gcd_fast(a,b))
            
    def test_large(self):
        for (a, b, d) in [(28851538, 1183019, 17657), (286480, 2568, 8)]:
            self.assertEqual(gcd_fast(a,b), d)
            
if __name__ == "__main__":
    unittest.main()