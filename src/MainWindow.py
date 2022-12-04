import dearpygui.dearpygui as dpg
import config


class SingletonMainWindow(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MainWindow(metaclass=SingletonMainWindow):
    def __init__(self):
        with dpg.theme() as disabled_theme:
            with dpg.theme_component(dpg.mvButton, enabled_state=False):
                dpg.add_theme_color(dpg.mvThemeCol_Text, [128, 128, 128])
                dpg.add_theme_color(dpg.mvThemeCol_Button, [101, 101, 105])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [101, 101, 105])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [101, 101, 105])
        dpg.bind_theme(disabled_theme)
        with dpg.mutex():
            viewport_height = dpg.get_viewport_client_height()
            with dpg.window(label="Menu", autosize=True, tag="mainWindow", pos=config.mainWindowDefaultPos):
                dpg.add_spacer(height=50)
                dpg.add_text("Wybierz co chcesz zrobic", indent=120)
                dpg.add_spacer(height=50)
                dpg.add_button(label="Rozpocznij nauke", width=config.mainWinButtonWidth,
                               height=config.mainWinButtonHeight, callback=self.show_presentation)
                #dpg.add_button(label="Continue learning", width=config.mainWinButtonWidth,
                               #height=config.mainWinButtonHeight)
                dpg.add_button(label="Problem komiwojazera", width=config.mainWinButtonWidth,
                               height=config.mainWinButtonHeight, callback=self.show_tsp)
                dpg.add_button(label="Znajdowanie argumentow", width=config.mainWinButtonWidth,
                               height=config.mainWinButtonHeight, callback=self.show_opt)
                dpg.add_button(label="Ewolucja szczurow", width=config.mainWinButtonWidth,
                               height=config.mainWinButtonHeight, callback=self.show_math)
              #  dpg.add_button(label="Close", width=config.mainWinButtonWidth,
                             #  height=config.mainWinButtonHeight, callback=self.close_main_window)

        dpg.set_item_pos("mainWindow", [1440 // 2 - config.mainWinButtonWidth // 2,
                                        viewport_height // 2 - config.mainWinButtonHeight - 400 // 2])

    def close_main_window(self):
        dpg.delete_item("mainWindow")

    def show_node_editor(self):
        dpg.show_item("nodeEditor")
        dpg.set_item_pos("mainWindow", [0, 25])

    def show_math(self):
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
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("tsp")
        dpg.split_frame()
        width = dpg.get_item_width("tsp")
        height = dpg.get_item_height("tsp")
        dpg.set_item_pos("tsp", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")
