import numpy
import pygad


class TspGA:
    def __init__(self, num_generations, num_parents_mating, sol_per_pop, x_location, y_location):
        self.num_generations = num_generations
        self.num_parents_mating = num_parents_mating
        self.sol_per_pop = sol_per_pop
        self.x_location = x_location
        self.y_location = y_location

    def start(self):
        if self.num_parents_mating > self.sol_per_pop:
            return [-1], [-1], [-1]

        def fitness_func(solution, solution_idx):
            total_length = 0
            i = 0
            for loc in solution:
                if i == 0:
                    city_one = loc - 1
                    city_two = solution[len(solution) - 1] - 1
                    total_length += ((self.x_location[city_one] - self.x_location[city_two]) ** 2
                                     + (self.y_location[city_one] - self.y_location[city_two]) ** 2) ** (1 / 2)
                else:
                    city_one = loc - 1
                    city_two = solution[i - 1] - 1
                    total_length += ((self.x_location[city_one] - self.x_location[city_two]) ** 2
                                     + (self.y_location[city_one] - self.y_location[city_two]) ** 2) ** (1 / 2)
                i += 1
            return total_length * -1

        population_list = []
        gene_space = [i for i in range(1, 13)]
        for i in range(self.sol_per_pop):
            nxm_random_num = list(numpy.random.permutation(gene_space))
            population_list.append(nxm_random_num)

        fitness_function = fitness_func
        num_genes = len(gene_space)

        ga_instance = pygad.GA(num_generations=self.num_generations,
                               num_parents_mating=self.num_parents_mating,
                               initial_population=population_list,
                               fitness_func=fitness_function,
                               sol_per_pop=self.sol_per_pop,
                               num_genes=num_genes,
                               gene_type=int,
                               gene_space=gene_space,
                               allow_duplicate_genes=False)

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()

        return solution, solution_fitness, ga_instance.best_solutions_fitness
