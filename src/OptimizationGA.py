import pygad
from FitnessCalculator import FitnessCalculator


class OptimizationGA:
    """
        Klasa odpowiedzialna za wykonanie przykładowego zadania szukania wartośći argumentów
    """
    def __init__(self, num_generations=0, num_parents_mating=0, mut_prop=0, sol_per_pop=0,
                 function_inputs=None, result=0):
        """
            :param num_generations: liczba generacji
            :param num_parents_mating: liczba rodzicow
            :param mut_prop: prawdopodobienstwo mutacji
            :param sol_per_pop: liczba osobnikow
            :param function_inputs: funkcja oceny
            :param result: oczekiwany wynik
        """
        self.num_generations = num_generations
        self.num_parents_mating = num_parents_mating
        self.mut_prop = mut_prop
        self.sol_per_pop = sol_per_pop
        self.function_inputs = function_inputs
        self.result = result

    def start(self):
        """
            Rozpoczyna działanie algorytmu genetycznego
        :return: - najlepsze rozwiązanie w aktualnej populacji,
                 - jakość najlepszego rozwiązania,
                 - najlepsze rozwiązanie
        """
        if self.num_parents_mating > self.sol_per_pop:
            return [-1], [-1], [-1]

        fitness_calculator = FitnessCalculator(self.function_inputs, self.result)
        num_genes = len(self.function_inputs)

        ga_instance = pygad.GA(num_generations=self.num_generations,
                               num_parents_mating=self.num_parents_mating,
                               fitness_func=lambda solution, solution_idx: fitness_calculator.optimization(solution),
                               sol_per_pop=self.sol_per_pop,
                               num_genes=num_genes,
                               mutation_probability=self.mut_prop)

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()

        return solution, solution_fitness, ga_instance.best_solutions_fitness
