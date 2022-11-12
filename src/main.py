import dearpygui.dearpygui as dpg
from MainWindow import MainWindow
from NodeEditor import NodeEditor
from Math import Math
from Presentation import Presentation
from Dictionary import Dictionary
from Crossover import Crossover


def main():
    dpg.create_context()
    dpg.create_viewport(title='Custom Title', width=1440, height=810)
    dpg.set_viewport_pos(pos=[0.0, 0.0])
    dpg.setup_dearpygui()

    dictionary = Dictionary()
    crossover = Crossover()

    with dpg.font_registry():
        default_font = dpg.add_font("ArialNarrow7-JB8E.ttf", 20)

    dpg.bind_font(default_font)
    with dpg.viewport_menu_bar():
        with dpg.menu(label="Placeholder"):
            dpg.add_menu_item(label="Placeholder")
        dpg.add_menu_item(label="Dictionary", callback=lambda: dictionary.show())
        dpg.add_menu_item(label="Crossover", callback=lambda: crossover.show())

    mainWindow = MainWindow()
    nodeEditor = NodeEditor()
    math = Math()
    presentatin = Presentation()


    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()





if __name__ == '__main__':
    main()



