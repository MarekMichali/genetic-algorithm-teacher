import dearpygui.dearpygui as dpg
import config as c
import time
import Presentation


class Fitness:
    def __init__(self):
        self.color = (15,86,135,255)
        self.checkboxes = []
        self.yOffset = 100
        self.xOneOffset = 5
        self.xMove = 200
        self.firstChromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.secondChromo = (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0)
        self.thirdChromo = (1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0)
        self.fourthChromo = (0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1)
        with dpg.window(label="Fitness", autosize=True, tag="fitness", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("fitness")
            with open('fitness.txt') as f:
                lines = f.readlines()

            s = ''.join(lines)
            #dpg.add_text(s)
            #for l in lines:
                #dpg.add_text(l, indent=20)
            with dpg.table(width=1440, height=640, header_row=False):
                dpg.add_table_column(width_fixed=True, init_width_or_weight=516)
                dpg.add_table_column(init_width_or_weight=740)
                #with open('gen.txt') as f:
               #     lines = f.readlines()
               # s = ''.join(lines)
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        with open('fitness.txt') as f:
                            lines = f.readlines()

                        s = ''.join(lines)
                        # dpg.add_text(s)
                        for l in lines:
                            dpg.add_text(l, indent=20)
                        dpg.add_spacer(height=20)
                        with open('fitnessExamples.txt') as f:
                            lines = f.readlines()
                            i = 0
                            self.checkboxes.append((dpg.add_radio_button(lines, callback=self.wartosc)))



                    with dpg.table_cell():
                        with dpg.drawlist(width=1440, height=500):
                            with dpg.draw_layer():
                                dpg.draw_line((48 + self.xMove, 50), (653 + self.xMove, 50), color=self.color, thickness=5)
                                dpg.draw_line((50 + self.xMove, 50), (50 + self.xMove, 103), color=self.color, thickness=5)
                                dpg.draw_line((50 + self.xMove, 100), (653 + self.xMove, 100), color=self.color, thickness=5)

                                x = 100 + self.xMove
                                y = 50
                                allelX = 64 + self.xMove
                                allelY = 54
                                counter = 11
                                for i in self.firstChromo:
                                    number = pow(2,counter)
                                  #  dpg.draw_text((allelX + 5, allelY - 25), number, color=(250, 250, 250, 255),
                                   #               size=15)
                                    counter -= 1
                                    dpg.draw_line((x, y), (x, 2 * y), color=self.color, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allelX, allelY), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allelX + self.xOneOffset, allelY), "1",
                                                      color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allelX += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48 + self.xMove, 50 + self.yOffset), (653 + self.xMove, 50 + self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50 + self.xMove, 50 + self.yOffset), (50 + self.xMove, 103 + self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50 + self.xMove, 100 + self.yOffset), (653 + self.xMove, 100 + self.yOffset), color=self.color,
                                              thickness=5)
                                x = 100 + self.xMove
                                y = 50
                                allelX = 64 + self.xMove
                                allelY = 54
                                for i in self.secondChromo:
                                    dpg.draw_line((x, y + self.yOffset), (x, 2 * y + self.yOffset), color=self.color,
                                                  thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allelX, allelY + self.yOffset), "0", color=(250, 250, 250, 255),
                                                      size=50)
                                    else:
                                        dpg.draw_text((allelX + self.xOneOffset, allelY + self.yOffset), "1",
                                                      color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allelX += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48 + self.xMove, 50 + 2*self.yOffset), (653 + self.xMove, 50 + 2*self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50 + self.xMove, 50 + 2*self.yOffset), (50 + self.xMove, 103 + 2*self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50 + self.xMove, 100 + 2*self.yOffset), (653 + self.xMove, 100 + 2*self.yOffset), color=self.color,
                                              thickness=5)
                                x = 100 + self.xMove
                                y = 50
                                allelX = 64 + self.xMove
                                allelY = 54
                                for i in self.thirdChromo:
                                    dpg.draw_line((x, y + 2*self.yOffset), (x, 2 * y + 2*self.yOffset), color=self.color,
                                                  thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allelX, allelY + 2*self.yOffset), "0", color=(250, 250, 250, 255),
                                                      size=50)
                                    else:
                                        dpg.draw_text((allelX + self.xOneOffset, allelY + 2*self.yOffset), "1",
                                                      color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allelX += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48 + self.xMove, 50 + 3*self.yOffset), (653 + self.xMove, 50 + 3*self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50 + self.xMove, 50 + 3*self.yOffset), (50 + self.xMove, 103 + 3*self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50 + self.xMove, 100 + 3*self.yOffset), (653 + self.xMove, 100 + 3*self.yOffset), color=self.color,
                                              thickness=5)
                                x = 100 + self.xMove
                                y = 50
                                allelX = 64 + self.xMove
                                allelY = 54
                                for i in self.fourthChromo:
                                    dpg.draw_line((x, y + 3*self.yOffset), (x, 2 * y + 3*self.yOffset), color=self.color,
                                                  thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allelX, allelY + 3*self.yOffset), "0", color=(250, 250, 250, 255),
                                                      size=50)
                                    else:
                                        dpg.draw_text((allelX + self.xOneOffset, allelY + 3*self.yOffset), "1",
                                                      color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allelX += 50

                            with dpg.draw_layer(tag="arrowsLayer", show=True):
                                dpg.draw_arrow((-25 + self.xMove, 75), (25 + self.xMove, 75), color=(0, 200, 255), thickness=5, size=10)
                               # dpg.draw_circle((125 + self.xMove, 75), color=(255, 0, 0, 100), radius=38, thickness=5)
                                dpg.draw_arrow((-25 + self.xMove, 75 + self.yOffset), (25 + self.xMove, 75 + self.yOffset), color=(0, 200, 255),
                                               thickness=5, size=10)
                                dpg.draw_arrow((-25 + self.xMove, 75 + 2*self.yOffset), (25 + self.xMove, 75 + 2*self.yOffset), color=(0, 200, 255),
                                               thickness=5, size=10)
                                dpg.draw_arrow((-25 + self.xMove, 75 + 3*self.yOffset), (25 + self.xMove, 75 + 3*self.yOffset), color=(0, 200, 255),
                                               thickness=5, size=10)
                            with dpg.draw_layer(tag="firstRadiLayer", show=True):
                                dpg.draw_text((- 70 + self.xMove, 54), "4", color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 70 + self.xMove, 54 + self.yOffset), "6", color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 70 + self.xMove, 54 + 2*self.yOffset), "5", color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 70 + self.xMove, 54 + 3*self.yOffset), "7", color=(250, 250, 250, 255), size=50)
                            with dpg.draw_layer(tag="secondRadiLayer", show=False):
                                dpg.draw_text((- 110 + self.xMove, 54), "401", color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 150 + self.xMove, 54 + self.yOffset), "3356", color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 150 + self.xMove, 54 + 2*self.yOffset), "2834", color=(250, 250, 250, 255), size=50)
                                dpg.draw_text((- 137 + self.xMove, 54 + 3*self.yOffset), "1259", color=(250, 250, 250, 255), size=50)

            with dpg.group(horizontal=True):
                dpg.add_button(width=c.navBut[0], height=c.navBut[1], arrow=True, direction=dpg.mvDir_Left, indent=660, callback=lambda: self.back())
                # dpg.add_spacer(width=500)
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right,
                           callback=lambda: self.next())



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

    def wartosc(self, app_data, user_data):
        print((user_data))
        if "ilosci" in user_data:
            dpg.configure_item("firstRadiLayer", show=True)
            dpg.configure_item("secondRadiLayer", show=False)
        else:
             dpg.configure_item("firstRadiLayer", show=False)
             dpg.configure_item("secondRadiLayer", show=True)

    def next(self):
        print("asggsaa")
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
        print("asggsaa")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("dictionary")
        dpg.split_frame()
        width = dpg.get_item_width("dictionary")
        height = dpg.get_item_height("dictionary")
        dpg.set_item_pos("dictionary", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("fitness")