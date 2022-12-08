import dearpygui.dearpygui as dpg
import config as c


class SingletonFitness(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Fitness(metaclass=SingletonFitness):
    def __init__(self):
        self.blue = (15, 86, 135, 255)
        self.checkboxes = []
        self.y_offset = 100
        self.x_offset = -1
        self.x_move = 200
        self.first_chromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.second_chromo = (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0)
        self.third_chromo = (1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0)
        self.fourth_chromo = (0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1)
        with dpg.window(label="Ocena rozwiązania", autosize=True, tag="fitness", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("fitness")
            with dpg.table(width=1440, height=640, header_row=False):
                dpg.add_table_column(width_fixed=True, init_width_or_weight=516)
                dpg.add_table_column(init_width_or_weight=740)
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        with open('data//fitness.txt' , encoding="utf-8") as f:
                            lines = f.readlines()
                            for line in lines:
                                dpg.add_text(line, indent=20)
                        dpg.add_spacer(height=20)
                        with open('data//fitnessExamples.txt' , encoding="utf-8") as f:
                            lines = f.readlines()
                            self.checkboxes.append((dpg.add_radio_button(lines, callback=self.values)))

                    with dpg.table_cell():
                        dpg.add_spacer(height=50)
                        with dpg.drawlist(width=1440, height=500):
                            with dpg.draw_layer():
                                dpg.draw_line((48 + self.x_move, 50), (653 + self.x_move, 50), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50 + self.x_move, 50), (50 + self.x_move, 103), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50 + self.x_move, 100), (653 + self.x_move, 100), color=self.blue,
                                              thickness=5)

                                x = 100 + self.x_move
                                y = 50
                                allel_x = 63 + self.x_move
                                allel_y = 54
                                counter = 11
                                for i in self.first_chromo:
                                    counter -= 1
                                    dpg.draw_line((x, y), (x, 2 * y), color=self.blue, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y), "1",
                                                      color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48 + self.x_move, 50 + self.y_offset),
                                              (653 + self.x_move, 50 + self.y_offset), color=self.blue, thickness=5)
                                dpg.draw_line((50 + self.x_move, 50 + self.y_offset),
                                              (50 + self.x_move, 103 + self.y_offset), color=self.blue, thickness=5)
                                dpg.draw_line((50 + self.x_move, 100 + self.y_offset),
                                              (653 + self.x_move, 100 + self.y_offset), color=self.blue, thickness=5)
                                x = 100 + self.x_move
                                y = 50
                                allel_x = 63 + self.x_move
                                allel_y = 54
                                for i in self.second_chromo:
                                    dpg.draw_line((x, y + self.y_offset), (x, 2 * y + self.y_offset), color=self.blue,
                                                  thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y + self.y_offset), "0",
                                                      color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y + self.y_offset), "1",
                                                      color=(250, 250, 250, 255), size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48 + self.x_move, 50 + 2 * self.y_offset),
                                              (653 + self.x_move, 50 + 2 * self.y_offset),
                                              color=self.blue, thickness=5)
                                dpg.draw_line((50 + self.x_move, 50 + 2 * self.y_offset),
                                              (50 + self.x_move, 103 + 2 * self.y_offset),
                                              color=self.blue, thickness=5)
                                dpg.draw_line((50 + self.x_move, 100 + 2 * self.y_offset),
                                              (653 + self.x_move, 100 + 2 * self.y_offset),
                                              color=self.blue, thickness=5)
                                x = 100 + self.x_move
                                y = 50
                                allel_x = 63 + self.x_move
                                allel_y = 54
                                for i in self.third_chromo:
                                    dpg.draw_line((x, y + 2*self.y_offset), (x, 2 * y + 2 * self.y_offset),
                                                  color=self.blue, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y + 2*self.y_offset), "0",
                                                      color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y + 2 * self.y_offset), "1",
                                                      color=(250, 250, 250, 255), size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48 + self.x_move, 50 + 3 * self.y_offset),
                                              (653 + self.x_move, 50 + 3 * self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50 + self.x_move, 50 + 3 * self.y_offset),
                                              (50 + self.x_move, 103 + 3 * self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50 + self.x_move, 100 + 3 * self.y_offset),
                                              (653 + self.x_move, 100 + 3 * self.y_offset), color=self.blue,
                                              thickness=5)
                                x = 100 + self.x_move
                                y = 50
                                allel_x = 63 + self.x_move
                                allel_y = 54
                                for i in self.fourth_chromo:
                                    dpg.draw_line((x, y + 3*self.y_offset), (x, 2 * y + 3 * self.y_offset),
                                                  color=self.blue, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y + 3*self.y_offset), "0",
                                                      color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y + 3 * self.y_offset), "1",
                                                      color=(250, 250, 250, 255), size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer(tag="arrowsLayer", show=True):
                                dpg.draw_arrow((-25 + self.x_move, 75), (25 + self.x_move, 75), color=(0, 200, 255),
                                               thickness=5, size=10)
                                dpg.draw_arrow((-25 + self.x_move, 75 + self.y_offset),
                                               (25 + self.x_move, 75 + self.y_offset), color=(0, 200, 255),
                                               thickness=5, size=10)
                                dpg.draw_arrow((-25 + self.x_move, 75 + 2 * self.y_offset),
                                               (25 + self.x_move, 75 + 2 * self.y_offset), color=(0, 200, 255),
                                               thickness=5, size=10)
                                dpg.draw_arrow((-25 + self.x_move, 75 + 3 * self.y_offset),
                                               (25 + self.x_move, 75 + 3 * self.y_offset), color=(0, 200, 255),
                                               thickness=5, size=10)

                            with dpg.draw_layer(tag="firstRadiLayer", show=True):
                                dpg.draw_text((- 70 + self.x_move, 54), "4", color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 70 + self.x_move, 54 + self.y_offset), "6",
                                              color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 70 + self.x_move, 54 + 2 * self.y_offset), "5",
                                              color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 70 + self.x_move, 54 + 3 * self.y_offset), "7",
                                              color=(250, 250, 250, 255), size=50)

                            with dpg.draw_layer(tag="secondRadiLayer", show=False):
                                dpg.draw_text((- 110 + self.x_move, 54), "401", color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 150 + self.x_move, 54 + self.y_offset), "3356",
                                              color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 150 + self.x_move, 54 + 2 * self.y_offset), "2834",
                                              color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 137 + self.x_move, 54 + 3 * self.y_offset), "1259",
                                              color=(250, 250, 250, 255), size=50)

            with dpg.group(horizontal=True):
                dpg.add_button(width=c.navBut[0], height=c.navBut[1], arrow=True, direction=dpg.mvDir_Left,
                               indent=660, callback=lambda: self.back(), tag="fitnessLeft")
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right,
                               callback=lambda: self.next(), tag="fitnessRight")

    def show(self):
        if not dpg.is_item_visible("fitness"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("fitness")
            dpg.split_frame()
            width = dpg.get_item_width("fitness")
            height = dpg.get_item_height("fitness")
            dpg.set_item_pos("fitness", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def show_ext(self):
        if not dpg.is_item_visible("fitness"):
            dpg.disable_item("fitnessLeft")
            dpg.disable_item("fitnessRight")
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("fitness")
            dpg.split_frame()
            width = dpg.get_item_width("fitness")
            height = dpg.get_item_height("fitness")
            dpg.set_item_pos("fitness", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def values(self, app_data, user_data):
        if "ilości" in user_data:
            dpg.configure_item("firstRadiLayer", show=True)
            dpg.configure_item("secondRadiLayer", show=False)
        else:
            dpg.configure_item("firstRadiLayer", show=False)
            dpg.configure_item("secondRadiLayer", show=True)

    def next(self):
        dpg.enable_item("selectorLeft")
        dpg.enable_item("selectorRight")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("selector")
        dpg.split_frame()
        width = dpg.get_item_width("selector")
        height = dpg.get_item_height("selector")
        dpg.set_item_pos("selector", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("fitness")

    def back(self):
        dpg.enable_item("dictionaryLeft")
        dpg.enable_item("dictionaryRight")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("dictionary")
        dpg.split_frame()
        width = dpg.get_item_width("dictionary")
        height = dpg.get_item_height("dictionary")
        dpg.set_item_pos("dictionary", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("fitness")
