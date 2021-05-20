import bpy
from bpy.types import PropertyGroup
from bpy.props import FloatProperty
from bpy.props import IntProperty
from bpy.props import StringProperty

class ScientificNotation():
    def __init__(name='', description=''):
        self.name = name
        self.description = description

    def get_num(self):
        return self.number * pow(10, self.power)
    number: FloatProperty(min=1, max=10, defaulbt=1, precision=2)
    power: IntProperty()
    value = property(get_num)

class UserInputProperties(PropertyGroup):

    anchor_strength: FloatProperty(
        name="Anchor Strength",
        description="Strength of Anchor Constraint",
        min=0.001,
        max=1e30,
        default=1e20,
        precision=3)

