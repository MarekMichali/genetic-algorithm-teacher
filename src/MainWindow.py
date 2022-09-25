import dearpygui.dearpygui as dpg
import config


class MainWindow:
    def __init__(self):
        with dpg.window(label="Main window", autosize=True, tag="mainWindow", pos=config.mainWindowDefaultPos):
            dpg.add_spacer(height=50)
            dpg.add_text("Select what do you want to do", indent=120)
            dpg.add_spacer(height=50)
            dpg.add_button(label="Start learning", width=500, height=50)
            dpg.add_button(label="Continue learning", width=500, height=50)
            dpg.add_button(label="Select chapter", width=500, height=50)
            dpg.add_button(label="Open playground", width=500, height=50, callback=self.showNodeEditor)
            dpg.add_button(label="Close", width=500, height=50, callback=self.closeMainWindow)

    def closeMainWindow(self):
        dpg.delete_item("mainWindow")

    def showNodeEditor(self):
        dpg.show_item("nodeEditor")
        dpg.set_item_pos("mainWindow", [0, 25])