import dearpygui.dearpygui as dpg
import config
import time
import Presentation

class MainWindow:
    def __init__(self):
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
            print(viewport_height)
            with dpg.window(label="Main window", autosize=True, tag="mainWindow", pos=config.mainWindowDefaultPos):
                width, height, channels, data = dpg.load_image("dna.png")

                with dpg.texture_registry():
                    texture_id = dpg.add_static_texture(width, height, data)

                dpg.add_image(texture_id, width=200, height=100)
                dpg.add_spacer(height=50)

                dpg.add_text("Select what do you want to do", indent=120)
                dpg.add_spacer(height=50)
                dpg.add_button(label="Start learning", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight, callback=self.show_presentation)
                dpg.add_button(label="Continue learning", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight)
                dpg.add_button(label="Tsp", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight, callback=self.show_tsp)
                dpg.add_button(label="Optymalizacja", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight, callback=self.show_opt)
                dpg.add_button(label="Ewolucja szczurow", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight, callback=self.show_math)
                dpg.add_button(label="Close", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight, callback=self.close_main_window)

        #dpg.split_frame()
        width = dpg.get_item_width("mainWindow")
        height = dpg.get_item_height("mainWindow")
        dpg.set_item_pos("mainWindow", [1440 // 2 - config.mainWinButtonWidth // 2, viewport_height // 2 - config.mainWinButtonHeight - 400 // 2])
    def close_main_window(self):
        dpg.delete_item("mainWindow")

    def show_node_editor(self):
        dpg.show_item("nodeEditor")
        dpg.set_item_pos("mainWindow", [0, 25])

    def show_math(self):
       # dpg.show_item("evolveOnes")
        #dpg.set_item_pos("mainWindow", [0, 25])

        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("evolveOnes")
        dpg.split_frame()
        width = dpg.get_item_width("evolveOnes")
        height = dpg.get_item_height("evolveOnes")
        dpg.set_item_pos("evolveOnes", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")

    def show_presentation(self):
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("introSlide")
        dpg.split_frame()
        width = dpg.get_item_width("introSlide")
        height = dpg.get_item_height("introSlide")
        dpg.set_item_pos("introSlide", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")

    def show_opt(self):
       # dpg.show_item("evolveOnes")
        #dpg.set_item_pos("mainWindow", [0, 25])

        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("optimalization")
        dpg.split_frame()
        width = dpg.get_item_width("optimalization")
        height = dpg.get_item_height("optimalization")
        dpg.set_item_pos("optimalization", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")

    def show_tsp(self):
       # dpg.show_item("evolveOnes")
        #dpg.set_item_pos("mainWindow", [0, 25])

        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("tsp")
        dpg.split_frame()
        width = dpg.get_item_width("tsp")
        height = dpg.get_item_height("tsp")
        dpg.set_item_pos("tsp", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")