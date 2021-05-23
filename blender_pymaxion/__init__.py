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
        operator.reset_particle_system,
        operator.PYMAXION_OT_anchorConstraint,
        operator.PYMAXION_OT_cableConstraint,
        operator.PYMAXION_OT_forceConstraint,
        operator.PYMAXION_OT_barConstraint,
        ui.PYMAXION_PT_particleSystem,
        ui.PYMAXION_PT_constraints,
        ui.PYMAXION_PT_Anchor,
        ui.PYMAXION_PT_Force,
        ui.PYMAXION_PT_Cable,
        properties.UserInputProperties,
        properties.AnchorSciNot,
        properties.BarSciNot,
        properties.CableSciNot,
        properties.ForceSciNot
    )

    default_constraint_props = {'anchor': {'num': {'min': 1, 'max': 10, 'default': 1, 'precision': 2},
                                           'power': {'min': -30 , 'max': 30, 'default': 20}},
                                'cable':  {'num': {'min': 1, 'max': 10, 'default': 1, 'precision': 2},
                                           'power': {'min':-20, 'max': 20, 'default': 6}},
                                'bar':    {'num': {'min': 1, 'max': 10, 'default': 1, 'precision': 2},
                                           'power': {'min':-20, 'max': 20, 'default': 6}},
                                'force':  {'num': {'min': 1, 'max': 10, 'default': 1, 'precision': 2},
                                           'power': {'min':-20, 'max':20, 'default': 6}}}

    def register():
        for cls in classes:
            register_class(cls)

        bpy.types.Scene.tools = bpy.props.PointerProperty(type=properties.UserInputProperties)

        for constraint in default_constraint_props:
            prop = properties.ScientificNotation(num_dict=constraint['num'], pow_dict=constraint['power'])
            bpy.types.Scene[constraint] = bpy.props.PointerProperty(type=prop)

        # bpy.types.Scene.anchorProp = bpy.props.PointerProperty(type=properties.AnchorSciNot)
        # bpy.types.Scene.cableProp = bpy.props.PointerProperty(type=properties.CableSciNot)
        # bpy.types.Scene,barProp = bpy.props.PointerProperty(type=properties.BarSciNot)


    def un_register():
        for cls in reversed(classes):
            unregister_class(cls)

        del bpy.types.Scene.tools
        del bpy.types.Scene.sciProp
