bl_info = {
    'name': 'Import/Export: Phoenix bones (.phxbn)...',
    'author': 'David Rosen',
    'version': '0.2',
    'blender': (2, 92, 0),
    'location': 'File > Import/Export > PHXBN',
    'description': 'Import Phoenix Bones (.phxbn format)',
    'warning': '', # used for warning icon and text in addons panel
    'category': 'Import/Export'}

import bpy

def menu_import(self, context):
    from io_phxbn import import_phxbn
    self.layout.operator(import_phxbn.PHXBNImporter.bl_idname, text="Phoenix Bones (.phxbn)").filepath = "*.phxbn"
    
def menu_export(self, context):
    from io_phxbn import export_phxbn
    import os
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".phxbn"
    self.layout.operator(export_phxbn.PHXBNExporter.bl_idname, text="Phoenix Bones (.phxbn)").filepath = default_path
    
def register():
    from io_phxbn import import_phxbn, export_phxbn
    bpy.utils.register_class(import_phxbn.PHXBNImporter)
    bpy.utils.register_class(export_phxbn.PHXBNExporter)
    bpy.types.TOPBAR_MT_file_import.append(menu_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_export)

def unregister():
    from io_phxbn import import_phxbn, export_phxbn
    bpy.utils.unregister_class(import_phxbn.PHXBNImporter)
    bpy.utils.unregister_class(export_phxbn.PHXBNExporter)
    bpy.types.TOPBAR_MT_file_import.remove(menu_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export)
    
if __name__ == "__main__":
    register()
