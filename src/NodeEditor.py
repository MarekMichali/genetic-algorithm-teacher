import dearpygui.dearpygui as dpg
import config


class NodeEditor:
    def __init__(self):
        with dpg.window(label="Tutorial", tag="nodeEditor", pos=config.nodeEditorDefaultPos, autosize=True):
            dpg.add_button(label="Run")
            dpg.hide_item("nodeEditor")
            with dpg.node_editor(callback=self.link_callback, delink_callback=self.delink_callback, tag="a", width=1000,
                                 height=600):
                with dpg.node(label="Node 1", pos=[200, 0]):
                    with dpg.node_attribute(label="Node A1"):
                       # with dpg.group(horizontal=True):
                        #dpg.add_text("Input", indent=10)
                        dpg.add_input_float(label="F1", width=100, callback=self.test)

                    with dpg.node_attribute(label="Node A2", attribute_type=dpg.mvNode_Attr_Output, tag="test"):
                        dpg.add_input_int(label="F2", width=100, step=0)


                with dpg.node(label="Mutation Ratio"):
                    with dpg.node_attribute(label="Node A3"):
                        dpg.add_text("Input", indent=10)
                    with dpg.node_attribute(label="Node A4", attribute_type=dpg.mvNode_Attr_Static,  tag="dupa"):
                        dpg.add_spacer(height=20)
                        dpg.add_input_float(width=100,  tag="dupav2")
                        dpg.add_spacer(height=20)
                    with dpg.node_attribute(label="Node A5", attribute_type=dpg.mvNode_Attr_Output):
                        dpg.add_text("Output", indent=50,  tag="aaaaa")

    def link_callback(this, sender, app_data):
        # app_data -> (link_id1, link_id2)
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)
        print(dpg.get_item_info(dpg.get_item_parent(app_data[0])))
        print(dpg.get_value(dpg.get_item_children(dpg.get_item_children(dpg.get_item_parent(app_data[0]))[1][2])[1][0]))
        #print(app_data[0])
       # print(sender)
        print(dpg.get_item_children(app_data[0])[1][0])
        print(dpg.get_value(dpg.get_item_children(app_data[0])[1][0]))
        print(dpg.get_value(dpg.get_item_children(app_data[1])[1][0]))


    # callback runs when user attempts to disconnect attributes
    def delink_callback(this, sender, app_data):
        dpg.delete_item(app_data)

    def test(this, ds, aa):
        x = dpg.get_selected_links("a")
        print(ds)
        print(aa)
        print(dpg.get_item_info("a"))