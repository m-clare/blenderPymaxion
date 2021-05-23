import bpy
from bpy.types import PropertyGroup
from bpy.props import FloatProperty
from bpy.props import IntProperty
from bpy.props import StringProperty

class ScientificNotation(PropertyGroup):
    def __init__(self, num_dict={}, power_dict={}):
        self.num_dict = num_dict
        self.power_dict = power_dict
        self.number = FloatProperty()
        self.power = IntProperty()
        self.value = self.get_num()

    def get_num(self):
        default_num = {'min': -10, 'max': 10, 'default': 1, 'precision': 2}
        default_pow = {'min': -30, 'max': 30, 'default': 1}

        for key in default_num.keys():
            self.number[key] = self.num_dict.get(key, default_num[key])
            for key in default_pow.keys():
                self.power[key] = self.power_dict.get(key, default_pow[key])
        return self.number * pow(10, self.power)


    # value = property(get_num)

default_constraint_props = {'anchor': {'num': {'min': 1, 'max': 10, 'default': 1, 'precision': 2},
                                       'power': {'min': -30 , 'max': 30, 'default': 20}},
                            'cable':  {'num': {'min': 1, 'max': 10, 'default': 1, 'precision': 2},
                                       'power': {'min':-20, 'max': 20, 'default': 6}},
                            'bar':    {'num': {'min': 1, 'max': 10, 'default': 1, 'precision': 2},
                                       'power': {'min':-20, 'max': 20, 'default': 6}},
                            'force':  {'num': {'min': 1, 'max': 10, 'default': 1, 'precision': 2},
                                       'power': {'min':-20, 'max':20, 'default': 6}}}


class AnchorSciNot(PropertyGroup):
    def get_num(self):
        return self.number * pow(10, self.power)
    number: FloatProperty(min=1, max=10, default=1, precision=2)
    power: IntProperty(min=-30, max=30, default=20)
    value = property(get_num)

class ForceSciNot(PropertyGroup):
    def get_num(self):
        return self.number * pow(10, self.power)
    number: FloatProperty(min=1, max=10, default=1, precision=2)
    power: IntProperty(min=-20, max=20, default=6)
    value = property(get_num)

class CableSciNot(PropertyGroup):
    def get_num(self):
        return self.number * pow(10, self.power)
    number: FloatProperty(min=1, max=10, default=1, precision=2)
    power: IntProperty(min=-20, max=20, default=6)
    value = property(get_num)

class BarSciNot(PropertyGroup):
    def get_num(self):
        return self.number * pow(10, self.power)
    number: FloatProperty(min=1, max=10, default=1, precision=2)
    power: IntProperty(min=-20, max=20, default=6)
    value = property(get_num)

class UserInputProperties(PropertyGroup):

    anchor_strength: FloatProperty(
        name="Anchor Strength",
        description="Strength of Anchor Constraint",
        min=0.001,
        max=1e30,
        default=1e20,
        precision=3)

    cable_diameter: FloatProperty(
        name="Cable diameter (m)",
        description="Diameter of Cable",
        min=1e-3,
        max=2,
        default=0.05,
        precision=3
    )

