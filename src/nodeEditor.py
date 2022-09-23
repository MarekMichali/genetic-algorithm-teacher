import dearpygui.dearpygui as dpg

dpg.create_context()

# callback runs when user attempts to connect attributes
def link_callback(sender, app_data):
    # app_data -> (link_id1, link_id2)
    dpg.add_node_link(app_data[0], app_data[1], parent=sender)
    print(app_data[0])
    print(sender)
    print(dpg.get_item_children(app_data[0])[1])
    print(dpg.get_value(dpg.get_item_children(app_data[0])[1][0]))
    print(dpg.get_value(dpg.get_item_children(app_data[1])[1][0]))

# callback runs when user attempts to disconnect attributes
def delink_callback(sender, app_data):
    dpg.delete_item(app_data)

def test(ds, aa):
    x = dpg.get_selected_links("a")
    print(ds)
    print(aa)
    print(dpg.get_item_info("a"))

with dpg.window(label="Tutorial", width=500, height=500):
    with dpg.node_editor(callback=link_callback, delink_callback=delink_callback, tag="a",width=500, height=500):
        with dpg.node(label="Node 1"):
            with dpg.node_attribute(label="Node A1"):
                dpg.add_input_float(label="F1", width=150, callback=test)

            with dpg.node_attribute(label="Node A2", attribute_type=dpg.mvNode_Attr_Output, tag="test"):
                dpg.add_input_float(label="F2", width=150)

        with dpg.node(label="Node 2"):
            with dpg.node_attribute(label="Node A3"):
                dpg.add_input_float(label="F3", width=200)
            with dpg.node_attribute(label="Node A3"):
                dpg.add_text("aa")
            with dpg.node_attribute(label="Node A4", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_input_float(label="F4", width=200)

    with dpg.window(label="Main window", autosize=True, tag="mainWindow"):
        dpg.add_spacer(height=50)
        dpg.add_text("Select what you want to do", indent=100)
        dpg.add_spacer(height=50)
        dpg.add_button(label="Start learning", width=500, height=50, callback=test)




dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()