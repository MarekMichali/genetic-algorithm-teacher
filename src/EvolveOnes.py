import dearpygui.dearpygui as dpg
from EvovleOnesGA import EvolveOnesGA


class SingletonEvolveOnes(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class EvolveOnes(metaclass=SingletonEvolveOnes):
    def __init__(self):
        self.chromo_color = (15, 86, 135, 255)
        self.y_offset = 100
        self.x_offset = -1
        self.first_chromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.last_fitness = 0
        with dpg.window(label="Ewolucja szczurów", autosize=True, tag="evolveOnes", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("evolveOnes")
            with dpg.table(width=820, height=310, header_row=False):
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        dpg.add_text("Zadanie omawiane w prezentacji.", indent=240)
                        dpg.add_text("Pozwala sprawdzić jaki wpływ na przebieg ewolucji mają poszczególne parametry.",
                                     indent=20)
                        dpg.add_spacer(height=20)
                        dpg.add_input_int(label=" Liczba generacji do zatrzymania ewolucji", tag="NoGe",
                                          default_value=100, width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba osobników w generacji", tag="NoOe", default_value=20,
                                          width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba rodziców wybranych dla nowej populacji", tag="NoPe",
                                          default_value=6, width=140, min_value=2, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Procentowe prawdopodobieństwo mutacji", tag="MutPe",
                                          default_value=1, width=140, min_value=0, min_clamped=True, max_value=100,
                                          max_clamped=True, indent=140)
                        dpg.add_spacer(height=20)
                        dpg.add_button(label="Wykonaj", callback=self.start, indent=340, tag="evoStart")

    def start(self):
        dpg.disable_item("evoStart")
        num_generations = dpg.get_value("NoGe")
        num_parents_mating = dpg.get_value("NoPe")
        mut_prop = dpg.get_value("MutPe")/100.0
        sol_per_pop = dpg.get_value("NoOe")
        function_inputs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        evolve_ones_ga = EvolveOnesGA(num_generations, num_parents_mating, mut_prop, sol_per_pop, function_inputs)
        solution, solution_fitness, best_solutions_fitness = evolve_ones_ga.start()

        if solution[0] == -1 and solution_fitness[0] == -1 and best_solutions_fitness[0] == -1:
            self.error("Błąd", self.on_selection)
            return
        self.show_info("Rozwiązanie", solution, self.on_selection, best_solutions_fitness)

    def show_info(self, title, message, selection_callback, best_sols):
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()

            with dpg.window(label=title, modal=True, no_close=True, autosize=True, tag="ones_plot",
                            pos=(9999, 9999)) as modal_id:
                with dpg.plot(label="Jakość rozwiązania w zależności od numer generacji", width=1440, height=400,
                              track_offset=5.0):
                    dpg.add_plot_axis(dpg.mvXAxis, label="Numer generacji")
                    dpg.add_plot_axis(dpg.mvYAxis, label="Jakość", tag="y_axis_ones")
                    dpg.add_line_series(list(range(0, dpg.get_value("NoGe") + 1)), best_sols, parent="y_axis_ones")

                dpg.add_spacer(height=20)
                dpg.add_text("Otrzymane rozwiązanie", indent=620)
                dpg.add_spacer(height=10)
                with dpg.drawlist(width=1440, height=130):
                    with dpg.draw_layer():
                        dpg.draw_line((418, 5), (1023, 5), color=self.chromo_color, thickness=5)
                        dpg.draw_line((420, 5), (420, 58), color=self.chromo_color, thickness=5)
                        dpg.draw_line((420, 55), (1023, 55), color=self.chromo_color, thickness=5)

                        x = 470
                        y = 5
                        allel_x = 433
                        allel_y = 9
                        for i in message:
                            dpg.draw_line((x, y), (x, 50 + y), color=self.chromo_color, thickness=5)
                            if i == 0:
                                dpg.draw_text((allel_x, allel_y), "0", color=(250, 250, 250, 255), size=50)
                            else:
                                dpg.draw_text((allel_x + self.x_offset, allel_y), "1",
                                              color=(250, 250, 250, 255),
                                              size=50)
                            x += 50
                            allel_x += 50
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=selection_callback,
                                   indent=685)

        dpg.split_frame()
        width = dpg.get_item_width(modal_id)
        height = dpg.get_item_height(modal_id)
        dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])

    def on_selection(self, sender, unused, user_data):
        dpg.delete_item(user_data[0])
        dpg.enable_item("evoStart")

    def error(self, title, selection_callback):
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()

            with dpg.window(label=title, modal=True, no_close=True, autosize=True,
                            pos=(9999, 9999)) as modal_id:
                dpg.add_text("Nie może być więcej rodziców niż osobników w populacji!")
                dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=selection_callback,
                               indent=220)
        dpg.split_frame()
        width = dpg.get_item_width(modal_id)
        height = dpg.get_item_height(modal_id)
        dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])

    def show(self):
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("evolveOnes")
        dpg.split_frame()
        width = dpg.get_item_width("evolveOnes")
        height = dpg.get_item_height("evolveOnes")
        dpg.set_item_pos("evolveOnes", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")
