import dearpygui.dearpygui as dpg
import config
import PresentationInterface


class SingletonDiagram(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Diagram(PresentationInterface.PresentationInterface, config.Config, metaclass=SingletonDiagram):
    def __init__(self):
        self.chromo_color = (15, 86, 135, 255)
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
                        dpg.add_spacer(height=10)
                        dpg.add_text("Schemat działania algorytmu genetycznego", indent=510)
                        with dpg.drawlist(width=1400, height=590):
                            height = 50
                            width = 271

                            dpg.draw_text([width - 100, height + 15], "Start", size=20)
                            dpg.draw_arrow([width + 65, height + 25], [width - 45, height + 25], thickness=5,
                                           color=self.chromo_color, size=10)

                            dpg.draw_rectangle([width + 70, height], [width + 370, height + 50],
                                               thickness=5, color=self.chromo_color, tag="diagStart")
                            dpg.draw_text([width + 125, height + 5], "Generowanie populacji", size=20)
                            dpg.draw_text([width + 165, height + 25], "poczatkowej", size=20)
                            dpg.draw_line([width + 220, height + 50], [width + 220, height + 225], thickness=5,
                                          color=self.chromo_color)
                            dpg.draw_arrow([width + 265, height + 225], [width + 218, height + 225], thickness=5,
                                           color=self.chromo_color, size=10)

                            dpg.draw_rectangle([width + 470, height], [width + 770, height + 50],
                                               thickness=5, color=self.chromo_color, tag="diagCross")
                            dpg.draw_text([width + 570, height + 15], "Krzyżowanie", size=20)
                            dpg.draw_arrow([width + 620, height + 96], [width + 620, height + 50], thickness=5,
                                           color=self.chromo_color, size=10)

                            dpg.draw_rectangle([width + 470, height + 100], [width + 770, height + 150],
                                               thickness=5, color=self.chromo_color, tag="diagMut")
                            dpg.draw_text([width + 588, height + 115], "Mutacja", size=20)
                            dpg.draw_line([width + 620, height + 225], [width + 620, height + 150], thickness=5,
                                          color=self.chromo_color)
                            dpg.draw_arrow([width + 575, height + 225], [width + 623, height + 225], thickness=5,
                                           color=self.chromo_color, size=10)

                            dpg.draw_rectangle([width + 270, height + 200], [width + 570, height + 250],
                                               thickness=5, color=self.chromo_color, tag="diagSel")
                            dpg.draw_text([width + 315, height + 215], "Ocena populacji i selekcja", size=20)
                            dpg.draw_arrow([width + 420, height + 296], [width + 420, height + 250], thickness=5,
                                           color=self.chromo_color, size=10)

                            dpg.draw_quad([width + 420, height + 300], [width + 520, height + 400],
                                          [width + 420, height + 500], [width + 320, height + 400],
                                          thickness=5, color=self.chromo_color, tag="diagDec")
                            dpg.draw_text([width + 393, height + 375], "Koniec", size=20)
                            dpg.draw_text([width + 385, height + 395], "ewolucji?", size=20)

                            dpg.draw_text([width + 520, height + 370], "Nie", size=20)
                            dpg.draw_text([width + 290, height + 370], "Tak", size=20)
                            dpg.draw_line([width + 520, height + 400], [width + 863, height + 400], thickness=5,
                                          color=self.chromo_color)
                            dpg.draw_line([width + 860, height + 400], [width + 860, height + 25], thickness=5,
                                          color=self.chromo_color)
                            dpg.draw_arrow([width + 775, height + 25], [width + 863, height + 25], thickness=5,
                                           color=self.chromo_color, size=10)
                            dpg.draw_arrow([width + 120, height + 400], [width + 320, height + 400], thickness=5,
                                           color=self.chromo_color, size=10)
                            dpg.draw_text([width + 60, height + 390], "Stop", size=20)

            with dpg.group(horizontal=True):
                dpg.add_button(width=self.navBut[0], height=self.navBut[1], arrow=True, direction=dpg.mvDir_Left,
                               indent=660, callback=lambda: self.back(), tag="diagramLeft")
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right,
                               callback=lambda: self.next(), tag="diagramRight")

    def show(self):
        if not dpg.is_item_visible("diagram"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.split_frame()
            width = dpg.get_item_width("diagram")
            height = dpg.get_item_height("diagram")
            dpg.set_item_pos("diagram", dpg.get_item_pos("introSlide"))
            dpg.show_item("diagram")
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
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.split_frame()
        width = dpg.get_item_width("introSlide")
        height = dpg.get_item_height("introSlide")
        dpg.set_item_pos("introSlide", dpg.get_item_pos("diagram"))
        dpg.show_item("introSlide")
        dpg.hide_item("diagram")

    def next(self):
        dpg.enable_item("dictionaryLeft")
        dpg.enable_item("dictionaryRight")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.split_frame()
        width = dpg.get_item_width("dictionary")
        height = dpg.get_item_height("dictionary")
        dpg.set_item_pos("dictionary", dpg.get_item_pos("diagram"))
        dpg.show_item("dictionary")
        dpg.hide_item("diagram")
