import sys

bpy = sys.modules.get("bpy")

if bpy is not None:
    import bpy
    from bpy.utils import register_class
    from bpy.utils import unregister_class

    from . import ui
    from . import operator
    from . import properties

    classes = (
        operator.create_particle_system,
        operator.solve_particle_system,
        operator.write_particle_system,
        operator.PYMAXION_OT_anchorConstraint,
        operator.PYMAXION_OT_cableConstraint,
        operator.PYMAXION_OT_forceConstraint,
        operator.PYMAXION_OT_barConstraint,
        ui.PYMAXION_PT_particleSystem,
        ui.PYMAXION_PT_constraints,
        properties.UserInputProperties,
    )

    def register():
        for cls in classes:
            register_class(cls)

        bpy.types.Scene.tools = bpy.props.PointerProperty(type=properties.UserInputProperties)

    def un_register():
        for cls in reversed(classes):
            unregister_class(cls)

        del bpy.types.Scene.tools
