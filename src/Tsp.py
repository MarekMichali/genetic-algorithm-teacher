import random
import dearpygui.dearpygui as dpg
from TspGA import TspGA
import ExampleInterface as ExampleInterface


class SingletonTsp(type):
    """
        Klasa odpowiedzialna za implementację singletonu dla klasy Tsp
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Tsp(ExampleInterface.ExampleInterface, metaclass=SingletonTsp):
    """
        Klasa odpowiedzialna za wyświetlenie przykładu problemu komiwojażera
    """
    def __init__(self, cities_count=10):
        self.dot_color = (255, 242, 0, 255)
        self.line_color = (255, 242, 0, 128)
        self.x_location = []
        self.y_location = []
        self.cities = []
        self.cities_count = cities_count
        for i in range(0, self.cities_count):
            self.cities.append(i)
            self.x_location.append(random.randint(1, 99))
            self.y_location.append(random.randint(1, 99))

        def print_val(sender, app_data, user_data):
            location = dpg.get_value(sender)
            x = location[0]
            y = location[1]
            for i in self.cities:
                if user_data == str(i):
                    self.x_location[i] = x
                    self.y_location[i] = y

        def shuffle(sender, app_data, user_data):
            for i in range(self.cities_count):
                rx = random.randint(1, 99)
                ry = random.randint(1, 99)
                self.x_location[i] = rx
                self.y_location[i] = ry

            for i in self.cities:
                dpg.set_value(str(i), value=[self.x_location[i], self.y_location[i]])


        with dpg.window(label="Problem komiwojażera", autosize=True, tag="tsp", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("tsp")
            with dpg.table(width=1440, height=600, header_row=False):
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        dpg.add_text(
                            "Komiwojażer chce odwiedzić wszystkie miasta tylko jeden raz i wrócić do miasta,"
                            " z którego zaczynał pokonując jak najkrótsza trasę.",
                            indent=20)
                        dpg.add_text(
                            "Rozmieść punkty odpowiadające miastom przeciągając je myszką i skonfiguruj działanie"
                            " algorytmu genetycznego.",
                            indent=20)
                        dpg.add_spacer(height=20)
                        with dpg.group(horizontal=True):
                            with dpg.group():
                                dpg.add_spacer(height=100)
                                dpg.add_button(label="Sprawdź kodowanie chromosomu",
                                               callback=lambda: self.show_chromosome(self.on_selection), indent=140)
                                dpg.add_spacer(height=20)
                                dpg.add_button(label="Losuj położenie miast", callback=shuffle, indent=187)
                                dpg.add_spacer(height=20)
                                dpg.add_input_int(label=" Liczba generacji do zatrzymania ewolucji", tag="NoGt",
                                                  default_value=100, width=140, min_value=1,
                                                  min_clamped=True, indent=40)
                                dpg.add_input_int(label=" Liczba osobników w generacji", tag="NoOt", default_value=20,
                                                  width=140, min_value=1, min_clamped=True, indent=40)
                                dpg.add_input_int(label=" Liczba rodziców wybranych dla nowej populacji", tag="NoPt",
                                                  default_value=6, width=140, min_value=2, min_clamped=True, indent=40)
                                dpg.add_spacer(height=20)
                                dpg.add_button(label="Wykonaj", callback=self.start, indent=240, tag="tspStart")
                                dpg.add_spacer(width=700)

                            with dpg.group():
                                with dpg.plot(label="Położenie miast", height=550, width=550):
                                    dpg.add_plot_legend()
                                    dpg.add_plot_axis(dpg.mvXAxis, label="x")
                                    dpg.set_axis_limits(dpg.last_item(), 0, 100)
                                    dpg.add_plot_axis(dpg.mvYAxis, label="y")
                                    dpg.set_axis_limits(dpg.last_item(), 0, 100)

                                    for i in self.cities:
                                        dpg.add_drag_point(label=str(i), color=self.dot_color, tag=str(i),
                                                           default_value=(self.x_location[i], self.y_location[i]),
                                                           callback=print_val, user_data=str(i), thickness=20)


    def start(self):
        """
            Rozpoczyna walidację i działanie algorytmu genetycznego
        """
        dpg.disable_item("tspStart")

        num_generations = dpg.get_value("NoGt")
        num_parents_mating = dpg.get_value("NoPt")
        sol_per_pop = dpg.get_value("NoOt")

        tsp_ga = TspGA(num_generations, num_parents_mating, sol_per_pop, self.x_location, self.y_location) #tu
        solution, solution_fitness, best_solutions_fitness = tsp_ga.start()

        if solution[0] == -1 and solution_fitness[0] == -1 and best_solutions_fitness[0] == -1:
            self.error("Błąd", self.on_selection)
            return

        self.show_info("Rozwiązanie", solution, self.on_selection, best_solutions_fitness)

    def show_info(self, title, message, selection_callback, best_sols):
        """
            Wyświetla informację o uzyskanym wyniku działania algorytmu genetycznego
        :param title: tytuł okienka
        :param message: wiadomość do wyświetlenia
        :param selection_callback: funkcja służąca do zamknięcia tego okienka
        :param best_sols: wynik działania algorytmu genetycznego
        """
        y_invert = 505
        x_indent = 10
        multiplier = 5
        thickness = 5
        plot_data = []

        for b in best_sols:
            plot_data.append(b * -1)

        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()

            with dpg.window(label=title, modal=True, no_close=True, autosize=True, tag="tsp_plot",
                            pos=(9999, 9999)) as modal_id:
                dpg.add_spacer(height=20)
                dpg.add_text("Otrzymane rozwiązanie", indent=620)
                dpg.add_spacer(height=10)
                with dpg.group(horizontal=True):
                    with dpg.plot(label="Długość trasy w zależności od numeru generacji", width=700, height=500,
                                  track_offset=5.0):
                        dpg.add_plot_axis(dpg.mvXAxis, label="Numer generacji")
                        dpg.add_plot_axis(dpg.mvYAxis, label="Długość trasy", tag="y_axis_tsp")
                        dpg.add_line_series(list(range(0, dpg.get_value("NoGt")+1)), plot_data, parent="y_axis_tsp")
                    dpg.add_spacer(width=20)
                    with dpg.drawlist(width=700, height=560):
                        with dpg.draw_layer():
                            j = 0
                            for i in self.x_location:
                                dpg.draw_circle((x_indent + multiplier * i, y_invert - multiplier * self.y_location[j]),
                                                radius=5, color=self.dot_color, fill=self.dot_color)
                                j += 1

                            i = 0
                            for loc in message:
                                if i == 0:
                                    city_one = loc - 1
                                    city_two = message[len(message) - 1] - 1
                                    dpg.draw_line((x_indent + multiplier * self.x_location[city_one],
                                                   y_invert - multiplier * self.y_location[city_one]),
                                                  (x_indent + multiplier * self.x_location[city_two],
                                                   y_invert - multiplier * self.y_location[city_two]),
                                                  color=self.line_color, thickness=thickness)
                                else:
                                    city_one = loc - 1
                                    city_two = message[i - 1] - 1
                                    dpg.draw_line((x_indent + multiplier * self.x_location[city_one],
                                                   y_invert - multiplier * self.y_location[city_one]),
                                                  (x_indent + multiplier * self.x_location[city_two],
                                                   y_invert - multiplier * self.y_location[city_two]),
                                                  color=self.line_color, thickness=thickness)
                                i += 1

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
        dpg.enable_item("tspStart")

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
        dpg.show_item("tsp")
        dpg.split_frame()
        width = dpg.get_item_width("tsp")
        height = dpg.get_item_height("tsp")
        dpg.set_item_pos("tsp", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")

    def show_chromosome(self, selection_callback):
        """
            Wyświetla informacje o kodowaniu chromosomu
        """
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
            with dpg.window(label="Kodowanie chromosomu", modal=True, no_close=True, autosize=True, tag="tpsChromosome",
                            pos=(9999, 9999)) as modal_id:
                dpg.add_spacer(height=20)
                with open('data//tsp.txt', encoding="utf-8") as f:
                    lines = f.readlines()
                    for line in lines:
                        dpg.add_text(line, indent=20)
                dpg.add_spacer(height=20, width=570)
                dpg.add_text("Przykładowe ułożenie miast w chromosomie", indent=20)
                dpg.add_spacer(height=5)
                dpg.add_text("[WAW|BER|PRG|VIE|BTS|LON|LIS|VNO|CPH|PAR|ROM|BRN]", indent=20)
                dpg.add_spacer(height=10)

                with dpg.group(horizontal=True):
                    dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=selection_callback,
                                   indent=247)

        dpg.split_frame()
        width = dpg.get_item_width(modal_id)
        height = dpg.get_item_height(modal_id)
        dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
