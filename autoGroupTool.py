import maya.cmds as cmds

def create_control_groups():
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.warning("No objects selected.")
        return

    for obj in selected_objects:
        position = cmds.xform(obj, query=True, worldSpace=True, translation=True)
        rotation = cmds.xform(obj, query=True, worldSpace=True, rotation=True)
        
        group = cmds.group(empty=True, name=f"{obj}_Grp")
        cmds.xform(group, worldSpace=True, translation=position)
        cmds.xform(group, worldSpace=True, rotation=rotation)
        
        cmds.parent(obj, group)

create_control_groups()
