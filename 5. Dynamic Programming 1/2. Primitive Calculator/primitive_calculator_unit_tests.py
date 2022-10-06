import unittest
from primitive_calculator import DPprimitiveCalculator


class PrimitiveCalculator(unittest.TestCase):
    def test(self):
        for n, answer in ((2, 1), (3, 1), (5, 3), (96234, 14)):
            minimumOps = DPprimitiveCalculator(n)[0]
            sequence = DPprimitiveCalculator(n)[1]
            self.assertEqual(answer, minimumOps)
            self.assertEqual(sequence[0], 1)
            self.assertEqual(sequence[-1], n)
            for i in range(len(sequence) - 1):
                if sequence[i + 1] != sequence[i] + 1 and sequence[i + 1] != 2 * sequence[i]:
                    self.assertEqual(sequence[i + 1], 3 * sequence[i])


if __name__ == '__main__':
    unittest.main()
