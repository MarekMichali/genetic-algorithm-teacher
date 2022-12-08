import random
import dearpygui.dearpygui as dpg
import config as c


class SingletonSelector(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Selector(metaclass=SingletonSelector):
    def __init__(self):
        self.blue = (15, 86, 135, 255)
        self.checkboxes = []
        self.checkboxesData = []
        self.y_offset = 100
        self.x_offset = -1
        self.x_move = 200
        self.count = 0
        self.whatRadio = 1
        self.selected_chromo = 7
        self.first_chromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.second_chromo = (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0)
        self.third_chromo = (1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0)
        self.fourth_chromo = (0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1)
        self.randoms = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7]
        self.rolCounter = 0
        self.rolCounterStop = 0
        with dpg.window(label="Selekcja", autosize=True, tag="selector", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("selector")
            with dpg.table(width=1440, height=640, header_row=False):
                dpg.add_table_column(width_fixed=True, init_width_or_weight=516)
                dpg.add_table_column(init_width_or_weight=740)
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        with open('data//selector.txt') as f:
                            lines = f.readlines()
                            for line in lines:
                                dpg.add_text(line, indent=20)

                        dpg.add_spacer(height=20)
                        with open('data//selectorExamples.txt') as f:
                            lines = f.readlines()
                            i = 0
                            for line in lines:
                                if i == 0 or i == 2:
                                    self.checkboxesData.append(line)
                                i += 1
                            self.checkboxes.append((dpg.add_radio_button(lines, callback=self.wartosc)))

                    with dpg.table_cell():
                        dpg.add_spacer(height=50)
                        with dpg.drawlist(width=1440, height=500, tag="selection_animation"):
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
                                                      color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48 + self.x_move, 50 + 2 * self.y_offset),
                                              (653 + self.x_move, 50 + 2 * self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50 + self.x_move, 50 + 2 * self.y_offset),
                                              (50 + self.x_move, 103 + 2 * self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50 + self.x_move, 100 + 2 * self.y_offset),
                                              (653 + self.x_move, 100 + 2 * self.y_offset), color=self.blue,
                                              thickness=5)
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

                            with dpg.draw_layer(tag="selector_arrows", show=True):
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
                            with dpg.draw_layer(tag="selector_fitness", show=True):
                                dpg.draw_text((- 70 + self.x_move, 54), "4", color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 70 + self.x_move, 54 + self.y_offset), "6",
                                              color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 70 + self.x_move, 54 + 2 * self.y_offset), "5",
                                              color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 70 + self.x_move, 54 + 3 * self.y_offset), "7",
                                              color=(250, 250, 250, 255), size=50)

                            with dpg.draw_layer(tag="hideFirst", show=True):
                                dpg.draw_rectangle((0, 0), (1200, 125), color=(60, 60, 61, 200),
                                                   fill=(60, 60, 61, 200))
                            with dpg.draw_layer(tag="hideSecond", show=False):
                                dpg.draw_rectangle((0, 125), (1200, 225), color=(60, 60, 61, 200),
                                                   fill=(60, 60, 61, 200))
                            with dpg.draw_layer(tag="hideThird", show=True):
                                dpg.draw_rectangle((0, 225), (1200, 325), color=(60, 60, 61, 200),
                                                   fill=(60, 60, 61, 200))
                            with dpg.draw_layer(tag="hideFourth", show=False):
                                dpg.draw_rectangle((0, 325), (1200, 425), color=(60, 60, 61, 200),
                                                   fill=(60, 60, 61, 200))
                            speed = 10

                            def animate():
                                if self.whatRadio == 2:
                                    self.count += 1
                                    self.rolCounter += 1
                                    if speed <= self.count < 2*speed:
                                        dpg.configure_item("hideFirst", show=False)
                                        dpg.configure_item("hideSecond", show=True)
                                        dpg.configure_item("hideThird", show=True)
                                        dpg.configure_item("hideFourth", show=True)
                                        if self.rolCounterStop <= self.rolCounter and self.selected_chromo == 4:
                                            self.count = 6*speed
                                    if 2*speed <= self.count < 3*speed:
                                        dpg.configure_item("hideFirst", show=True)
                                        dpg.configure_item("hideSecond", show=False)
                                        dpg.configure_item("hideThird", show=True)
                                        dpg.configure_item("hideFourth", show=True)
                                        if self.rolCounterStop <= self.rolCounter and self.selected_chromo == 6:
                                            self.count = 6*speed
                                    if 3*speed <= self.count < 4*speed:
                                        dpg.configure_item("hideFirst", show=True)
                                        dpg.configure_item("hideSecond", show=True)
                                        dpg.configure_item("hideThird", show=False)
                                        dpg.configure_item("hideFourth", show=True)
                                        if self.rolCounterStop <= self.rolCounter and self.selected_chromo == 5:
                                            self.count = 6*speed
                                    if 4*speed <= self.count < 5*speed:
                                        dpg.configure_item("hideFirst", show=True)
                                        dpg.configure_item("hideSecond", show=True)
                                        dpg.configure_item("hideThird", show=True)
                                        dpg.configure_item("hideFourth", show=False)
                                        if self.rolCounterStop <= self.rolCounter and self.selected_chromo == 7:
                                            self.count = 6*speed
                                    if self.count == 5*speed:
                                        self.count = speed
                                else:
                                    self.count = speed

                            with dpg.item_handler_registry(tag="selector_item_registry"):
                                dpg.add_item_visible_handler(callback=animate)
                            dpg.bind_item_handler_registry("selection_animation", dpg.last_container())

            with dpg.group(horizontal=True):
                dpg.add_button(width=c.navBut[0], height=c.navBut[1], arrow=True, direction=dpg.mvDir_Left, indent=660,
                               callback=lambda: self.back(), tag="selectorLeft")
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right,
                               callback=lambda: self.next(), tag="selectorRight")

    def show(self):
        if not dpg.is_item_visible("selector"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("selector")
            dpg.split_frame()
            width = dpg.get_item_width("selector")
            height = dpg.get_item_height("selector")
            dpg.set_item_pos("selector", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def show_ext(self):
        if not dpg.is_item_visible("selector"):
            dpg.disable_item("selectorLeft")
            dpg.disable_item("selectorRight")
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("selector")
            dpg.split_frame()
            width = dpg.get_item_width("selector")
            height = dpg.get_item_height("selector")
            dpg.set_item_pos("selector", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def wartosc(self, app_data, user_data):
        if "rankingowa" in user_data:
            self.whatRadio = 1
            dpg.configure_item("hideFirst", show=True)
            dpg.configure_item("hideSecond", show=False)
            dpg.configure_item("hideThird", show=True)
            dpg.configure_item("hideFourth", show=False)
        else:
            self.whatRadio = 2
            self.selected_chromo = random.choice(self.randoms)
            self.rolCounterStop = random.randrange(50, 200)
            self.rolCounter = 0
            print(self.selected_chromo)

    def next(self):
        dpg.enable_item("crossoverLeft")
        dpg.enable_item("crossoverRight")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("crossover")
        dpg.split_frame()
        width = dpg.get_item_width("crossover")
        height = dpg.get_item_height("crossover")
        dpg.set_item_pos("crossover", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("selector")

    def back(self):
        dpg.enable_item("fitnessLeft")
        dpg.enable_item("fitnessRight")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("fitness")
        dpg.split_frame()
        width = dpg.get_item_width("fitness")
        height = dpg.get_item_height("fitness")
        dpg.set_item_pos("fitness", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("selector")
