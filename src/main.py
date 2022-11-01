import dearpygui.dearpygui as dpg
from MainWindow import MainWindow
from NodeEditor import NodeEditor
from Math import Math


def main():
    dpg.create_context()
    dpg.create_viewport(title='Custom Title', width=1920, height=1080)
    dpg.setup_dearpygui()

    with dpg.font_registry():
        default_font = dpg.add_font("ArialNarrow7-JB8E.ttf", 20)

    dpg.bind_font(default_font)
    with dpg.viewport_menu_bar():
        with dpg.menu(label="Placeholder"):
            dpg.add_menu_item(label="Placeholder")

    mainWindow = MainWindow()
    nodeEditor = NodeEditor()
    math = Math()

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()