import dearpygui.dearpygui as dpg
import config as c


class IntroSlide:
    def __init__(self):
        with dpg.window(label="Wprowadzenie", autosize=True, tag="introSlide", pos=[99999,99999], on_close=lambda: dpg.show_item("mainWindow"), height=7000):
            dpg.hide_item("introSlide")
            with open('introSlide.txt') as f:
                lines = f.readlines()

            s = ''.join(lines)

            with dpg.table(width=1440, height=640, header_row=False):
                dpg.add_table_column(width=200)
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_spacer(height=100)
                        for l in lines:
                            dpg.add_text(l, indent=20)
            with dpg.group(horizontal=True):
                #
                dpg.add_button(width=c.navBut[0], height=c.navBut[1], arrow=True, direction=dpg.mvDir_Left, indent=660)
               # dpg.add_spacer(width=500)
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right, callback=lambda: self.next())
    def show(self):
        if not dpg.is_item_visible("introSlide"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("introSlide")
            dpg.split_frame()
            width = dpg.get_item_width("introSlide")
            height = dpg.get_item_height("introSlide")
            dpg.set_item_pos("introSlide", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
            dpg.hide_item("mainWindow")

    def next(self):
        print("asggsaa")
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("dictionary")
        dpg.split_frame()
        width = dpg.get_item_width("dictionary")
        height = dpg.get_item_height("dictionary")
        dpg.set_item_pos("dictionary", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("introSlide")

