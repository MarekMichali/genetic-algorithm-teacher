import dearpygui.dearpygui as dpg
import numpy
from OptimizationGA import OptimizationGA
import ExampleInterface as ExampleInterface


class SingletonOptimization(type):
    """
        Klasa odpowiedzialna za implementację singletonu dla klasy Optimization
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Optimization(ExampleInterface.ExampleInterface, metaclass=SingletonOptimization):
    """
        Klasa odpowiedzialna za wyświetlenie przykładu szukania wartości argumentów
    """
    def __init__(self):
        self.prediction = 0
        with dpg.window(label="Znajdowanie argumentów", autosize=True, tag="optimalization", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("optimalization")
            with dpg.table(width=820, height=310, header_row=False):
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        dpg.add_text("Znajdowanie wartości argumentów x, y, z", indent=220)
                        dpg.add_spacer(height=20)
                        dpg.add_button(label="Sprawdź kodowanie chromosomu",
                                       callback=lambda: self.show_chromosome(self.on_selection), indent=250)
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
                        dpg.add_input_int(label=" Liczba osobników w generacji", tag="NoOo", default_value=20,
                                          width=140, min_value=1, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Liczba rodziców wybranych dla nowej populacji", tag="NoPo",
                                          default_value=6, width=140, min_value=2, min_clamped=True, indent=140)
                        dpg.add_input_int(label=" Procentowe prawdopodobieństwo mutacji", tag="MutPo",
                                          default_value=1, width=140, min_value=0, min_clamped=True, max_value=100,
                                          max_clamped=True, indent=140)
                        dpg.add_spacer(height=20)
                        dpg.add_button(label="Wykonaj", callback=self.start, indent=340, tag="optStart")

    def start(self):
        """
            Rozpoczyna walidację i działanie algorytmu genetycznego
        """
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
            self.error("Błąd", self.on_selection)
            return

        self.prediction = numpy.sum(numpy.array(function_inputs) * solution)
        self.show_info("Rozwiązanie", solution, self.on_selection, best_solutions_fitness)

    def show_info(self, title, message, selection_callback, best_sols):
        """
            Wyświetla informację o uzyskanym wyniku działania algorytmu genetycznego
        :param title: tytuł okienka
        :param message: wiadomość do wyświetlenia
        :param selection_callback: funkcja służąca do zamknięcia tego okienka
        :param best_sols: wynik działania algorytmu genetycznego
        """
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()

            with dpg.window(label=title, modal=True, no_close=True, autosize=True, tag="opt_plot",
                            pos=(9999, 9999)) as modal_id:
                with dpg.plot(label="Jakość rozwiązania w zależności od numeru generacji", width=1440, height=400,
                              track_offset=5.0):
                    dpg.add_plot_axis(dpg.mvXAxis, label="Numer generacji")
                    dpg.add_plot_axis(dpg.mvYAxis, label="Jakość", tag="y_axis_opt")
                    dpg.add_line_series(list(range(0, dpg.get_value("NoGo") + 1)), best_sols, parent="y_axis_opt")

                dpg.add_spacer(height=20)
                dpg.add_text("Otrzymane rozwiązanie", indent=620)
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
        """
            Zamyka okienko i odblokowywuje przycisk wykonania algorytmu genetycznego
        :param sender: wymagane przez DearPyGui, nieużywane
        :param unused: wymagane przez DearPyGui, nieużywane
        :param user_data: okienko, które należy zamknąć
        """
        dpg.delete_item(user_data[0])
        dpg.enable_item("optStart")

    def error(self, title, selection_callback):
        """
            Wyświetla okienko informujące o napotkanym błędzie
        :param title: tytuł okienka
        :param selection_callback: funkcja służąca do zamknięcia tego okienka
        """
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
        """
            Pokazuje przykładowe zadanie
        """
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("optimalization")
        dpg.split_frame()
        width = dpg.get_item_width("optimalization")
        height = dpg.get_item_height("optimalization")
        dpg.set_item_pos("optimalization", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")

    def show_chromosome(self, selection_callback):
        """
            Wyświetla informacje o kodowaniu chromosomu
        """
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
            with dpg.window(label="Kodowanie chromosomu", modal=True, no_close=True, autosize=True, tag="optimizationChromosome",
                            pos=(9999, 9999)) as modal_id:
                dpg.add_spacer(height=20)
                with open('data//optimization.txt', encoding="utf-8") as f:
                    lines = f.readlines()
                    for line in lines:
                        dpg.add_text(line, indent=20)
                dpg.add_spacer(height=20, width=570)
                dpg.add_text("Przykładowy chromosom", indent=20)
                dpg.add_spacer(height=5)
                dpg.add_text("[123.515|86.25|-7.6812]", indent=20)
                dpg.add_spacer(height=10)

                with dpg.group(horizontal=True):
                    dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=selection_callback,
                                   indent=247)

        dpg.split_frame()
        width = dpg.get_item_width(modal_id)
        height = dpg.get_item_height(modal_id)
        dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
