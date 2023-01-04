import numpy
import pygad
from FitnessCalculator import FitnessCalculator


class TspGA:
    """
        Klasa odpowiedzialna za wykonanie przykładowego zadania problemu komiwojażera
    """
    def __init__(self, num_generations=0, num_parents_mating=0, sol_per_pop=0, x_location=0, y_location=0):
        """
            :param num_generations: liczba generacji
            :param num_parents_mating: liczba rodzicow
            :param sol_per_pop: liczba osobnikow
            :param x_location: współrzędne x miast
            :param y_location: współrzędne y miast
        """
        self.num_generations = num_generations
        self.num_parents_mating = num_parents_mating
        self.sol_per_pop = sol_per_pop
        self.x_location = x_location
        self.y_location = y_location

    def start(self):
        """
            Rozpoczyna działanie algorytmu genetycznego
        :return: - najlepsze rozwiązanie w aktualnej populacji,
                 - jakość najlepszego rozwiązania,
                 - najlepsze rozwiązanie
        """
        if self.num_parents_mating > self.sol_per_pop:
            return [-1], [-1], [-1]

        fitness_calculator = FitnessCalculator()
        population_list = []
        gene_space = [i for i in range(1, 13)]
        for i in range(self.sol_per_pop):
            nxm_random_num = list(numpy.random.permutation(gene_space))
            population_list.append(nxm_random_num)

        num_genes = len(gene_space)

        ga_instance = pygad.GA(num_generations=self.num_generations,
                               num_parents_mating=self.num_parents_mating,
                               initial_population=population_list,
                               fitness_func=lambda solution, solution_idx:
                               fitness_calculator.tsp(solution, self.x_location, self.y_location),
                               sol_per_pop=self.sol_per_pop,
                               num_genes=num_genes,
                               gene_type=int,
                               gene_space=gene_space,
                               allow_duplicate_genes=False)

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()

        return solution, solution_fitness, ga_instance.best_solutions_fitness
