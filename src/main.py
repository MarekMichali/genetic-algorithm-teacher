import dearpygui.dearpygui as dpg


def main():
    dpg.create_context()
    dpg.create_viewport(title='Custom Title', width=1920, height=1080)

    with dpg.font_registry():
        default_font = dpg.add_font("ArialNarrow7-JB8E.ttf", 20)

    dpg.bind_font(default_font)
    with dpg.viewport_menu_bar():
        with dpg.menu(label="Placeholder"):
            dpg.add_menu_item(label="Placeholder")

    with dpg.window(label="Main window", autosize=True):
        dpg.add_spacer(height=50)
        dpg.add_text("Select what you want to do", indent=100)
        dpg.add_spacer(height=50)
        dpg.add_button(label="Start learning", width=500, height=50)
        dpg.add_button(label="Continue learning", width=500, height=50)
        dpg.add_button(label="Select chapter", width=500, height=50)
        dpg.add_button(label="Open playground", width=500, height=50)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    main()