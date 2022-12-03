from math import sin, cos

import dearpygui.dearpygui as dpg
import numpy
import time

import config
import pygad


class Tsp:
    def __init__(self):
        self.blue = (15, 86, 135, 255)
        self.x_location = [8, 50, 18, 35, 90, 40, 84, 74, 34, 40, 60, 74]
        self.y_location = [3, 62, 20, 25, 89, 71, 7, 29, 45, 65, 69, 47]

        with dpg.window(label="Problem komiwojazera", autosize=True, tag="tsp", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("tsp")
            with dpg.table(width=820, height=310, header_row=False):
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        dpg.add_text("Zadanie omawiane w prezentacji.", indent=240)
                        dpg.add_text("Pozwala sprawdzic jaki wplyw na przebieg ewolucji maja poszczegolne parametry.",
                                     indent=20)
                        dpg.add_spacer(height=20)
                        dpg.add_input_int(label=" Liczba generacji do zatrzymania ewolucji", tag="NoGt",
                                          default_value=100, width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba osobnikow w generacji", tag="NoOt", default_value=20,
                                          width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba rodzicow wybranych dla nowej populacji", tag="NoPt",
                                          default_value=6, width=140, min_value=2, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Procentowe prawdopodobienstwo mutacji", tag="MutPt",
                                          default_value=1, width=140, min_value=0, min_clamped=True, max_value=100,
                                          max_clamped=True, indent=140)
                        dpg.add_spacer(height=20)
                        dpg.add_button(label="Wykonaj", callback=self.start, indent=340)

    def start(self):
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

        fitness_function = fitness_func
        num_generations = dpg.get_value("NoGt")
        num_parents_mating = dpg.get_value("NoPt")
        mut_prop = dpg.get_value("MutPt")/100.0
        sol_per_pop = dpg.get_value("NoOt")
        num_genes = len(self.x_location)
        gene_space = [i for i in range(1, 13)]
        population_list = []
        for i in range(sol_per_pop):
            nxm_random_num = list(numpy.random.permutation(gene_space))
            population_list.append(nxm_random_num)

        ga_instance = pygad.GA(num_generations=num_generations,
                               num_parents_mating=num_parents_mating,
                               initial_population=population_list,
                               fitness_func=fitness_function,
                               sol_per_pop=sol_per_pop,
                               num_genes=num_genes,
                               gene_type=int,
                               gene_space=gene_space,
                               allow_duplicate_genes=False)

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        self.show_info("Rozwiazanie", solution, self.on_selection, ga_instance.best_solutions_fitness)

    def show_info(self, title, message, selection_callback, best_sols):
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()

            with dpg.window(label=title, modal=True, no_close=True, autosize=True, tag="tsp_plot",
                            pos=(9999, 9999)) as modal_id:
                dpg.add_spacer(height=20)
                dpg.add_text("Otrzymane rozwiazanie", indent=620)
                dpg.add_spacer(height=10)
                with dpg.drawlist(width=1440, height=500):
                    with dpg.draw_layer():
                        j = 0
                        for i in self.x_location:
                            dpg.draw_circle((i, self.y_location[j]), radius=2, color=self.blue, fill=self.blue)
                            j += 1

                        i = 0
                        for loc in message:
                            if i == 0:
                                city_one = loc - 1
                                city_two = message[len(message) - 1] - 1
                                dpg.draw_line((self.x_location[city_one], self.y_location[city_one]),
                                              (self.x_location[city_two], self.y_location[city_two]),
                                              color=self.blue, thickness=1)
                            else:
                                city_one = loc - 1
                                city_two = message[i - 1] - 1
                                dpg.draw_line((self.x_location[city_one], self.y_location[city_one]),
                                              (self.x_location[city_two], self.y_location[city_two]),
                                              color=self.blue, thickness=1)
                            i += 1

                with dpg.group(horizontal=True):
                    dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=selection_callback,
                                   indent=685)

        dpg.split_frame()
        width = dpg.get_item_width(modal_id)
        height = dpg.get_item_height(modal_id)
        dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])

    def on_selection(self, sender, unused, user_data):
        dpg.delete_item(user_data[0])
