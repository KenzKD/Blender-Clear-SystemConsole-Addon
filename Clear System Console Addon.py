bl_info = {
    "name": "Clear System Console",
    "author": "Robert Guetzkow",
    "version": (1, 0, 0),
    "blender": (2, 81, 0),
    "location": "Text Editor Header",
    "description": "Clear the system console.",
    "wiki_url": "",
    "category": "Text Editor"}

import bpy
import os


class CLEARCONSOLE_OT_clear(bpy.types.Operator):
    bl_idname = "clearconsole.clear"
    bl_label = "Clear System Console"
    bl_description = "This operator clears the system console."
    bl_options = {"REGISTER"}

    def execute(self, context):
        if os.name == "nt":
            os.system("cls") 
        else:
            os.system("clear") 
        return {"FINISHED"}


def draw(self, context):
    self.layout.operator(CLEARCONSOLE_OT_clear.bl_idname)


classes = (CLEARCONSOLE_OT_clear,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.TEXT_HT_header.append(draw)


def unregister():
    bpy.types.TEXT_HT_header.remove(draw)
    
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()