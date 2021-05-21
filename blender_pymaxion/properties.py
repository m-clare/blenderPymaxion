import bpy
from bpy.types import PropertyGroup
from bpy.props import FloatProperty
from bpy.props import IntProperty
from bpy.props import StringProperty

class ScientificNotation(PropertyGroup):
    def get_num(self):
        return self.number * pow(10, self.power)
    number: FloatProperty(min=1, max=10, default=1, precision=2)
    power: IntProperty(min=-30, max=30, default=10)
    value = property(get_num)

class UserInputProperties(PropertyGroup):

    anchor_strength: FloatProperty(
        name="Anchor Strength",
        description="Strength of Anchor Constraint",
        min=0.001,
        max=1e30,
        default=1e20,
        precision=3)
