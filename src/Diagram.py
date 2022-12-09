import math
import dearpygui.dearpygui as dpg
import config as c


class SingletonDiagram(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Diagram(metaclass=SingletonDiagram):
    def __init__(self):
        self.blue = (15, 86, 135, 255)
        self.y_offset = 100
        self.x_offset = -1
        self.first_chromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.second_chromo = (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0)
        self.renderCount = 0
        with dpg.window(label="Diagram", autosize=True, tag="diagram", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("diagram")
            with dpg.table(width=1440, height=640, header_row=False):
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=50)
                        with dpg.drawlist(width=1440, height=600):
                            height = 50
                            width = 271
                            dpg.draw_rectangle([width + 70, height], [width + 370, height + 50],
                                               thickness=5, color=self.blue)
                            dpg.draw_text([width + 125, height + 5], "Generowanie populacji", size=20)
                            dpg.draw_text([width + 165, height + 25], "poczatkowej", size=20)
                            dpg.draw_rectangle([width + 470, height], [width + 770, height + 50],
                                               thickness=5, color=self.blue)
                            dpg.draw_rectangle([width + 470, height + 100], [width + 770, height + 150],
                                               thickness=5, color=self.blue)
                            dpg.draw_rectangle([width + 270, height + 200], [width + 570, height + 250],
                                               thickness=5, color=self.blue)
                            dpg.draw_quad([width + 420, height + 300], [width + 520, height + 400],
                                          [width + 420, height + 500], [width + 320, height + 400],
                                          thickness=5, color=self.blue)


            with dpg.group(horizontal=True):
                dpg.add_button(width=c.navBut[0], height=c.navBut[1], arrow=True, direction=dpg.mvDir_Left, indent=660,
                               callback=lambda: self.back(), tag="diagramLeft")
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right,
                               callback=lambda: self.next(), tag="diagramRight")

    def show(self):
        if not dpg.is_item_visible("diagram"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("diagram")
            dpg.split_frame()
            width = dpg.get_item_width("diagram")
            height = dpg.get_item_height("diagram")
            dpg.set_item_pos("diagram", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def show_ext(self):
        dpg.disable_item("diagramLeft")
        dpg.disable_item("diagramRight")
        if not dpg.is_item_visible("diagram"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("diagram")
            dpg.split_frame()
            width = dpg.get_item_width("diagram")
            height = dpg.get_item_height("diagram")
            dpg.set_item_pos("diagram", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def back(self):
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
        dpg.hide_item("mutation")

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
