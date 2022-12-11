import math
import dearpygui.dearpygui as dpg
import config as c


class SingletonCrossover(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Crossover(metaclass=SingletonCrossover):
    def __init__(self):
        self.blue = (15, 86, 135, 255)
        self.y_offset = 100
        self.x_offset = -1
        self.first_chromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.second_chromo = (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0)
        self.render_count = 0

        with dpg.window(label="Krzyżowanie", autosize=True, tag="crossover", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("crossover")
            with dpg.table(width=1440, height=640, header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        with open('data//crossover.txt', encoding="utf-8") as f:
                            lines = f.readlines()
                            for line in lines:
                                dpg.add_text(line, indent=20)

                    with dpg.table_cell():
                        dpg.add_spacer(height=50)
                        with dpg.drawlist(width=800, height=500, tag="cross_animation"):
                            with dpg.draw_layer():
                                dpg.draw_line((48, 250), (203, 250), color=self.blue, thickness=5)
                                dpg.draw_line((348, 250), (653, 250), color=self.blue, thickness=5)
                                dpg.draw_line((50, 250), (50, 303), color=self.blue, thickness=5)
                                dpg.draw_line((50, 300), (203, 300), color=self.blue, thickness=5)
                                dpg.draw_line((348, 300), (653, 300), color=self.blue, thickness=5)

                                x = 100
                                y = 250
                                allel_x = 63
                                allel_y = 254
                                counter = 0
                                for i in self.first_chromo:
                                    counter += 1
                                    if counter == 4 or counter == 5 or counter == 6:
                                        if counter == 6:
                                            dpg.draw_line((x, y), (x, y + 50), color=self.blue, thickness=5)
                                        x += 50
                                        allel_x += 50
                                        continue
                                    dpg.draw_line((x, y), (x, y + 50), color=self.blue, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y), "1",
                                                      color=(250, 250, 250, 255), size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48, 250 + self.y_offset), (203, 250 + self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((348, 250 + self.y_offset), (653, 250 + self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50, 250 + self.y_offset), (50, 303 + self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50, 300 + self.y_offset), (203, 300 + self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((348, 300 + self.y_offset), (653, 300 + self.y_offset), color=self.blue,
                                              thickness=5)
                                x = 100
                                y = 250
                                allel_x = 63
                                allel_y = 254
                                counter = 0
                                for i in self.second_chromo:
                                    counter += 1
                                    if counter == 4 or counter == 5 or counter == 6:
                                        if counter == 6:
                                            dpg.draw_line((x, y + self.y_offset), (x, y + 50 + self.y_offset),
                                                          color=self.blue, thickness=5)
                                        x += 50
                                        allel_x += 50
                                        continue
                                    dpg.draw_line((x, y + self.y_offset), (x, y + 50 + self.y_offset), color=self.blue,
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
                                dpg.draw_line((48, 50), (503, 50), color=self.blue, thickness=5)
                                dpg.draw_line((50, 50), (50, 103), color=self.blue, thickness=5)
                                dpg.draw_line((50, 100), (503, 100), color=self.blue, thickness=5)

                                x = 100
                                y = 50
                                allel_x = 63
                                allel_y = 54
                                counter = 0
                                for i in self.first_chromo:
                                    counter += 1
                                    if counter == 10:
                                        break
                                    dpg.draw_line((x, y), (x, 2 * y), color=self.blue, thickness=5)
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y), "1",
                                                      color=(250, 250, 250, 255), size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48, 50 + self.y_offset), (503, 50 + self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50, 50 + self.y_offset), (50, 103 + self.y_offset), color=self.blue,
                                              thickness=5)
                                dpg.draw_line((50, 100 + self.y_offset), (503, 100 + self.y_offset), color=self.blue,
                                              thickness=5)
                                x = 100
                                y = 50
                                allel_x = 63
                                allel_y = 54
                                counter = 0
                                for i in self.second_chromo:
                                    counter += 1
                                    if counter == 10:
                                        break
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

                                with dpg.draw_node():
                                    dpg.apply_transform(dpg.last_item(), dpg.create_translation_matrix([550, 150]))
                                    with dpg.draw_node(tag="cross_first_anim", user_data=90.0):
                                        dpg.apply_transform(dpg.last_item(),
                                                            dpg.create_rotation_matrix(
                                                                math.pi * 45.0 / 180.0, [0, 0, -1])
                                                            * dpg.create_translation_matrix([150, 0]))
                                        with dpg.draw_node(tag="cross_first_chromo", user_data=45.0):
                                            dpg.apply_transform(dpg.last_item(),
                                                                dpg.create_translation_matrix(
                                                                    [25, 0]))
                                            dpg.draw_line((0, 0), (77, 0), color=self.blue, thickness=5)
                                            dpg.draw_line((0, 0), (-77, 0), color=self.blue, thickness=5)
                                            dpg.draw_line((25, 2), (25, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((-10, -46), "0", color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((75, 2), (75, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((-60, -46), "0", color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((-25, 2), (-25, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((40 + self.x_offset, -46), "1",
                                                          color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((-75, 2), (-75, -52), color=self.blue, thickness=5)
                                            dpg.draw_line((0, -50), (77, -50), color=self.blue, thickness=5)
                                            dpg.draw_line((0, -50), (-77, -50), color=self.blue, thickness=5)

                                    with dpg.draw_node(tag="cross_second_anim", user_data=270.0):
                                        dpg.apply_transform(dpg.last_item(),
                                                            dpg.create_rotation_matrix(
                                                                math.pi * 45.0 / 180.0, [0, 0, -1])
                                                            * dpg.create_translation_matrix([150, 0]))
                                        with dpg.draw_node(tag="cross_second_chromo", user_data=45.0):
                                            dpg.apply_transform(dpg.last_item(),
                                                                dpg.create_translation_matrix([25, 0]))
                                            dpg.draw_line((0, 0), (77, 0), color=self.blue, thickness=5)
                                            dpg.draw_line((0, 0), (-77, 0), color=self.blue, thickness=5)

                                            dpg.draw_line((25, 2), (25, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((-10, -46), "0", color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((75, 2), (75, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((-60 + self.x_offset, -46), "1", color=(250, 250, 250, 255),
                                                          size=50)
                                            dpg.draw_line((-25, 2), (-25, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((40, -46), "0",
                                                          color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((-75, 2), (-75, -52), color=self.blue, thickness=5)
                                            dpg.draw_line((0, -50), (77, -50), color=self.blue, thickness=5)
                                            dpg.draw_line((0, -50), (-77, -50), color=self.blue, thickness=5)

                                with dpg.draw_node():
                                    dpg.apply_transform(dpg.last_item(), dpg.create_translation_matrix([250, 350]))

                                    with dpg.draw_node(tag="cross_third_anim", user_data=90.0):
                                        dpg.apply_transform(dpg.last_item(),
                                                            dpg.create_rotation_matrix(
                                                                math.pi * 45.0 / 180.0, [0, 0, -1])
                                                            * dpg.create_translation_matrix([150, 0]))
                                        with dpg.draw_node(tag="cross_third_chromo", user_data=45.0):
                                            dpg.apply_transform(dpg.last_item(),
                                                                dpg.create_translation_matrix([25, 0]))
                                            dpg.draw_line((0, 0), (77, 0), color=self.blue, thickness=5)
                                            dpg.draw_line((0, 0), (-77, 0), color=self.blue, thickness=5)

                                            dpg.draw_line((25, 2), (25, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((-10 + self.x_offset, -46), "1", color=(250, 250, 250, 255),
                                                          size=50)
                                            dpg.draw_line((75, 2), (75, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((-60 + self.x_offset, -46), "1", color=(250, 250, 250, 255),
                                                          size=50)
                                            dpg.draw_line((-25, 2), (-25, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((40, -46), "0",
                                                          color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((-75, 2), (-75, -52), color=self.blue, thickness=5)

                                            dpg.draw_line((0, -50), (77, -50), color=self.blue, thickness=5)
                                            dpg.draw_line((0, -50), (-77, -50), color=self.blue, thickness=5)

                                    #
                                    with dpg.draw_node(tag="cross_fourth_anim", user_data=270.0):
                                        dpg.apply_transform(dpg.last_item(),
                                                            dpg.create_rotation_matrix(
                                                                math.pi * 45.0 / 180.0, [0, 0, -1])
                                                            * dpg.create_translation_matrix([150, 0]))

                                        with dpg.draw_node(tag="cross_fourth_chromo", user_data=45.0):
                                            dpg.apply_transform(dpg.last_item(),
                                                                dpg.create_translation_matrix([25, 0]))
                                            dpg.draw_line((0, 0), (77, 0), color=self.blue, thickness=5)
                                            dpg.draw_line((0, 0), (-77, 0), color=self.blue, thickness=5)

                                            dpg.draw_line((25, 2), (25, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((-10, -46), "0", color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((75, 2), (75, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((-60 + + self.x_offset, -46), "1", color=(250, 250, 250, 255),
                                                          size=50)
                                            dpg.draw_line((-25, 2), (-25, -52), color=self.blue, thickness=5)
                                            dpg.draw_text((40, -46), "0",
                                                          color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((-75, 2), (-75, -52), color=self.blue, thickness=5)

                                            dpg.draw_line((0, -50), (77, -50), color=self.blue, thickness=5)
                                            dpg.draw_line((0, -50), (-77, -50), color=self.blue, thickness=5)

                                def animate():
                                    first_chromo_rot = dpg.get_item_user_data("cross_first_anim") + 1
                                    second_chromo_rot = dpg.get_item_user_data("cross_second_anim") + 1
                                    third_chromo_rot = dpg.get_item_user_data("cross_third_anim") + 1
                                    fourth_chromo_rot = dpg.get_item_user_data("cross_fourth_anim") + 1

                                    if first_chromo_rot == 270:
                                        self.render_count += 1
                                        if self.render_count == 270:
                                            first_chromo_rot = 90
                                            second_chromo_rot = 270
                                            third_chromo_rot = 90
                                            fourth_chromo_rot = 270
                                            self.render_count = 0
                                        else:
                                            return
                                    dpg.apply_transform("cross_first_anim",
                                                        dpg.create_rotation_matrix(
                                                            math.pi * first_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([50, 0]))
                                    dpg.set_item_user_data("cross_first_anim", first_chromo_rot)
                                    first_anim_rot = dpg.get_item_user_data("cross_first_chromo") + 3.0
                                    dpg.apply_transform("cross_first_chromo",
                                                        dpg.create_rotation_matrix(
                                                            -math.pi * first_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([25, 0]))
                                    dpg.set_item_user_data("cross_first_chromo", first_anim_rot)

                                    dpg.apply_transform("cross_second_anim",
                                                        dpg.create_rotation_matrix(
                                                            math.pi * second_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([50, 0]))
                                    dpg.set_item_user_data("cross_second_anim", second_chromo_rot)
                                    second_anim_rot = dpg.get_item_user_data("cross_second_chromo") + 3.0
                                    dpg.apply_transform("cross_second_chromo",
                                                        dpg.create_rotation_matrix(
                                                            -math.pi * second_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([25, 0]))
                                    dpg.set_item_user_data("cross_second_chromo", second_anim_rot)

                                    dpg.apply_transform("cross_third_anim",
                                                        dpg.create_rotation_matrix(
                                                            math.pi * third_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([50, 0]))
                                    dpg.set_item_user_data("cross_third_anim", third_chromo_rot)
                                    first_anim_rot = dpg.get_item_user_data("cross_third_chromo") + 3.0
                                    dpg.apply_transform("cross_third_chromo",
                                                        dpg.create_rotation_matrix(
                                                            -math.pi * third_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([25, 0]))
                                    dpg.set_item_user_data("cross_third_chromo", first_anim_rot)

                                    dpg.apply_transform("cross_fourth_anim",
                                                        dpg.create_rotation_matrix(
                                                            math.pi * fourth_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([50, 0]))
                                    dpg.set_item_user_data("cross_fourth_anim", fourth_chromo_rot)
                                    second_anim_rot = dpg.get_item_user_data("cross_fourth_chromo") + 3.0
                                    dpg.apply_transform("cross_fourth_chromo",
                                                        dpg.create_rotation_matrix(
                                                            -math.pi * fourth_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([25, 0]))
                                    dpg.set_item_user_data("cross_fourth_chromo", second_anim_rot)

                                with dpg.item_handler_registry(tag="cross_item_registry"):
                                    dpg.add_item_visible_handler(callback=animate)
                                dpg.bind_item_handler_registry("cross_animation", dpg.last_container())

            with dpg.group(horizontal=True):
                dpg.add_button(width=c.navBut[0], height=c.navBut[1], arrow=True, direction=dpg.mvDir_Left, indent=660,
                               callback=lambda: self.back(), tag="crossoverLeft")
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right,
                               callback=lambda: self.next(), tag="crossoverRight")

    def show(self):
        if not dpg.is_item_visible("crossover"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.split_frame()
            width = dpg.get_item_width("crossover")
            height = dpg.get_item_height("crossover")
            dpg.set_item_pos("crossover", dpg.get_item_pos("selector"))
            dpg.show_item("crossover")
            dpg.hide_item("mainWindow")

    def show_ext(self):
        if not dpg.is_item_visible("crossover"):
            dpg.disable_item("crossoverLeft")
            dpg.disable_item("crossoverRight")
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("crossover")
            dpg.split_frame()
            width = dpg.get_item_width("crossover")
            height = dpg.get_item_height("crossover")
            dpg.set_item_pos("crossover", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def next(self):
        dpg.enable_item("mutationLeft")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.split_frame()
        width = dpg.get_item_width("mutation")
        height = dpg.get_item_height("mutation")
        dpg.set_item_pos("mutation", dpg.get_item_pos("crossover"))
        dpg.show_item("mutation")
        dpg.hide_item("crossover")

    def back(self):
        dpg.enable_item("selectorLeft")
        dpg.enable_item("selectorRight")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.split_frame()
        width = dpg.get_item_width("selector")
        height = dpg.get_item_height("selector")
        dpg.set_item_pos("selector", dpg.get_item_pos("crossover"))
        dpg.show_item("selector")
        dpg.hide_item("crossover")
