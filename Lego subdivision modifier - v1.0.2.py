bl_info = {
    "name": "Lego Subdivider",
    "blender": (3, 4, 1),
    "category": "Object",
    "version": (1, 0, 2),
    "author": "Electronic Films",
    "location": "3D View > Sidebar > Lego Subdivider",
}


import bpy

# Define the operator for the button action
class OBJECT_OT_lego_subdivider(bpy.types.Operator):
    bl_idname = "object.lego_subdivider"
    bl_label = "Subdivide LEGO"
    
    def execute(self, context):
        # Switch to Edit Mode
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Execute the specified operations
        bpy.ops.mesh.split_normals()
        bpy.ops.mesh.merge_normals()
        bpy.ops.mesh.select_all(action='INVERT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        bpy.ops.mesh.select_non_manifold()
        bpy.ops.mesh.remove_doubles()
        bpy.ops.transform.edge_crease(value=1, snap=False)
        bpy.ops.mesh.split_normals()
        
        # Switch back to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        return {'FINISHED'}

# Define the panel for the addon in the sidebar
class LegoSubdividerPanel(bpy.types.Panel):
    bl_label = "Lego Subdivider"
    bl_idname = "PT_LegoSubdividerPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Lego Subdivider'  # New tab name
    bl_context = 'objectmode'

    def draw(self, context):
        layout = self.layout
        
        # Add a button that triggers the operator
        layout.operator("object.lego_subdivider", text="Subdivide LEGO", icon="MESH_ICOSPHERE")

# Register the operator and panel
def register():
    bpy.utils.register_class(OBJECT_OT_lego_subdivider)
    bpy.utils.register_class(LegoSubdividerPanel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_lego_subdivider)
    bpy.utils.unregister_class(LegoSubdividerPanel)

# Run the addon when the script is executed in Blender
if __name__ == "__main__":
    register()
