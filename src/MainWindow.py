import dearpygui.dearpygui as dpg
import config


class MainWindow:
    def __init__(self):
        with dpg.window(label="Main window", autosize=True, tag="mainWindow", pos=config.mainWindowDefaultPos):
            dpg.add_spacer(height=50)
            dpg.add_text("Select what do you want to do", indent=120)
            dpg.add_spacer(height=50)
            dpg.add_button(label="Start learning", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight, callback=self.show_presentation)
            dpg.add_button(label="Continue learning", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight)
            dpg.add_button(label="Select chapter", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight)
            dpg.add_button(label="Open playground", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight, callback=self.show_node_editor)
            dpg.add_button(label="Example", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight, callback=self.show_math)
            dpg.add_button(label="Close", width=config.mainWinButtonWidth, height=config.mainWinButtonHeight, callback=self.close_main_window)

    def close_main_window(self):
        dpg.delete_item("mainWindow")

    def show_node_editor(self):
        dpg.show_item("nodeEditor")
        dpg.set_item_pos("mainWindow", [0, 25])

    def show_math(self):
        dpg.show_item("math")
        dpg.set_item_pos("mainWindow", [0, 25])

    def show_presentation(self):
        dpg.show_item("ps")
        dpg.hide_item("mainWindow")