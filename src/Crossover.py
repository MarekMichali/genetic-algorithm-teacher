import math
from datetime import datetime

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
        self.renderCount = 0
        with dpg.window(label="Krzyzowanie", autosize=True, tag="crossover", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("crossover")
            with dpg.table(width=1440, height=610, header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        with open('..//crossover.txt') as f:
                            lines = f.readlines()
                            i = 0
                            for line in lines:
                                dpg.add_text(line, indent=20)

                    with dpg.table_cell():
                        with dpg.drawlist(width=800, height=500, tag="_demo_advanced_drawing"):
                            with dpg.draw_layer():
                                dpg.draw_line((48, 50), (503, 50), color=self.color, thickness=5)
                                dpg.draw_line((50, 50), (50, 103), color=self.color, thickness=5)
                                dpg.draw_line((50, 100), (503, 100), color=self.color, thickness=5)


                                x = 100
                                y = 50
                                allelX = 64
                                allelY = 54
                                counter = 0
                                for i in self.firstChromo:
                                    counter += 1
                                    if counter == 10:
                                        break
                                    dpg.draw_line((x, y), (x, 2*y), color=self.color, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allelX, allelY), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allelX + self.xOneOffset, allelY), "1", color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allelX += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48, 50 + self.yOffset), (503, 50 + self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50, 50 + self.yOffset), (50, 103 + self.yOffset), color=self.color,
                                              thickness=5)
                                dpg.draw_line((50, 100 + self.yOffset), (503, 100 + self.yOffset), color=self.color,
                                              thickness=5)
                                x = 100
                                y = 50
                                allelX = 64
                                allelY = 54
                                counter = 0
                                for i in self.secondChromo:
                                    counter += 1
                                    if counter == 10:
                                        break
                                    dpg.draw_line((x, y +  self.yOffset), (x, 2 * y +  self.yOffset), color=self.color, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allelX, allelY + self.yOffset), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allelX + self.xOneOffset, allelY + self.yOffset), "1",
                                                      color=(250, 250, 250, 255),
                                                      size=50)
                                    x += 50
                                    allelX += 50

                                with dpg.draw_node(tag="_drawing_sun"):
                                    dpg.apply_transform(dpg.last_item(), dpg.create_translation_matrix([550, 150]))
                                    #dpg.draw_circle([0, 0], 5, color=[0, 0, 0], fill=[0, 255, 0]) #sun
                                    with dpg.draw_node(tag="_drawing_planet1", user_data=90.0):
                                        dpg.apply_transform(dpg.last_item(),
                                                            dpg.create_rotation_matrix(math.pi * 45.0 / 180.0, [0, 0,-1]) * dpg.create_translation_matrix([150, 0]))
                                       # dpg.draw_circle([0, 0], 10, color=[0, 255, 0], fill=[0, 255, 0]) #planeta
                                        #dpg.draw_circle([0, 0], 25, color=[255, 0, 255])

                                        with dpg.draw_node(tag="_drawing_moon1", user_data=45.0):
                                            dpg.apply_transform(dpg.last_item(),
                                                                 dpg.create_translation_matrix(
                                                                    [25, 0]))
                                           # dpg.draw_circle([0, 0], 5, color=[255, 0, 255], fill=[255, 0, 255]) # ksiezyc
                                            dpg.draw_line((0, 0), (77, 0), color=self.color, thickness=5)
                                            dpg.draw_line((0, 0), (-77, 0), color=self.color, thickness=5)

                                            dpg.draw_line((25, 2), (25, -52), color=self.color, thickness=5)
                                            dpg.draw_text((-10, -46), "0", color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((75, 2), (75, -52), color=self.color, thickness=5)
                                            dpg.draw_text((-60, -46), "0", color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((-25, 2), (-25, -52), color=self.color, thickness=5)
                                            dpg.draw_text((40 + self.xOneOffset, -46 ), "1",
                                                          color=(250, 250, 250, 255),
                                                          size=50)
                                            dpg.draw_line((-75, 2), (-75, -52), color=self.color, thickness=5)

                                            dpg.draw_line((0, -50), (77, -50), color=self.color, thickness=5)
                                            dpg.draw_line((0, -50), (-77, -50), color=self.color, thickness=5)

                                    #
                                    with dpg.draw_node(tag="_drawing_planet2", user_data=270.0):
                                        dpg.apply_transform(dpg.last_item(),
                                                            dpg.create_rotation_matrix(math.pi * 45.0 / 180.0, [0, 0,-1]) * dpg.create_translation_matrix([150, 0]))
                                       # dpg.draw_circle([0, 0], 10, color=[0, 255, 0], fill=[0, 255, 0]) #planeta
                                        #dpg.draw_circle([0, 0], 25, color=[255, 0, 255])

                                        with dpg.draw_node(tag="_drawing_moon2", user_data=45.0):
                                            dpg.apply_transform(dpg.last_item(),
                                                                 dpg.create_translation_matrix(
                                                                    [25, 0]))
                                            #dpg.draw_circle([0, 0], 5, color=[255, 0, 255], fill=[255, 0, 255]) # ksiezyc
                                            dpg.draw_line((0, 0), (77, 0), color=self.color, thickness=5)
                                            dpg.draw_line((0, 0), (-77, 0), color=self.color, thickness=5)

                                            dpg.draw_line((25, 2), (25, -52), color=self.color, thickness=5)
                                            dpg.draw_text((-10, -46), "0", color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((75, 2), (75, -52), color=self.color, thickness=5)
                                            dpg.draw_text((-60 + self.xOneOffset, -46), "1", color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((-25, 2), (-25, -52), color=self.color, thickness=5)
                                            dpg.draw_text((40, -46), "0",
                                                          color=(250, 250, 250, 255),
                                                          size=50)
                                            dpg.draw_line((-75, 2), (-75, -52), color=self.color, thickness=5)

                                            dpg.draw_line((0, -50), (77, -50), color=self.color, thickness=5)
                                            dpg.draw_line((0, -50), (-77, -50), color=self.color, thickness=5)

                                def _demo_live_drawing():
                                    planet_rot1 = dpg.get_item_user_data("_drawing_planet1") + 1
                                    planet_rot2 = dpg.get_item_user_data("_drawing_planet2") + 1
                                   # print(planet_rot2)
                                    if planet_rot1 == 270:
                                        self.renderCount += 1
                                        if self.renderCount == 270:
                                            planet_rot1 = 90
                                            planet_rot2 = 270
                                            self.renderCount = 0
                                        else:
                                            return
                                    dpg.apply_transform("_drawing_planet1",
                                                        dpg.create_rotation_matrix(math.pi * planet_rot1 / 180.0, [0, 0,
                                                                                                                   -1]) * dpg.create_translation_matrix(
                                                            [50, 0]))
                                    dpg.set_item_user_data("_drawing_planet1", planet_rot1)
                                    moon_rot1 = dpg.get_item_user_data("_drawing_moon1") + 3.0
                                   # print(moon_rot1)

                                    dpg.apply_transform("_drawing_moon1",
                                                        dpg.create_rotation_matrix(-math.pi * planet_rot1 / 180.0, [0, 0,-1]) * dpg.create_translation_matrix([25, 0]))
                                    #print(dpg.create_rotation_matrix(-math.pi * planet_rot1 / 180.0, [0, 0,-1]) * dpg.create_translation_matrix([25, 0]) )
                                    dpg.set_item_user_data("_drawing_moon1", moon_rot1)
                                    #

                                    dpg.apply_transform("_drawing_planet2",
                                                        dpg.create_rotation_matrix(math.pi * planet_rot2 / 180.0, [0, 0,
                                                                                                                   -1]) * dpg.create_translation_matrix(
                                                            [50, 0]))
                                    dpg.set_item_user_data("_drawing_planet2", planet_rot2)
                                    moon_rot2 = dpg.get_item_user_data("_drawing_moon2") + 3.0
                                    dpg.apply_transform("_drawing_moon2",
                                                        dpg.create_rotation_matrix(-math.pi * planet_rot2 / 180.0,
                                                                                   [0, 0,
                                                                                    -1]) * dpg.create_translation_matrix(
                                                            [25, 0]))
                                   # print(dpg.create_rotation_matrix(math.pi * moon_rot2 / 180.0, [0, 0, -1]))
                                    dpg.set_item_user_data("_drawing_moon2", moon_rot2)



                                with dpg.item_handler_registry(tag="__demo_item_reg6"):
                                    dpg.add_item_visible_handler(callback=_demo_live_drawing)
                                dpg.bind_item_handler_registry("_demo_advanced_drawing", dpg.last_container())
                                #_demo_live_drawing()
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
