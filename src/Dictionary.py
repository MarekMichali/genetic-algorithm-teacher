import dearpygui.dearpygui as dpg
import config
import time
import Presentation
import config as c


class Dictionary:
    def __init__(self):
        self.color = (15,86,135,255)
        self.checkboxes = []
        self.yOffset = 100
        self.xOneOffset = 5
        self.firstChromo = (0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1)
        self.secondChromo = (1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0)
        with dpg.window(label="Dictionary", autosize=True, tag="dictionary", pos=[99999, 99999],
                        on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("dictionary")
            with open('dictionarySlide.txt') as f:
                lines = f.readlines()

            s = ''.join(lines)

            #or line in lines:
            #   dpg.add_text(line, indent=20)

            with dpg.table(width=1440, height=610, header_row=False, borders_innerV=True, borders_outerV=True, borders_innerH=True, borders_outerH=True):
                dpg.add_table_column()
                dpg.add_table_column()
                #with open('gen.txt') as f:
               #     lines = f.readlines()
               # s = ''.join(lines)
                with dpg.table_row():
                    with dpg.table_cell():
                        #dpg.add_spacer(height=20)
                        with open('dictionarySlide.txt') as f:
                            lines = f.readlines()
                            for line in lines:
                                dpg.add_text(line, indent=20)
                        dpg.add_spacer(height=10)
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
                                    self.checkboxes.append(dpg.add_checkbox(callback=self.show_layer))
                                    dpg.add_text(line, bullet=True)


                    with dpg.table_cell():
                        dpg.add_spacer(height=100)
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

                            with dpg.draw_layer(tag="genLayer", show=False):
                                #dpg.draw_arrow((50, 70), (100, 65), color=(0, 200, 255), thickness=1, size=10)
                                dpg.draw_circle((125, 75), color=(255, 0, 0, 100), radius=38, thickness=5)

                            with dpg.draw_layer(tag="chromoLayer", show=False):
                                dpg.draw_ellipse((25, 25), (675, 125), color=(255, 0, 0, 100), thickness=5)

                            with dpg.draw_layer(tag="popuLayer", show=False):
                                dpg.draw_ellipse((25, 25), (675, 125 + self.yOffset), color=(255, 0, 0, 100), thickness=5)
                    with dpg.table_cell(height=10):
                        dpg.add_text("dupa")
            with dpg.group(horizontal=True):
                #
                dpg.add_button(width=c.navBut[0], height=c.navBut[1], arrow=True, direction=dpg.mvDir_Left, indent=660)
                # dpg.add_spacer(width=500)
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right,
                               callback=lambda: self.next())

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
                elif i == 2 or i == 1:
                    show_value = dpg.get_value(self.checkboxes[2]) or dpg.get_value(self.checkboxes[1])
                    dpg.configure_item("chromoLayer", show=show_value)
                elif i == 3:
                    dpg.configure_item("popuLayer", show=show_value)
            i += 1

    def next(self):
        print("asggsaa")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("fitness")
        dpg.split_frame()
        width = dpg.get_item_width("fitness")
        height = dpg.get_item_height("fitness")
        dpg.set_item_pos("fitness", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("dictionary")

