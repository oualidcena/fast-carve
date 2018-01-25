bl_info = {
    "name": "Fast Carve",
    "description": "Hardsurface utility Blender addon for quick and easy boolean and bevel operations",
    "author": "Jayanam",
    "version": (0, 3, 0, 0),
    "blender": (2, 79, 0),
    "location": "View3D",
    "category": "Object"}

# Blender imports
import bpy

from bpy.props import *

from . fc_bevel_op    import FC_BevelOperator
from . fc_unbevel_op  import FC_UnBevelOperator
from . fc_panel       import FC_Panel
from . fc_bevel_panel import FC_Bevel_Panel
from . fc_bool_op     import FC_BoolOperator_Diff
from . fc_bool_op     import FC_BoolOperator_Union
from . fc_bool_op     import FC_BoolOperator_Slice
from . fc_immediate_mode_op import FC_Immediate_Mode_Operator

bpy.types.Scene.carver_target = PointerProperty(type=bpy.types.Object)

addon_keymaps = []

def register():
   bpy.utils.register_class(FC_Panel)
   bpy.utils.register_class(FC_Bevel_Panel)
   bpy.utils.register_class(FC_BevelOperator)
   bpy.utils.register_class(FC_UnBevelOperator)
   bpy.utils.register_class(FC_BoolOperator_Diff)
   bpy.utils.register_class(FC_BoolOperator_Union)
   bpy.utils.register_class(FC_BoolOperator_Slice)
   bpy.utils.register_class(FC_Immediate_Mode_Operator)
   
   # add keymap entry
   kcfg = bpy.context.window_manager.keyconfigs.addon
   if kcfg:
       km = kcfg.keymaps.new(name='3D View', space_type='VIEW_3D')
       kmi = km.keymap_items.new("object.fc_immediate_mode_op", 'F', 'PRESS', shift=True, ctrl=True)
       addon_keymaps.append((km, kmi))
    
def unregister():
   bpy.utils.unregister_class(FC_Panel)
   bpy.utils.unregister_class(FC_Bevel_Panel)
   bpy.utils.unregister_class(FC_BevelOperator)
   bpy.utils.unregister_class(FC_UnBevelOperator)
   bpy.utils.unregister_class(FC_BoolOperator_Diff)
   bpy.utils.unregister_class(FC_BoolOperator_Union)
   bpy.utils.unregister_class(FC_BoolOperator_Slice)
   
   # remove keymap entry
   for km, kmi in addon_keymaps:
       km.keymap_items.remove(kmi)
   addon_keymaps.clear()
    
   bpy.utils.unregister_class(FC_Immediate_Mode_Operator)
    
if __name__ == "__main__":
    register()