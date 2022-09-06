import unittest
from car_fueling import compute_min_number_of_refills


class CarFuelingTest(unittest.TestCase):

    def test(self):
        for (distance, miles, gasStations, answer) in [
            (950, 400, [200, 350, 550, 750], 2),
            (10, 3, [1, 2, 5, 9], -1),
            (200, 250, [100, 150], 0)]:

                self.assertEqual(compute_min_number_of_refills(distance, miles, gasStations), answer)


if __name__ == '__main__':
    unittest.main()
