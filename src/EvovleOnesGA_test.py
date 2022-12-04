import unittest
from EvovleOnesGA import EvolveOnesGA


class MyTestCase(unittest.TestCase):
    def test_bad_parameter(self):
        evolve_ones_ga = EvolveOnesGA(num_parents_mating=5, sol_per_pop=4)
        x, y, z = evolve_ones_ga.start()
        self.assertEqual(x[0], -1)
        self.assertEqual(y[0], -1)
        self.assertEqual(z[0], -1)


if __name__ == '__main__':
    unittest.main()
