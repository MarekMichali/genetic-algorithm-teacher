import dearpygui.dearpygui as dpg
import config

class Presentation:
    def __init__(self):
        with dpg.window(label="What is this", autosize=True, tag="ps", pos=[99999,99999]):
            dpg.hide_item("ps")
            with open('..//1.txt') as f:
                lines = f.readlines()

            s = ''.join(lines)
            dpg.add_text(s)
            dpg.add_text("Select what do you want to do")
