import dearpygui.dearpygui as dpg
import src.config as config


class SingletonMainWindow(type):
    """
        Klasa odpowiedzialna za implementację singletonu dla klasy MainWindow
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MainWindow(config.Config, metaclass=SingletonMainWindow):
    """
        Klasa odpowiedzialna za główne menu
    """
    def __init__(self):
        with dpg.theme() as global_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (60, 60, 61))
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (60, 60, 61))
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (70, 71, 75))
                dpg.add_theme_color(dpg.mvThemeCol_Button, (70, 71, 75))
                dpg.add_theme_color(dpg.mvPlotCol_Line, (255, 242, 0), category=dpg.mvThemeCat_Plots)
            with dpg.theme_component(dpg.mvButton, enabled_state=False):
                dpg.add_theme_color(dpg.mvThemeCol_Text, [128, 128, 128])
                dpg.add_theme_color(dpg.mvThemeCol_Button, [101, 101, 105])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [101, 101, 105])
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [101, 101, 105])
        dpg.bind_theme(global_theme)

        with dpg.mutex():
            viewport_height = dpg.get_viewport_client_height()
            with dpg.window(label="Menu", autosize=True, tag="mainWindow", pos=[99999, 99999]):
                dpg.add_spacer(height=50)
                dpg.add_text("Wybierz co chcesz zrobić", indent=145)
                dpg.add_spacer(height=50)
                dpg.add_button(label="Rozpocznij naukę", width=self.mainWinButtonWidth,
                               height=self.mainWinButtonHeight, callback=self.show_presentation)
                dpg.add_button(label="Ewolucja szczurów", width=self.mainWinButtonWidth,
                               height=self.mainWinButtonHeight, callback=self.show_ones)
                dpg.add_button(label="Znajdowanie argumentów", width=self.mainWinButtonWidth,
                               height=self.mainWinButtonHeight, callback=self.show_opt)
                dpg.add_button(label="Problem komiwojażera", width=self.mainWinButtonWidth,
                               height=self.mainWinButtonHeight, callback=self.show_tsp)

        dpg.set_item_pos("mainWindow", [1408 // 2 - self.mainWinButtonWidth // 2,
                                        viewport_height // 2 - self.mainWinButtonHeight - 323 // 2])

    def show(self):
        """
            Pokazuje główne menu
        """
        if not dpg.is_item_visible("mainWindow"):
            with dpg.mutex():
                viewport_width = dpg.get_viewport_client_width()
                viewport_height = dpg.get_viewport_client_height()
            dpg.show_item("mainWindow")
            dpg.split_frame()
            width = dpg.get_item_width("mainWindow")
            height = dpg.get_item_height("mainWindow")
            dpg.set_item_pos("mainWindow", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])

    def close_main_window(self):
        """
            Zamyka główne menu
        """
        dpg.delete_item("mainWindow")

    def show_ones(self):
        """
            Wyświetla przykładowe zadanie ewolucji szczurów
        """
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
        """
            Wyświetla prezentację
        """
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
        """
            Wyświetla przykładowe zadanie szukania wartośći argumentów
        """
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
        """
            Wyświetla przykładowe zadanie problemu komiwojażera
        """
        with dpg.mutex():
            viewport_width = dpg.get_viewport_client_width()
            viewport_height = dpg.get_viewport_client_height()
        dpg.show_item("tsp")
        dpg.split_frame()
        width = dpg.get_item_width("tsp")
        height = dpg.get_item_height("tsp")
        dpg.set_item_pos("tsp", [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])
        dpg.hide_item("mainWindow")
