import pygad
from FitnessCalculator import FitnessCalculator


class EvolveOnesGA:
    def __init__(self, num_generations=0, num_parents_mating=0, mut_prop=0, sol_per_pop=0, function_inputs=None):
        self.num_generations = num_generations
        self.num_parents_mating = num_parents_mating
        self.mut_prop = mut_prop
        self.sol_per_pop = sol_per_pop
        self.function_inputs = function_inputs

    def start(self):
        if self.num_parents_mating > self.sol_per_pop:
            return [-1], [-1], [-1]

        fitness_calculator = FitnessCalculator(self.function_inputs)
        num_genes = len(self.function_inputs)

        ga_instance = pygad.GA(num_generations=self.num_generations,
                               num_parents_mating=self.num_parents_mating,
                               fitness_func=lambda solution, solution_idx: fitness_calculator.evolve_ones(solution),
                               sol_per_pop=self.sol_per_pop,
                               num_genes=num_genes,
                               gene_type=int,
                               gene_space=[0, 1],
                               mutation_probability=self.mut_prop)

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()

        return solution, solution_fitness, ga_instance.best_solutions_fitness
