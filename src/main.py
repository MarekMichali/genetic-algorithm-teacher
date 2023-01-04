import dearpygui.dearpygui as dpg
from MainWindow import MainWindow
from Dictionary import Dictionary
from Crossover import Crossover
from IntroSlide import IntroSlide
from Mutation import Mutation
from Fitness import Fitness
from Selector import Selector
from EvolveOnes import EvolveOnes
from Optimization import Optimization
from Tsp import Tsp
from Diagram import Diagram


def main():
    dpg.create_context()
    dpg.create_viewport(title='Aplikacja do nauki zasad dzialania algorytmow genetycznych', width=1440, height=810, clear_color=(50, 50, 51))
    dpg.set_viewport_pos(pos=[0.0, 0.0])
    dpg.setup_dearpygui()

    dictionary = Dictionary()
    crossover = Crossover()
    intro_slide = IntroSlide()
    mutation = Mutation()
    fitness = Fitness()
    selector = Selector()
    evolve_ones = EvolveOnes()
    optimization = Optimization()
    tsp = Tsp()
    main_window = MainWindow()
    diagram = Diagram()

    with dpg.font_registry():
        with dpg.font("data//calibri.ttf", 20, default_font=True) as calibri:
            dpg.add_font_range(0x0100, 0x017f)
        dpg.bind_font(calibri)

    with dpg.viewport_menu_bar():
        dpg.add_menu_item(label="Menu", callback=lambda: main_window.show())
        dpg.add_menu_item(label="Diagram", callback=lambda: diagram.show_ext())
        dpg.add_menu_item(label="Podstawowe pojęcia", callback=lambda: dictionary.show_ext())
        dpg.add_menu_item(label="Ocena rozwiązania", callback=lambda: fitness.show_ext())
        dpg.add_menu_item(label="Selekcja", callback=lambda: selector.show_ext())
        dpg.add_menu_item(label="Krzyżowanie", callback=lambda: crossover.show_ext())
        dpg.add_menu_item(label="Mutacja", callback=lambda: mutation.show_ext())
        dpg.add_menu_item(label="     ",)
        with dpg.menu(label="Przykłady"):
            dpg.add_menu_item(label ="Ewolucja szczurów", callback=lambda: evolve_ones.show())
            dpg.add_menu_item(label="Znajdowanie argumentów", callback=lambda: optimization.show())
            dpg.add_menu_item(label="Problem komiwojażera", callback=lambda: tsp.show())

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()
