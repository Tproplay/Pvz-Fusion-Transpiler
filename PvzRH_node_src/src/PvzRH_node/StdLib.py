"""Contains some useful functions and classes for level creation and manipulation."""

from .extensions import *
from .TypeMgr import KeyCode

def format_string(*args):
    """Dynamically chains text and variables using physical StringValueNodes!"""
    if not args:
        return ""

    from .nodes import string_concat, string_value
    from .node_base import PortReference 
    
    def _parse_arg(arg):
        if hasattr(arg, 'to_string'):
            return arg.to_string()
        if isinstance(arg, PortReference):
            return arg._to_string_port()
        if hasattr(arg, 'node'):
            return arg
            
        return string_value(val=str(arg)).value

    current_chain = _parse_arg(args[0])

    for i in range(1, len(args)):
        next_piece = _parse_arg(args[i])
        current_chain = string_concat(a=current_chain, b=next_piece).result

    return current_chain

from .api import *

class _wasd_key:
    def __init__(self):
        self.up = KeyCode.W
        self.down = KeyCode.S
        self.left = KeyCode.A
        self.right = KeyCode.D

class WASDPlant:
    
    """Assigns WaSD keys to control a plant in the game."""
    
    def __init__(self, plant: Plant | Any):
        
        if (isinstance(plant, Plant)):
            self.plant = plant
        else:
            self.plant = Plant(plant)
            
        self.wasd_keys = _wasd_key()
        
    
    def Start(self):
        from .api import Trigger
        with Trigger.OnKeyDown(self.wasd_keys.up):
            self.plant.move_relative(0, -1)
        with Trigger.OnKeyDown(self.wasd_keys.down):
            self.plant.move_relative(0, 1)
        with Trigger.OnKeyDown(self.wasd_keys.left):
            self.plant.move_relative(-1, 0)
        with Trigger.OnKeyDown(self.wasd_keys.right):
            self.plant.move_relative(1, 0)



