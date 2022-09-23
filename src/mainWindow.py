import dearpygui.dearpygui as dpg


def closeMainWindow():
    dpg.delete_item("mainWindow")


def mainWindow():
    with dpg.window(label="Main window", autosize=True, tag="mainWindow"):
        dpg.add_spacer(height=50)
        dpg.add_text("Select what you want to do", indent=100)
        dpg.add_spacer(height=50)
        dpg.add_button(label="Start learning", width=500, height=50)
        dpg.add_button(label="Continue learning", width=500, height=50)
        dpg.add_button(label="Select chapter", width=500, height=50)
        dpg.add_button(label="Open playground", width=500, height=50)
        dpg.add_button(label="Close", width=500, height=50, callback=closeMainWindow)
