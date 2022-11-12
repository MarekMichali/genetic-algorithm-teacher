import dearpygui.dearpygui as dpg
import config
import time
import Presentation


class Dictionary:
    def __init__(self):
        self.color = (15,86,135,255)
        self.checkboxes = []
        with dpg.window(label="Dictionary", autosize=True, tag="dictionary", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("dictionary")

            with dpg.table(width=1440, height=610, header_row=False):
                dpg.add_table_column(width=200)
                dpg.add_table_column(width=200)
                #with open('gen.txt') as f:
               #     lines = f.readlines()
               # s = ''.join(lines)
                with dpg.table_row():
                    with dpg.table_cell():

                        with open('gen.txt') as f:
                            lines = f.readlines()
                            i = 0
                            for line in lines:
                                i += 1
                                if i == 3:
                                    with dpg.group(horizontal=True):
                                        dpg.add_text(line, indent=63)
                                        continue
                                with dpg.group(horizontal=True):
                                    self.checkboxes.append(dpg.add_checkbox(callback=self.show_layer))
                                    dpg.add_text(line, bullet=True)


                    with dpg.table_cell():
                        with dpg.drawlist(width=800, height=300):
                            with dpg.draw_layer():
                                dpg.draw_line((48, 50), (653, 50), color=self.color, thickness=5)
                                dpg.draw_line((50, 50), (50, 103), color=self.color, thickness=5)
                                dpg.draw_line((50, 100), (653, 100), color=self.color, thickness=5)
                                dpg.draw_line((650, 100), (650, 50), color=self.color, thickness=5)

                                dpg.draw_line((100, 50), (100, 100), color=self.color, thickness=5)
                                dpg.draw_text((64, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((150, 50), (150, 100), color=self.color, thickness=5)
                                dpg.draw_text((114, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((200, 50), (200, 100), color=self.color, thickness=5)
                                dpg.draw_text((164, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((250, 50), (250, 100), color=self.color, thickness=5)
                                dpg.draw_text((214, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((300, 50), (300, 100), color=self.color, thickness=5)
                                dpg.draw_text((264, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((350, 50), (350, 100), color=self.color, thickness=5)
                                dpg.draw_text((314, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((400, 50), (400, 100), color=self.color, thickness=5)
                                dpg.draw_text((364, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((450, 50), (450, 100), color=self.color, thickness=5)
                                dpg.draw_text((414, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((500, 50), (500, 100), color=self.color, thickness=5)
                                dpg.draw_text((464, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((550, 50), (550, 100), color=self.color, thickness=5)
                                dpg.draw_text((516, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_line((600, 50), (600, 100), color=self.color, thickness=5)
                                dpg.draw_text((564, 54), "0", color=(250, 250, 250, 255), size=50)

                                dpg.draw_text((614, 54), "0", color=(250, 250, 250, 255), size=50)

                            with dpg.draw_layer(tag="genLayer", show=False):
                                #dpg.draw_arrow((50, 70), (100, 65), color=(0, 200, 255), thickness=1, size=10)
                                dpg.draw_circle((125, 75), color=(255, 0, 0, 50), radius=38, thickness=5)

                            with dpg.draw_layer(tag="chromoLayer", show=False):
                                dpg.draw_ellipse((25, 25), (675, 125), color=(255, 0, 0, 50), thickness=5)

    def show(self):
        if not dpg.is_item_visible("dictionary"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("dictionary")
            dpg.split_frame()
            width = dpg.get_item_width("dictionary")
            height = dpg.get_item_height("dictionary")
            dpg.set_item_pos("dictionary", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def show_layer(self, sender, x):
        show_value = dpg.get_value(sender)
        i = 0
        for c in self.checkboxes:
            if c == sender:
                if i ==0:
                    dpg.configure_item("genLayer", show=show_value)
                elif i == 2 or i ==1:
                    dpg.configure_item("chromoLayer", show=show_value)
            i += 1

