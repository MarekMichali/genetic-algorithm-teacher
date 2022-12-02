import dearpygui.dearpygui as dpg
import config as c

class Presentation:
    def __init__(self):
        with dpg.window(label="Wprowadzenie", autosize=True, tag="ps", pos=[99999,99999], on_close=lambda: dpg.show_item("mainWindow")):
            dpg.hide_item("ps")
            with open('1.txt') as f:
                lines = f.readlines()

            s = ''.join(lines)

            dpg.add_text("Select what do you want to do")
            with dpg.table(width=1440, height=610, header_row=False):
                dpg.add_table_column(width=200)
                dpg.add_table_column(width=200)
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_text("dupa")
                    with dpg.table_cell():
                        dpg.add_text(s, wrap=200)
            with dpg.group(horizontal=True):
                dpg.add_button(width=c.navBut[0], height=c.navBut[1], arrow=True, direction=dpg.mvDir_Left)
                dpg.add_spacer(width=500)
                dpg.add_button(width=200, height=20, arrow=True, direction=dpg.mvDir_Right)