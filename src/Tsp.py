from math import sin, cos

import dearpygui.dearpygui as dpg
import numpy
import time

import config
import pygad


class Tsp:
    def __init__(self):
        self.color = (15, 86, 135, 255)
        self.checkboxes = []
        self.yOffset = 100
        self.xOneOffset = 5
        self.firstChromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)

        self.xLocation = [8, 50, 18, 35, 90, 40, 84, 74, 34, 40, 60, 74]
        self.yLocation = [3, 62, 20, 25, 89, 71, 7, 29, 45, 65, 69, 47]

        with dpg.window(label="tsp", autosize=True, tag="tsp", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("evolveOnes")
            with dpg.table(width=820, height=310, header_row=False):
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        dpg.add_text("Zadanie omawiane w prezentacji.", indent=240)
                        dpg.add_text("Pozwala sprawdzic jaki wplyw na przebieg ewolucji maja poszczegolne parametry.", indent=20)
                        dpg.add_spacer(height=20)
                        dpg.add_input_int(label=" Liczba generacji do zatrzymania ewolucji", tag="NoGt", default_value=100, width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba osobnikow w generacji", tag="NoOt", default_value=20,
                                          width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba rodzicow wybranych dla nowej populacji", tag="NoPt", default_value=6, width=140, min_value=2, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Procentowe prawdopodobienstwo mutacji", tag="MutProbt", default_value=1,
                                          width=140, min_value=0, min_clamped=True, max_value=100, max_clamped=True, indent=140)
                        dpg.add_spacer(height=20)
                        dpg.add_button(label="Wykonaj", callback=self.start, indent=340)

    def start(self):
        function_inputs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # Function inputs.
       # [7  8 12  6 10  4  3  1  9  2 11  5]
        def fitness_func(solution, solution_idx):
            total_length = 0
            i = 0
            print("solution", solution)
            for loc in solution:
                if i == 0:
                    print("loc: ", loc, solution[len(solution) - 1])
                    cityOne = loc - 1
                    cityTwo = solution[len(solution) - 1] - 1
                    total_length += ((self.xLocation[cityOne] - self.xLocation[cityTwo]) ** 2 + (self.yLocation[cityOne] - self.yLocation[cityTwo]) ** 2) ** (1 / 2)
                else:
                    cityOne = loc - 1
                    cityTwo = solution[i - 1] - 1
                    total_length += ((self.xLocation[cityOne] - self.xLocation[cityTwo]) ** 2 + (self.yLocation[cityOne] - self.yLocation[cityTwo]) ** 2) ** (1 / 2)



                i += 1
            return total_length * -1

        fitness_function = fitness_func
        num_generations = dpg.get_value("NoGt")  # Number of generations.
        num_parents_mating = dpg.get_value("NoPt")  # Number of solutions to be selected as parents in the mating pool.
        mut_prop = dpg.get_value("MutProbt")/100.0

        # To prepare the initial population, there are 2 ways:
        # 1) Prepare it yourself and pass it to the initial_population parameter. This way is useful when the user wants to start the genetic algorithm with a custom initial population.
        # 2) Assign valid integer values to the sol_per_pop and num_genes parameters. If the initial_population parameter exists, then the sol_per_pop and num_genes parameters are useless.
        sol_per_pop = dpg.get_value("NoOt")
        num_genes = len(self.xLocation)

        self.last_fitness = 0



        def callback_generation(ga_instance):
           # global last_fitness
            print("Generation = {generation}".format(generation=ga_instance.generations_completed))
            print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))
            print("Change     = {change}".format(change=ga_instance.best_solution()[1] - self.last_fitness))
            self.last_fitness = ga_instance.best_solution()[1]

        gene_space = [i for i in range(1, 13)]
        population_list = []
        for i in range(sol_per_pop):
            nxm_random_num = list(numpy.random.permutation(gene_space))
            population_list.append(nxm_random_num)  # add to the population_list
        # Creating an instance of the GA class inside the ga module. Some parameters are initialized within the constructor.
        ga_instance = pygad.GA(num_generations=num_generations,
                               num_parents_mating=num_parents_mating,
                               initial_population=population_list,
                               fitness_func=fitness_function,
                               sol_per_pop=sol_per_pop,
                               num_genes=num_genes,
                               #on_generation=callback_generation,

                               gene_type=int,
                             #  mutation_type="swap",

                               gene_space=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                               #mutation_probability=mut_prop,

                               allow_duplicate_genes=False
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
        #ga_instance.plot_fitness()
        # Saving the GA instance.
       # filename = 'genetic'  # The filename to which the instance is saved. The name is without extension.
        #ga_instance.save(filename=filename)
        self.show_info("Rozwiazanie", solution, self.on_selection, ga_instance.best_solutions_fitness)

  #      cosdatax = []
   #     cosdatay = []
    #    for i in range(0, 500):
     #       cosdatax.append(i / 1000)
      #      cosdatay.append(0.5 + 0.5 * cos(50 * i / 1000))

       # dpg.set_value('series_tag', [list(range(0,101)), ga_instance.best_solutions_fitness])
        #dpg.set_item_label('series_tag', "0.5 + 0.5 * cos(x)")
        # Loading the saved GA instance.
        #loaded_ga_instance = pygad.load(filename=filename)
       # loaded_ga_instance.plot_fitness()
    def show_info(self, title, message, selection_callback, best_sols):
        # guarantee these commands happen in the same frame
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()

            with dpg.window(label=title, modal=True, no_close=True, autosize=True, tag="ggggt", pos=(9999,9999)) as modal_id:

        #        with dpg.plot(label="Jakosc rozwiazania w zaleznosci od generacji", width=1440, height=400, track_offset=5.0):
                    # optionally create legend
         #           dpg.add_plot_legend()

                    # REQUIRED: create x and y axes
        #            dpg.add_plot_axis(dpg.mvXAxis, label="Generacja")
         #           dpg.add_plot_axis(dpg.mvYAxis, label="Jakosc", tag="y_axis2t")

                    # series belong to a y axis
          #          dpg.add_line_series(list(range(0,101)), best_sols, label="0.5 + 0.5 * sin(x)", parent="y_axis2t",
           #                             tag="series_tag2t")


                dpg.add_spacer(height=20)
                dpg.add_text("Otrzymane rozwiazanie", indent=620)
                dpg.add_spacer(height=10)
                with dpg.drawlist(width=1440, height=500):
                    with dpg.draw_layer():
                     #   dpg.draw_line((418, 5), (1023, 5), color=self.color, thickness=5)
                       # dpg.draw_line((48, 50), (653, 50), color=self.color, thickness=5)
                      #  dpg.draw_line((420, 5), (420, 58), color=self.color, thickness=5)
                       # dpg.draw_line((420, 55), (1023, 55), color=self.color, thickness=5)
                        #dpg.draw_line((50, 100), (653, 100), color=self.color, thickness=5)
                        j = 0
                        for i in self.xLocation:
                            dpg.draw_circle((i, self.yLocation[j]), radius=2, color=self.color, fill=self.color)
                            j += 1
                        for i in message:
                            dpg.draw_line((418, 5), (1023, 5), color=self.color, thickness=1)

                        i = 0

                        for loc in message:

                            if i == 0:
                                print("loc: ", loc, message[len(message) - 1])
                                cityidx1 = loc - 1
                                cityidx2 = message[len(message) - 1] - 1
                                dpg.draw_line((self.xLocation[cityidx1], self.yLocation[cityidx1]),
                                              (self.xLocation[cityidx2], self.yLocation[cityidx2]), color=self.color, thickness=1)
                            else:
                                cityidx1 = loc - 1
                                cityidx2 = message[i - 1] - 1
                                dpg.draw_line((self.xLocation[cityidx1], self.yLocation[cityidx1]), (self.xLocation[cityidx2], self.yLocation[cityidx2]), color=self.color, thickness=1)

                            i += 1




                with dpg.group(horizontal=True):
                    dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=selection_callback, indent=685)
                  #  dpg.add_button(label="Cancel", width=75, user_data=(modal_id, False), callback=selection_callback)
        # guarantee these commands happen in another frame
        dpg.split_frame()
        width = dpg.get_item_width(modal_id)
        height = dpg.get_item_height(modal_id)
        dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])

    def on_selection(self, sender, unused, user_data):
        dpg.delete_item(user_data[0])