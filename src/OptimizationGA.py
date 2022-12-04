import numpy
import pygad


class OptimizationGA:
    def __init__(self, num_generations, num_parents_mating, mut_prop, sol_per_pop, function_inputs, result):
        self.num_generations = num_generations
        self.num_parents_mating = num_parents_mating
        self.mut_prop = mut_prop
        self.sol_per_pop = sol_per_pop
        self.function_inputs = function_inputs
        self.result = result

    def start(self):
        if self.num_parents_mating > self.sol_per_pop:
            return [-1], [-1], [-1]

        def fitness_func(solution, solution_idx):
            output = numpy.sum(solution * self.function_inputs)
            fitness = 1.0 / numpy.abs(output - self.result)
            return fitness

        fitness_function = fitness_func
        num_genes = len(self.function_inputs)

        ga_instance = pygad.GA(num_generations=self.num_generations,
                               num_parents_mating=self.num_parents_mating,
                               fitness_func=fitness_function,
                               sol_per_pop=self.sol_per_pop,
                               num_genes=num_genes,
                               mutation_probability=self.mut_prop)

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()

        return solution, solution_fitness, ga_instance.best_solutions_fitness

