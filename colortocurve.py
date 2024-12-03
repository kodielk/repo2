import maya.cmds as cmds

def change_shape_override_color(color):
    """
    Changes the override color for shape nodes of the selected objects.

    Args:
        color (int or str): The color value (0-31) or a valid color name string.
                           String values map to indices based on Maya's color mapping.
    """
    color_map = {
        "black": 1, "grey": 2, "blue": 3, "dark blue": 4, "purple": 5, 
        "pink": 6, "brown": 7, "red": 13, "dark red": 15, "green": 14, 
        "dark green": 19, "yellow": 17, "orange": 21, "cyan": 18
    }

    if isinstance(color, str):
        color = color.lower()
        if color not in color_map:
            cmds.error(f"Invalid color name '{color}'. Valid names: {', '.join(color_map.keys())}")
        color = color_map[color]
    elif isinstance(color, int):
        if not (0 <= color <= 31):
            cmds.error("Color value must be between 0 and 31.")
    else:
        cmds.error("Color must be an integer (0-31) or a valid string name.")

    #  current selection
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.error("No objects selected. Please select one or more objects.")

    for obj in selected_objects:
        shape_nodes = cmds.listRelatives(obj, shapes=True, fullPath=True)
        if not shape_nodes:
            cmds.warning(f"No shape nodes found for '{obj}'. Skipping.")
            continue

        for shape in shape_nodes:
            cmds.setAttr(f"{shape}.overrideEnabled", True)
            cmds.setAttr(f"{shape}.overrideColor", color)

    print(f"Override color set to {color} for all shape nodes of the selected objects.")


