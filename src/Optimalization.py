from math import sin, cos

import dearpygui.dearpygui as dpg
import numpy
import time

import config
import pygad


class Optimalization:
    def __init__(self):
        self.prediction = 0
        self.color = (15, 86, 135, 255)
        self.checkboxes = []
        self.yOffset = 100
        self.xOneOffset = 5
        self.firstChromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.sindatax = []
        self.sindatay = []
        for i in range(0, 500):
            self.sindatax.append(i / 1000)
            self.sindatay.append(0.5 + 0.5 * sin(50 * i / 1000))
        with dpg.window(label="optimalization", autosize=True, tag="optimalization", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("optimalization")
            with dpg.table(width=820, height=310, header_row=False):
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)

                        dpg.add_text("Znajdowanie wartosci argumentow x, y, z", indent=220)
                        dpg.add_spacer(height=20)
                        with dpg.group(horizontal=True):

                            dpg.add_input_float(label="x", tag="inX", width=100, step=0, default_value=6, indent=170)
                            dpg.add_input_float(label="y", tag="inY", width=100, step=0, default_value=-18)
                            dpg.add_input_float(label="z", tag="inZ", width=100, step=0, default_value=49)
                            dpg.add_text("=")
                            dpg.add_input_float(tag="resultxyz", width=100, step=0, default_value=26)
                        dpg.add_spacer(height=20)
                        dpg.add_input_int(label=" Liczba generacji do zatrzymania ewolucji", tag="NoGo", default_value=100, width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba osobnikow w generacji", tag="NoOso", default_value=20,
                                          width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba rodzicow wybranych dla nowej populacji", tag="NoPeo", default_value=6, width=140, min_value=2, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Procentowe prawdopodobienstwo mutacji", tag="MutProbo", default_value=1,
                                          width=140, min_value=0, min_clamped=True, max_value=100, max_clamped=True, indent=140)
                        dpg.add_spacer(height=20)
                        dpg.add_button(label="Wykonaj", callback=self.start, indent=340)







    def start(self):
        """
        Given the following function:
            y = f(w1:w6) = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + 6wx6
            where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7) and y=44
        What are the best values for the 6 weights (w1 to w6)? We are going to use the genetic algorithm to optimize this function.
        """

        function_inputs = [dpg.get_value("inX"),dpg.get_value("inY"),dpg.get_value("inZ")] # Function inputs.
        result = dpg.get_value("resultxyz")
        def fitness_func(solution, solution_idx):
            # Calculating the fitness value of each solution in the current population.
            # The fitness function calulates the sum of products between each input and its corresponding weight.
            output = numpy.sum(solution * function_inputs)

            fitness = 1.0 / numpy.abs(output - result)
            return fitness

        fitness_function = fitness_func
        num_generations = dpg.get_value("NoGo")  # Number of generations.
        num_parents_mating = dpg.get_value("NoPeo")  # Number of solutions to be selected as parents in the mating pool.
        mut_prop = dpg.get_value("MutProbo")/100.0

        # To prepare the initial population, there are 2 ways:
        # 1) Prepare it yourself and pass it to the initial_population parameter. This way is useful when the user wants to start the genetic algorithm with a custom initial population.
        # 2) Assign valid integer values to the sol_per_pop and num_genes parameters. If the initial_population parameter exists, then the sol_per_pop and num_genes parameters are useless.
        sol_per_pop = dpg.get_value("NoOso")
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
                               mutation_probability=mut_prop,

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

        self.prediction = numpy.sum(numpy.array(function_inputs) * solution)
        print("Predicted output based on the best solution : {prediction}".format(prediction=self.prediction))

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

            with dpg.window(label=title, modal=True, no_close=True, autosize=True, tag="ggggo", pos=(9999,9999)) as modal_id:

                with dpg.plot(label="Jakosc rozwiazania w zaleznosci od generacji", width=1440, height=400, track_offset=5.0):
                    # optionally create legend
                    dpg.add_plot_legend()

                    # REQUIRED: create x and y axes
                    dpg.add_plot_axis(dpg.mvXAxis, label="Generacja")
                    dpg.add_plot_axis(dpg.mvYAxis, label="Jakosc", tag="y_axis2o")

                    # series belong to a y axis
                    dpg.add_line_series(list(range(0,101)), best_sols, parent="y_axis2o",
                                        tag="series_tag2o")


                dpg.add_spacer(height=20)
                dpg.add_text("Otrzymane rozwiazanie", indent=620)
                dpg.add_spacer(height=10)
                with dpg.group(horizontal=True):
                    dpg.add_spacer(width=20)
                    j = 0
                    for i in message:
                        if j == 0:
                            dpg.add_text("x = ")
                        elif j ==1:
                            dpg.add_text("y = ")
                        else:
                            dpg.add_text("z = ")
                        dpg.add_text(i)
                        dpg.add_spacer(width=10)
                        j += 1
                with dpg.group(horizontal=True):
                    dpg.add_spacer(width=20)
                    dpg.add_text(dpg.get_value("inX"))
                    if dpg.get_value("inY") >= 0:
                        dpg.add_text("* x + ")
                    else:
                        dpg.add_text("* x")
                    dpg.add_text(dpg.get_value("inY"))
                    if dpg.get_value("inZ") >= 0:
                        dpg.add_text("* y +")
                    else:
                        dpg.add_text("* y")
                    dpg.add_text(dpg.get_value("inZ"))
                    dpg.add_text("* z =")
                    dpg.add_text(self.prediction)
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