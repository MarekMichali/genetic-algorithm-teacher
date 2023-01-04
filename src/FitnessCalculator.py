import numpy


class FitnessCalculator:
    """
        Klasa odpowiedzialna za obliczanie jakości rozwiązań w algorytmie genetycznym
    """
    def __init__(self, function_inputs=0, result=0):
        self.function_inputs = function_inputs
        self.result = result

    def optimization(self, solution):
        """
            Oblicza jakość rozwiązania w przykładzie szukania wartośći argumentów
        :param solution: rozwiązanie
        :return: jakość rozwiązania
        """
        output = numpy.sum(solution * self.function_inputs)
        div = numpy.abs(output - self.result)
        fitness = 1.0 / (div + 0.000001)
        return fitness

    def evolve_ones(self, solution):
        """
            Oblicza jakość rozwiązania w przykładzie ewolucji szczurów
        :param solution: rozwiązanie
        :return: jakość rozwiązania
        """
        fitness = numpy.sum(solution * self.function_inputs)
        return fitness

    def tsp(self, solution, x_location, y_location):
        """

        :param solution: rozwiązanie
        :param x_location: współrzędne x miast
        :param y_location: współrzędne y miast
        :return: jakość rozwiązania
        """
        total_length = 0
        i = 0
        for loc in solution:
            if i == 0:
                city_one = loc - 1
                city_two = solution[len(solution) - 1] - 1
                total_length += ((x_location[city_one] - x_location[city_two]) ** 2
                                 + (y_location[city_one] - y_location[city_two]) ** 2) ** (1 / 2)
            else:
                city_one = loc - 1
                city_two = solution[i - 1] - 1
                total_length += ((x_location[city_one] - x_location[city_two]) ** 2
                                 + (y_location[city_one] - y_location[city_two]) ** 2) ** (1 / 2)
            i += 1
        return total_length * -1
