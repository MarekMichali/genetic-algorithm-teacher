import dearpygui.dearpygui as dpg
from MainWindow import MainWindow
from Dictionary import Dictionary
from Crossover import Crossover
from IntroSlide import IntroSlide
from Mutation import Mutation
from Fitness import Fitness
from Selector import Selector
from EvolveOnes import EvolveOnes
from Optimalization import Optimalization
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
    optimalization = Optimalization()
    tsp = Tsp()

    with dpg.font_registry():
        default_font = dpg.add_font("ArialNarrow7-JB8E.ttf", 20)

    dpg.bind_font(default_font)
    with dpg.viewport_menu_bar():
        with dpg.menu(label="Placeholder"):
            dpg.add_menu_item(label="Placeholder")
        dpg.add_menu_item(label="Dictionary", callback=lambda: dictionary.show())
        dpg.add_menu_item(label="Crossover", callback=lambda: crossover.show())
        dpg.add_menu_item(label="IntroSlide", callback=lambda: intro_slide.show())
        dpg.add_menu_item(label="Mutacja", callback=lambda: mutation.show())
        dpg.add_menu_item(label="Fitness", callback=lambda: fitness.show())
        dpg.add_menu_item(label="Selector", callback=lambda: selector.show())

    main_window = MainWindow()

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()



