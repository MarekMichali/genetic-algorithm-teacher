import math
import dearpygui.dearpygui as dpg
import config as c


class SingletonMutation(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Mutation(metaclass=SingletonMutation):
    def __init__(self):
        self.blue = (15, 86, 135, 255)
        self.y_offset = 100
        self.x_offset = -1
        self.first_chromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.second_chromo = (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0)
        self.renderCount = 0
        with dpg.window(label="Mutacja", autosize=True, tag="mutation", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("mutation")
            with dpg.table(width=1440, height=640, header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=20)
                        with open('data//mutation.txt') as f:
                            lines = f.readlines()
                            for line in lines:
                                dpg.add_text(line, indent=20)

                    with dpg.table_cell():
                        dpg.add_spacer(height=50)
                        with dpg.drawlist(width=800, height=500, tag="mutation_animation"):
                            with dpg.draw_layer():
                                dpg.draw_line((48, 50), (653, 50), color=self.blue, thickness=5)
                                dpg.draw_line((50, 50), (50, 103), color=self.blue, thickness=5)
                                dpg.draw_line((50, 100), (653, 100), color=self.blue, thickness=5)

                                x = 100
                                y = 50
                                allel_x = 63
                                allel_y = 54
                                counter = 0
                                for i in self.first_chromo:
                                    counter += 1
                                    dpg.draw_line((x, y), (x, 2 * y), color=self.blue, thickness=5)
                                    if counter == 9 or counter == 11:
                                        x += 50
                                        allel_x += 50
                                        continue
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y), "1",
                                                      color=(250, 250, 250, 255), size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer():
                                dpg.draw_line((48, 150), (653, 150), color=self.blue, thickness=5)
                                dpg.draw_line((50, 150), (50, 203), color=self.blue, thickness=5)
                                dpg.draw_line((50, 200), (653, 200), color=self.blue, thickness=5)

                                x = 100
                                y = 150
                                allel_x = 63
                                allel_y = 154
                                counter = 0
                                for i in self.second_chromo:
                                    counter += 1
                                    dpg.draw_line((x, y), (x, 50 + y), color=self.blue, thickness=5)
                                    #if counter == 9 or counter == 11:
                                     #   x += 50
                                      #  allel_x += 50
                                       # continue
                                    if i == 0:
                                        dpg.draw_text((allel_x, allel_y), "0", color=(250, 250, 250, 255), size=50)
                                    else:
                                        dpg.draw_text((allel_x + self.x_offset, allel_y), "1",
                                                      color=(250, 250, 250, 255), size=50)
                                    x += 50
                                    allel_x += 50

                            with dpg.draw_layer():
                                with dpg.draw_node():
                                    dpg.apply_transform(dpg.last_item(), dpg.create_translation_matrix([550, 100]))
                                    with dpg.draw_node(tag="mutation_first_anim", user_data=179.0):
                                        dpg.apply_transform(dpg.last_item(),
                                                            dpg.create_rotation_matrix(
                                                                math.pi * 45.0 / 180.0, [0, 0, -1])
                                                            * dpg.create_translation_matrix([150, 0]))

                                        with dpg.draw_node(tag="mutation_first_chromo", user_data=45.0):
                                            dpg.apply_transform(dpg.last_item(), dpg.create_translation_matrix([25, 0]))
                                            dpg.draw_line((-23, 0), (-77, 0), color=self.blue, thickness=5)
                                            dpg.draw_text((-60, -46), "0", color=(250, 250, 250, 255), size=50)
                                            dpg.draw_line((-25, 2), (-25, -52), color=self.blue, thickness=5)
                                            dpg.draw_line((-75, 2), (-75, -52), color=self.blue, thickness=5)
                                            dpg.draw_line((-23, -50), (-77, -50), color=self.blue, thickness=5)

                                    with dpg.draw_node(tag="mutation_second_anim", user_data=359.0):
                                        dpg.apply_transform(dpg.last_item(),
                                                            dpg.create_rotation_matrix(
                                                                math.pi * 45.0 / 180.0, [0, 0, -1])
                                                            * dpg.create_translation_matrix([150, 0]))

                                        with dpg.draw_node(tag="mutation_second_chromo", user_data=45.0):
                                            dpg.apply_transform(dpg.last_item(), dpg.create_translation_matrix([25, 0]))
                                            dpg.draw_line((-23, 0), (-77, 0), color=self.blue, thickness=5)
                                            dpg.draw_text((-60 + self.x_offset, -46), "1", color=(250, 250, 250, 255),
                                                          size=50)
                                            dpg.draw_line((-25, 2), (-25, -52), color=self.blue, thickness=5)
                                            dpg.draw_line((-75, 2), (-75, -52), color=self.blue, thickness=5)
                                            dpg.draw_line((-23, -50), (-77, -50), color=self.blue, thickness=5)

                            with dpg.draw_layer(tag="shadowMut", show=False):
                                dpg.draw_rectangle((350, 140), (401, 210), color=(60, 60, 61, 200),
                                                   fill=(60, 60, 61, 200))
                            with dpg.draw_layer(tag="hideMut", show=False):
                                dpg.draw_rectangle((353, 153), (397, 198), color=(60, 60, 61, 255),
                                                   fill=(60, 60, 61, 255))
                            with dpg.draw_layer(tag="showMut", show=False):
                                dpg.draw_text((363, -46 + 200), "1", color=(250, 250, 250, 255), size=50)
                            with dpg.draw_layer(tag="shadowMut2", show=False):
                                dpg.draw_rectangle((353, 153), (397, 198), color=(60, 60, 61, 200),
                                                   fill=(60, 60, 61, 200))

                                def animate():
                                    first_chromo_rot = dpg.get_item_user_data("mutation_first_anim") + 1
                                    second_chromo_rot = dpg.get_item_user_data("mutation_second_anim") + 1


                                    if first_chromo_rot == 240:
                                        dpg.configure_item("shadowMut", show=True)
                                    if first_chromo_rot == 300:
                                        dpg.configure_item("hideMut", show=True)
                                        dpg.configure_item("showMut", show=True)
                                        dpg.configure_item("shadowMut2", show=True)
                                    if first_chromo_rot == 360:
                                        dpg.configure_item("shadowMut", show=False)
                                        dpg.configure_item("shadowMut2", show=False)
                                    if first_chromo_rot == 361:
                                        self.renderCount += 1
                                        if self.renderCount == 360:
                                            first_chromo_rot = 179
                                            second_chromo_rot = 359
                                            self.renderCount = 0
                                            dpg.configure_item("hideMut", show=False)
                                            dpg.configure_item("showMut", show=False)
                                            dpg.configure_item("shadowMut2", show=False)
                                            dpg.configure_item("shadowMut", show=False)
                                        else:
                                            return
                                    dpg.apply_transform("mutation_first_anim",
                                                        dpg.create_rotation_matrix(
                                                            math.pi * first_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([50, 0]))
                                    dpg.set_item_user_data("mutation_first_anim", first_chromo_rot)
                                    first_anim_rot = dpg.get_item_user_data("mutation_first_chromo") + 3.0
                                    dpg.apply_transform("mutation_first_chromo",
                                                        dpg.create_rotation_matrix(
                                                            -math.pi * first_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([25, 0]))
                                    dpg.set_item_user_data("mutation_first_chromo", first_anim_rot)

                                    dpg.apply_transform("mutation_second_anim",
                                                        dpg.create_rotation_matrix(
                                                            math.pi * second_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([50, 0]))
                                    dpg.set_item_user_data("mutation_second_anim", second_chromo_rot)
                                    second_anim_rot = dpg.get_item_user_data("mutation_second_chromo") + 3.0
                                    dpg.apply_transform("mutation_second_chromo",
                                                        dpg.create_rotation_matrix(
                                                            -math.pi * second_chromo_rot / 180.0, [0, 0, -1])
                                                        * dpg.create_translation_matrix([25, 0]))
                                    dpg.set_item_user_data("mutation_second_chromo", second_anim_rot)

                                with dpg.item_handler_registry(tag="mutation_item_registry"):
                                    dpg.add_item_visible_handler(callback=animate)
                                dpg.bind_item_handler_registry("mutation_animation", dpg.last_container())

            with dpg.group(horizontal=True):
                dpg.add_button(width=c.navBut[0], height=c.navBut[1], arrow=True, direction=dpg.mvDir_Left, indent=660,
                               callback=lambda: self.back(), tag="mutationLeft")
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right, enabled=False)

    def show(self):
        if not dpg.is_item_visible("mutation"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("mutation")
            dpg.split_frame()
            width = dpg.get_item_width("mutation")
            height = dpg.get_item_height("mutation")
            dpg.set_item_pos("mutation", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def show_ext(self):
        dpg.disable_item("mutationLeft")
        if not dpg.is_item_visible("mutation"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("mutation")
            dpg.split_frame()
            width = dpg.get_item_width("mutation")
            height = dpg.get_item_height("mutation")
            dpg.set_item_pos("mutation", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
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
