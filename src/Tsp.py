import random
import dearpygui.dearpygui as dpg
from TspGA import TspGA
import ExampleInterface


class SingletonTsp(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Tsp(ExampleInterface.ExampleInterface, metaclass=SingletonTsp):
    def __init__(self):
        self.dot_color = (255, 242, 0, 255)
        self.line_color = (255, 242, 0, 128)
        self.x_location = [8.0, 50.0, 18.0, 35.0, 90.0, 40.0, 84.0, 74.0, 34.0, 40.0, 60.0, 74.0]
        self.y_location = [3.0, 62.0, 20.0, 25.0, 89.0, 71.0, 7.0, 29.0, 45.0, 65.0, 69.0, 47.0]

        def print_val(sender, app_data, user_data):
            location = dpg.get_value(sender)
            x = location[0]
            y = location[1]
            if user_data == "warszawa":
                self.x_location[0] = x
                self.y_location[0] = y
            elif user_data == "berlin":
                self.x_location[1] = x
                self.y_location[1] = y
            elif user_data == "praga":
                self.x_location[2] = x
                self.y_location[2] = y
            elif user_data == "wieden":
                self.x_location[3] = x
                self.y_location[3] = y
            elif user_data == "bratyslawa":
                self.x_location[4] = x
                self.y_location[4] = y
            elif user_data == "londyn":
                self.x_location[5] = x
                self.y_location[5] = y
            elif user_data == "lizbona":
                self.x_location[6] = x
                self.y_location[6] = y
            elif user_data == "wilno":
                self.x_location[7] = x
                self.y_location[7] = y
            elif user_data == "kopenhaga":
                self.x_location[8] = x
                self.y_location[8] = y
            elif user_data == "paryz":
                self.x_location[9] = x
                self.y_location[9] = y
            elif user_data == "rzym":
                self.x_location[10] = x
                self.y_location[10] = y
            elif user_data == "berno":
                self.x_location[11] = x
                self.y_location[11] = y

        def shuffle(sender, app_data, user_data):
            for i in range(12):
                rx = random.randint(1, 99)
                ry = random.randint(1, 99)
                self.x_location[i] = rx
                self.y_location[i] = ry

            dpg.set_value("warszawa", value=[self.x_location[0], self.y_location[0]])
            dpg.set_value("berlin", value=[self.x_location[1], self.y_location[1]])
            dpg.set_value("praga", value=[self.x_location[2], self.y_location[2]])
            dpg.set_value("wieden", value=[self.x_location[3], self.y_location[3]])
            dpg.set_value("bratyslawa", value=[self.x_location[4], self.y_location[4]])
            dpg.set_value("londyn", value=[self.x_location[5], self.y_location[5]])
            dpg.set_value("lizbona", value=[self.x_location[6], self.y_location[6]])
            dpg.set_value("wilno", value=[self.x_location[7], self.y_location[7]])
            dpg.set_value("kopenhaga", value=[self.x_location[8], self.y_location[8]])
            dpg.set_value("paryz", value=[self.x_location[9], self.y_location[9]])
            dpg.set_value("rzym", value=[self.x_location[10], self.y_location[10]])
            dpg.set_value("berno", value=[self.x_location[11], self.y_location[11]])

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

                                    dpg.add_drag_point(label="Warszawa", color=self.dot_color, tag="warszawa",
                                                       default_value=(self.x_location[0], self.y_location[0]),
                                                       callback=print_val, user_data="warszawa", thickness=20)
                                    dpg.add_drag_point(label="Berlin", color=self.dot_color, tag="berlin",
                                                       default_value=(self.x_location[1], self.y_location[1]),
                                                       callback=print_val, user_data="berlin")
                                    dpg.add_drag_point(label="Praga", color=self.dot_color, tag="praga",
                                                       default_value=(self.x_location[2], self.y_location[2]),
                                                       callback=print_val, user_data="praga")
                                    dpg.add_drag_point(label="Wieden", color=self.dot_color, tag="wieden",
                                                       default_value=(self.x_location[3], self.y_location[3]),
                                                       callback=print_val, user_data="wieden")
                                    dpg.add_drag_point(label="Bratyslawa", color=self.dot_color, tag="bratyslawa",
                                                       default_value=(self.x_location[4], self.y_location[4]),
                                                       callback=print_val, user_data="bratyslawa")
                                    dpg.add_drag_point(label="Londyn", color=self.dot_color, tag="londyn",
                                                       default_value=(self.x_location[5], self.y_location[5]),
                                                       callback=print_val, user_data="londyn")
                                    dpg.add_drag_point(label="Lizbona", color=self.dot_color, tag="lizbona",
                                                       default_value=(self.x_location[6], self.y_location[6]),
                                                       callback=print_val, user_data="lizbona")
                                    dpg.add_drag_point(label="Wilno", color=self.dot_color, tag="wilno",
                                                       default_value=(self.x_location[7], self.y_location[7]),
                                                       callback=print_val, user_data="wilno")
                                    dpg.add_drag_point(label="Kopenhaga", color=self.dot_color, tag="kopenhaga",
                                                       default_value=(self.x_location[8], self.y_location[8]),
                                                       callback=print_val, user_data="kopenhaga")
                                    dpg.add_drag_point(label="Paryz", color=self.dot_color, tag="paryz",
                                                       default_value=(self.x_location[9], self.y_location[9]),
                                                       callback=print_val, user_data="paryz")
                                    dpg.add_drag_point(label="Rzym", color=self.dot_color, tag="rzym",
                                                       default_value=(self.x_location[10], self.y_location[10]),
                                                       callback=print_val, user_data="rzym")
                                    dpg.add_drag_point(label="Berno", color=self.dot_color, tag="berno",
                                                       default_value=(self.x_location[11], self.y_location[11]),
                                                       callback=print_val, user_data="berno")

    def start(self):
        dpg.disable_item("tspStart")

        num_generations = dpg.get_value("NoGt")
        num_parents_mating = dpg.get_value("NoPt")
        sol_per_pop = dpg.get_value("NoOt")

        tsp_ga = TspGA(num_generations, num_parents_mating, sol_per_pop, self.x_location, self.y_location)
        solution, solution_fitness, best_solutions_fitness = tsp_ga.start()

        if solution[0] == -1 and solution_fitness[0] == -1 and best_solutions_fitness[0] == -1:
            self.error("Błąd", self.on_selection)
            return

        self.show_info("Rozwiązanie", solution, self.on_selection, best_solutions_fitness)

    def show_info(self, title, message, selection_callback, best_sols):
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
        dpg.delete_item(user_data[0])
        dpg.enable_item("tspStart")

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
        dpg.show_item("tsp")
        dpg.split_frame()
        width = dpg.get_item_width("tsp")
        height = dpg.get_item_height("tsp")
        dpg.set_item_pos("tsp", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")
