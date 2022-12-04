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


def main():
    dpg.create_context()
    dpg.create_viewport(title='Custom Title', width=1440, height=810)
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

    with dpg.font_registry():
        default_font = dpg.add_font("ArialNarrow7-JB8E.ttf", 20)

    dpg.bind_font(default_font)
    with dpg.viewport_menu_bar():
        dpg.add_menu_item(label="Menu", callback=lambda: main_window.show())
        dpg.add_menu_item(label="Podstawowe pojecia", callback=lambda: dictionary.show_ext())
        dpg.add_menu_item(label="Ocena rozwiazania", callback=lambda: fitness.show_ext())
        dpg.add_menu_item(label="Selekcja", callback=lambda: selector.show_ext())
        dpg.add_menu_item(label="Krzyzowanie", callback=lambda: crossover.show_ext())
        dpg.add_menu_item(label="Mutacja", callback=lambda: mutation.show_ext())
        dpg.add_menu_item(label="     ",)
        with dpg.menu(label="Przyklady"):
            dpg.add_menu_item(label="Ewolucja szczurow", callback=lambda: evolve_ones.show())
            dpg.add_menu_item(label="Znajdowanie argumentow", callback=lambda: optimization.show())
            dpg.add_menu_item(label="Problem komiwojazera", callback=lambda: tsp.show())

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()
