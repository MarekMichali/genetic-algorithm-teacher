import dearpygui.dearpygui as dpg
import config
import time
import Presentation


class Crossover:
    def __init__(self):
        self.color = (15, 86, 135, 255)
        self.checkboxes = []
        self.yOffset = 100
        self.xOneOffset = 5
        self.firstChromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.secondChromo = (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0)
        with dpg.window(label="Krzyzowanie", autosize=True, tag="crossover", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("crossover")
            with dpg.table(width=1440, height=610, header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        with open('gen.txt') as f:
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

                                    dpg.add_text(line, bullet=True)

                    with dpg.table_cell():
                        with dpg.drawlist(width=800, height=500):
                            with dpg.draw_layer():
                                dpg.draw_line((48, 50), (653, 50), color=self.color, thickness=5)
                                dpg.draw_line((50, 50), (50, 103), color=self.color, thickness=5)
                                dpg.draw_line((50, 100), (653, 100), color=self.color, thickness=5)

                                x = 100
                                y = 50
                                allelX = 64
                                allelY = 54
                                for i in self.firstChromo:
                                    dpg.draw_line((x, y), (x, 2*y), color=self.color, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allelX, allelY), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allelX + self.xOneOffset, allelY), "1", color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allelX += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48, 50 + self.yOffset), (653, 50 + self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50, 50 + self.yOffset), (50, 103 + self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50, 100 + self.yOffset), (653, 100 + self.yOffset), color=self.color,
                                              thickness=5)
                                x = 100
                                y = 50
                                allelX = 64
                                allelY = 54
                                for i in self.secondChromo:
                                    dpg.draw_line((x, y +  self.yOffset), (x, 2 * y +  self.yOffset), color=self.color, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allelX, allelY + self.yOffset), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allelX + self.xOneOffset, allelY + self.yOffset), "1",
                                                      color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allelX += 50





    def show(self):
        if not dpg.is_item_visible("crossover"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("crossover")
            dpg.split_frame()
            width = dpg.get_item_width("crossover")
            height = dpg.get_item_height("crossover")
            dpg.set_item_pos("crossover", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")