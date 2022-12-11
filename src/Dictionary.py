import dearpygui.dearpygui as dpg
import config
import PresentationInterface


class SingletonDictionary(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Dictionary(PresentationInterface.PresentationInterface, config.Config, metaclass=SingletonDictionary):
    def __init__(self):
        self.chromo_color = (15, 86, 135, 255)
        self.checkboxes = []
        self.y_offset = 100
        self.x_offset = -1
        self.first_chromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.second_chromo = (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0)
        with dpg.window(label="Podstawowe pojęcia", autosize=True, tag="dictionary", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("dictionary")
            with dpg.table(width=1440, height=640, header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        with open('data//dictionarySlide.txt', encoding="utf-8") as f:
                            lines = f.readlines()
                            for line in lines:
                                dpg.add_text(line, indent=20)
                        dpg.add_spacer(height=5)
                        with open('data//gen.txt', encoding="utf-8") as f:
                            lines = f.readlines()
                            i = 0
                            for line in lines:
                                i += 1
                                if i == 3 or i == 8:
                                    with dpg.group(horizontal=True):
                                        dpg.add_text(line, indent=63)
                                        continue
                                if i == 6 or i == 7:
                                    with dpg.group(horizontal=True):
                                        dpg.add_text(line, indent=34, bullet=True)
                                        continue
                                with dpg.group(horizontal=True):
                                    self.checkboxes.append(dpg.add_checkbox(callback=self.show_layer))
                                    dpg.add_text(line, bullet=True)

                    with dpg.table_cell():
                        dpg.add_spacer(height=50)
                        with dpg.drawlist(width=800, height=500):
                            with dpg.draw_layer():
                                dpg.draw_line((48, 50), (653, 50), color=self.chromo_color, thickness=5)
                                dpg.draw_line((50, 50), (50, 103), color=self.chromo_color, thickness=5)
                                dpg.draw_line((50, 100), (653, 100), color=self.chromo_color, thickness=5)

                                x = 100
                                y = 50
                                allel_x = 63
                                allel_y = 54
                                for i in self.first_chromo:
                                    dpg.draw_line((x, y), (x, 2 * y), color=self.chromo_color, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y), "1",
                                                      color=(250, 250, 250, 255), size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48, 50 + self.y_offset), (653, 50 + self.y_offset),
                                              color=self.chromo_color, thickness=5)
                                dpg.draw_line((50, 50 + self.y_offset), (50, 103 + self.y_offset),
                                              color=self.chromo_color, thickness=5)
                                dpg.draw_line((50, 100 + self.y_offset), (653, 100 + self.y_offset),
                                              color=self.chromo_color, thickness=5)

                                x = 100
                                y = 50
                                allel_x = 63
                                allel_y = 54
                                for i in self.second_chromo:
                                    dpg.draw_line((x, y + self.y_offset), (x, 2 * y + self.y_offset),
                                                  color=self.chromo_color, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y + self.y_offset), "0",
                                                      color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y + self.y_offset), "1",
                                                      color=(250, 250, 250, 255),  size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer(tag="genLayer", show=False):
                                dpg.draw_circle((125, 75), color=(255, 242, 0, 200), radius=38, thickness=5)

                            with dpg.draw_layer(tag="chromoLayer", show=False):
                                dpg.draw_ellipse((25, 25), (675, 125), color=(255, 242, 0, 200), thickness=5)

                            with dpg.draw_layer(tag="popuLayer", show=False):
                                dpg.draw_ellipse((25, 25), (675, 125 + self.y_offset), color=(255, 242, 0, 200),
                                                 thickness=5)

            with dpg.group(horizontal=True):
                dpg.add_button(width=self.navBut[0], height=self.navBut[1], arrow=True, direction=dpg.mvDir_Left,
                               indent=660, callback=lambda: self.back(), tag="dictionaryLeft", enabled=True)
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right,
                               callback=lambda: self.next(), tag="dictionaryRight")

    def show(self):
        if not dpg.is_item_visible("dictionary"):
            dpg.split_frame()
            dpg.set_item_pos("dictionary", dpg.get_item_pos("diagram"))
            dpg.show_item("dictionary")
            dpg.hide_item("mainWindow")

    def show_ext(self):
        if not dpg.is_item_visible("dictionary"):
            dpg.disable_item("dictionaryLeft")
            dpg.disable_item("dictionaryRight")
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("dictionary")
            dpg.split_frame()
            width = dpg.get_item_width("dictionary")
            height = dpg.get_item_height("dictionary")
            dpg.set_item_pos("dictionary", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def show_layer(self, sender):
        show_value = dpg.get_value(sender)
        i = 0
        for x in self.checkboxes:
            if x == sender:
                if i == 0:
                    dpg.configure_item("genLayer", show=show_value)
                elif i == 2 or i == 1:
                    show_value = dpg.get_value(self.checkboxes[2]) or dpg.get_value(self.checkboxes[1])
                    dpg.configure_item("chromoLayer", show=show_value)
                elif i == 3:
                    dpg.configure_item("popuLayer", show=show_value)
            i += 1

    def next(self):
        dpg.enable_item("fitnessLeft")
        dpg.enable_item("fitnessRight")
        dpg.split_frame()
        dpg.set_item_pos("fitness", dpg.get_item_pos("dictionary"))
        dpg.show_item("fitness")
        dpg.hide_item("dictionary")

    def back(self):
        dpg.enable_item("diagramLeft")
        dpg.enable_item("diagramRight")
        dpg.split_frame()
        dpg.set_item_pos("diagram",  dpg.get_item_pos("dictionary"))
        dpg.show_item("diagram")
        dpg.hide_item("dictionary")
