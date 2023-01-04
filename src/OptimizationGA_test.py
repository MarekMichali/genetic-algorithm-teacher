import unittest
from src.OptimizationGA import OptimizationGA


class MyTestCase(unittest.TestCase):
    def test_bad_parameter(self):
        """
            Sprawdza poprawność walidacji dla przykładu suzkania wartośći argumentów
        """
        optimization_ga = OptimizationGA(num_parents_mating=5, sol_per_pop=4)
        x, y, z = optimization_ga.start()
        self.assertEqual(x[0], -1)
        self.assertEqual(y[0], -1)
        self.assertEqual(z[0], -1)


if __name__ == '__main__':
    unittest.main()
