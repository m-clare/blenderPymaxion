import bpy
from bpy.types import Panel, PropertyGroup
from bpy.props import FloatProperty


class PYMAXION_PT_particleSystem(Panel):
    bl_idname = "PYMAXION_PT_particleSystem"
    bl_label = "Particle System"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pymaxion"

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        op = row.operator(
            "pymaxion_blender.create_particle_system", text="Create Particle System"
        )
        row = layout.row(align=True)
        op = row.operator(
            "pymaxion_blender.solve_particle_system", text="Solve Particle System"
        )
        row = layout.row(align=True)
        op = row.operator(
            "pymaxion_blender.reset_particle_system", text="Reset Particle System"
        )
        row = layout.row(align=True)
        op = row.operator(
            "pymaxion_blender.write_particle_system", text="Write Particle System"
        )


class PYMAXION_PT_constraints(Panel):
    bl_idname = "PYMAXION_PT_constraints"
    bl_label = "Constraints"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pymaxion"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tools = scene.tools  # TODO: more descriptive?

        layout.popover("OBJECT_PT_hello")

        box = layout.box()
        box.label(text="Anchor constraints")
        box.popover("PYMAXION_PT_Anchor")
        row = box.row(align=True)
        row.operator(
            "pymaxion_blender.anchor_constraint", text="Remove Anchors"
        ).action = "REMOVE"
        row.operator(
            "pymaxion_blender.anchor_constraint", text="Show Anchors"
        ).action = "SHOW"

        layout.separator()

        row = layout.row(align=True)
        row.operator(
            "pymaxion_blender.cable_constraint", text="Add Cables"
        ).action = "ADD"
        row.operator(
            "pymaxion_blender.cable_constraint", text="Remove Cables"
        ).action = "REMOVE"
        row.operator(
            "pymaxion_blender.cable_constraint", text="Show Cables"
        ).action = "SHOW"

        row = layout.row(align=True)
        row.operator("pymaxion_blender.bar_constraint", text="Add Bars").action = "ADD"
        row.operator(
            "pymaxion_blender.bar_constraint", text="Remove Bars"
        ).action = "REMOVE"
        row.operator(
            "pymaxion_blender.bar_constraint", text="Show Bars"
        ).action = "SHOW"

        layout.separator()

        box = layout.box()
        box.label(text="Force  constraints")
        box.popover("PYMAXION_PT_Force")
        row = box.row(align=True)
        row.operator(
            "pymaxion_blender.force_constraint", text="Remove Forces"
        ).action = "REMOVE"
        row.operator(
            "pymaxion_blender.force_constraint", text="Show Forces"
        ).action = "SHOW"


class PYMAXION_PT_Anchor(Panel):
    bl_label = "Add Anchors"
    bl_idname = "PYMAXION_PT_Anchor"
    bl_options = {"INSTANCED"}
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sciProp = scene.sciProp

        layout.label(text="Add Anchor Constraint")
        row = layout.row(align=True)
        row.prop(sciProp, "number", text="Strength Value")
        row.prop(sciProp, "power", text="10^")
        row = layout.row(align=True)
        row.operator("pymaxion_blender.anchor_constraint", text="Add").action = "ADD"

class PYMAXION_PT_Force(Panel):
    bl_label = "Add Forces"
    bl_idname = "PYMAXION_PT_Force"
    bl_options = {"INSTANCED"}
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sciProp = scene.sciProp

        layout.label(text="Add Force Constraint")
        row = layout.row(align=True)
        row.prop(sciProp, "number", text="Strength Value")
        row.prop(sciProp, "power", text="10^")
        row = layout.row(align=True)
        row.operator("pymaxion_blender.force_constraint", text="Add").action = "ADD"
