import dearpygui.dearpygui as dpg
import numpy
from OptimizationGA import OptimizationGA


class Optimization:
    def __init__(self):
        self.prediction = 0
        with dpg.window(label="Znajdowanie argumentow", autosize=True, tag="optimalization", pos=[99999, 99999],
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
                        dpg.add_input_int(label=" Liczba generacji do zatrzymania ewolucji", tag="NoGo",
                                          default_value=100, width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba osobnikow w generacji", tag="NoOo", default_value=20,
                                          width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba rodzicow wybranych dla nowej populacji", tag="NoPo",
                                          default_value=6, width=140, min_value=2, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Procentowe prawdopodobienstwo mutacji", tag="MutPo",
                                          default_value=1, width=140, min_value=0, min_clamped=True, max_value=100,
                                          max_clamped=True, indent=140)
                        dpg.add_spacer(height=20)
                        dpg.add_button(label="Wykonaj", callback=self.start, indent=340, tag="optStart")

    def start(self):
        dpg.disable_item("optStart")

        function_inputs = [dpg.get_value("inX"), dpg.get_value("inY"), dpg.get_value("inZ")]
        result = dpg.get_value("resultxyz")
        num_generations = dpg.get_value("NoGo")
        num_parents_mating = dpg.get_value("NoPo")
        mut_prop = dpg.get_value("MutPo")/100.0
        sol_per_pop = dpg.get_value("NoOo")

        optimization_ga = OptimizationGA(num_generations, num_parents_mating, mut_prop, sol_per_pop, function_inputs,
                                         result)
        solution, solution_fitness, best_solutions_fitness = optimization_ga.start()

        if solution[0] == -1 and solution_fitness[0] == -1 and best_solutions_fitness[0] == -1:
            self.error("Blad", self.on_selection)
            return

        self.prediction = numpy.sum(numpy.array(function_inputs) * solution)
        self.show_info("Rozwiazanie", solution, self.on_selection, best_solutions_fitness)

    def show_info(self, title, message, selection_callback, best_sols):
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()

            with dpg.window(label=title, modal=True, no_close=True, autosize=True, tag="opt_plot",
                            pos=(9999, 9999)) as modal_id:
                with dpg.plot(label="Jakosc rozwiazania w zaleznosci od generacji", width=1440, height=400,
                              track_offset=5.0):
                    dpg.add_plot_axis(dpg.mvXAxis, label="Generacja")
                    dpg.add_plot_axis(dpg.mvYAxis, label="Jakosc", tag="y_axis_opt")
                    dpg.add_line_series(list(range(0, 101)), best_sols, parent="y_axis_opt")

                dpg.add_spacer(height=20)
                dpg.add_text("Otrzymane rozwiazanie", indent=620)
                dpg.add_spacer(height=10)
                with dpg.group(horizontal=True):
                    dpg.add_spacer(width=20)
                    j = 0
                    for i in message:
                        if j == 0:
                            dpg.add_text("x = ")
                        elif j == 1:
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
                    dpg.add_text(str(self.prediction))
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=selection_callback,
                                   indent=685)
        dpg.split_frame()
        width = dpg.get_item_width(modal_id)
        height = dpg.get_item_height(modal_id)
        dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])

    def on_selection(self, sender, unused, user_data):
        dpg.delete_item(user_data[0])
        dpg.enable_item("optStart")

    def error(self, title, selection_callback):
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()

            with dpg.window(label=title, modal=True, no_close=True, autosize=True,
                            pos=(9999, 9999)) as modal_id:
                dpg.add_text("Nie moze byc wiecej rodzicow niz osobnikow w populacji!")
                dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=selection_callback,
                               indent=220)
        dpg.split_frame()
        width = dpg.get_item_width(modal_id)
        height = dpg.get_item_height(modal_id)
        dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
