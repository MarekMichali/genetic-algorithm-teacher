import unittest
from src.TspGA import TspGA


class MyTestCase(unittest.TestCase):
    def test_bad_parameter(self):
        """
            Sprawdza poprawność walidacji dla przykładu problemu komiwojażera
        """
        tsp_ha = TspGA(num_parents_mating=5, sol_per_pop=4)
        x, y, z = tsp_ha.start()
        self.assertEqual(x[0], -1)
        self.assertEqual(y[0], -1)
        self.assertEqual(z[0], -1)


if __name__ == '__main__':
    unittest.main()
