import maya.cmds as cmds

def create_controls_for_joints():
    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints:
        cmds.warning("No joint objects selected.")
        return
    
    for joint in selected_joints:
        control = cmds.circle(name=joint.replace('_Jnt', '') + '_Ctrl', normal=(1, 0, 0), radius=1.0)[0]
        group = cmds.group(name=control + '_Grp', empty=True)
        cmds.matchTransform(group, joint)
        cmds.matchTransform(control, joint)
        cmds.parent(control, group)
        
        base_name = joint.rsplit('_', 1)[0] if '_' in joint else joint
        control_name = base_name + '_Ctrl'
        group_name = control_name + '_Grp'
        
        cmds.rename(control, control_name)
        cmds.rename(group, group_name)

    print("Controls and groups created for all selected joints.")

create_controls_for_joints()
