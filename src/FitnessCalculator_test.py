import unittest
import numpy as np
from FitnessCalculator import FitnessCalculator


class MyTestCase(unittest.TestCase):
    def test_optimization_success(self):
        """
            Sprawdza poprawność działania funkcji oceny dla przykładu szukania wartośći argumentów
        """
        fitness_calculator = FitnessCalculator([1, 1])
        result = fitness_calculator.optimization(np.array([10, 90]))
        self.assertEqual(0.0099999999, result)

    def test_optimization_max_value(self):
        """
            Sprawdza poprawność działania funkcji oceny dla przykładu szukania wartośći argumentów dla maksymalnej wartości
        """
        fitness_calculator = FitnessCalculator([1, -1])
        result = fitness_calculator.optimization(np.array([10, 10]))
        self.assertEqual(1000000, result)

    def test_evolve_ones(self):
        """
            Sprawdza poprawność działania funkcji oceny dla przykładu ewolucji szczurów
        """
        fitness_calculator = FitnessCalculator([1, 1, 1])
        result = fitness_calculator.evolve_ones(np.array([1, 1, 1]))
        self.assertEqual(3, result)

    def test_tsp(self):
        """
            Sprawdza poprawność działania funkcji oceny dla przykładu problemu komiwojażera
        """
        fitness_calculator = FitnessCalculator()
        result = fitness_calculator.tsp(np.array([1, 2]), [1, 2], [1, 2])
        self.assertGreater(0, result)


if __name__ == '__main__':
    unittest.main()
