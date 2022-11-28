import dearpygui.dearpygui as dpg
import numpy
import time

import config
import pygad


class EvolveOnes:
    def __init__(self):
        with dpg.window(label="Krzyzowanie", autosize=True, tag="evolveOnes", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("evolveOnes")
            with dpg.table(width=1440, height=640, header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_input_int(label="Po ilu generacjach zatrzymac algorytm", tag="NoGe", default_value=100)
                        dpg.add_input_int(label="Ilu rodzicow wybrac dla nowej populacji", tag="NoPe", default_value=7)
                        dpg.add_button(label="Execute", callback=self.start)




    def start(self):
        """
        Given the following function:
            y = f(w1:w6) = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + 6wx6
            where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7) and y=44
        What are the best values for the 6 weights (w1 to w6)? We are going to use the genetic algorithm to optimize this function.
        """

        function_inputs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # Function inputs.

        def fitness_func(solution, solution_idx):
            # Calculating the fitness value of each solution in the current population.
            # The fitness function calulates the sum of products between each input and its corresponding weight.
            fitness = numpy.sum(solution * function_inputs)
            print(solution_idx, solution, fitness)
            return fitness

        fitness_function = fitness_func
        num_generations = dpg.get_value("NoGe")  # Number of generations.
        num_parents_mating = dpg.get_value("NoPe")  # Number of solutions to be selected as parents in the mating pool.

        # To prepare the initial population, there are 2 ways:
        # 1) Prepare it yourself and pass it to the initial_population parameter. This way is useful when the user wants to start the genetic algorithm with a custom initial population.
        # 2) Assign valid integer values to the sol_per_pop and num_genes parameters. If the initial_population parameter exists, then the sol_per_pop and num_genes parameters are useless.
        sol_per_pop = 4  # Number of solutions in the population.
        num_genes = len(function_inputs)

        self.last_fitness = 0

        def callback_generation(ga_instance):
           # global last_fitness
            print("Generation = {generation}".format(generation=ga_instance.generations_completed))
            print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))
            print("Change     = {change}".format(change=ga_instance.best_solution()[1] - self.last_fitness))
            self.last_fitness = ga_instance.best_solution()[1]

        # Creating an instance of the GA class inside the ga module. Some parameters are initialized within the constructor.
        ga_instance = pygad.GA(num_generations=num_generations,
                               num_parents_mating=num_parents_mating,
                               fitness_func=fitness_function,
                               sol_per_pop=sol_per_pop,
                               num_genes=num_genes,
                               on_generation=callback_generation,
                               gene_type=int,
                               init_range_low=0,
                               init_range_high=2
                              )

        # Running the GA to optimize the parameters of the function.
        ga_instance.run()
        # After the generations complete, some plots are showed that summarize the how the outputs/fitenss values evolve over generations.
        #ga_instance.plot_fitness()

        # Returning the details of the best solution.
        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        print("Parameters of the best solution : {solution}".format(solution=solution))
        print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
        print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

        prediction = numpy.sum(numpy.array(function_inputs) * solution)
        print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

        if ga_instance.best_solution_generation != -1:
            print("Best fitness value reached after {best_solution_generation} generations.".format(
                best_solution_generation=ga_instance.best_solution_generation))

        # Saving the GA instance.
       # filename = 'genetic'  # The filename to which the instance is saved. The name is without extension.
        #ga_instance.save(filename=filename)
        self.show_info("Rozwiazanie", solution, self.on_selection)
        # Loading the saved GA instance.
        #loaded_ga_instance = pygad.load(filename=filename)
       # loaded_ga_instance.plot_fitness()
    def show_info(self, title, message, selection_callback):
        # guarantee these commands happen in the same frame
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()

            with dpg.window(label=title, modal=True, no_close=True, autosize=True, tag="gggg", pos=(9999,9999)) as modal_id:
                dpg.add_text(message)
                dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=selection_callback)
                dpg.add_button(label="Cancel", width=75, user_data=(modal_id, False), callback=selection_callback)

        # guarantee these commands happen in another frame
        dpg.split_frame()
        width = dpg.get_item_width(modal_id)
        height = dpg.get_item_height(modal_id)
        dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])

    def on_selection(self, sender, unused, user_data):
        dpg.delete_item(user_data[0])