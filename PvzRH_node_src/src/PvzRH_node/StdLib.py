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

class Dictionary:
    """A Virtual Dictionary (Global State Manager) utilizing Native Variables."""
    def __init__(self, schema: dict = None): #type: ignore
        self._store = {}
        if schema:
            for key, initial_val in schema.items():
                self.add_key(key, initial_val)

    def add_key(self, key: str, initial_val): #type: ignore
        if key in self._store: raise KeyError(f"Key '{key}' already exists!")
            
        if isinstance(initial_val, bool):
            self._store[key] = BoolVar(start_val=initial_val)
        elif isinstance(initial_val, float):
            self._store[key] = FloatVar(start_val=initial_val)
        elif isinstance(initial_val, int):
            self._store[key] = IntVar(start_val=initial_val)
        else:
            raise TypeError("Unsupported Dictionary type. Use int, float, or bool.")

    def __getitem__(self, key): return self._store[key]
    def __setitem__(self, key, value): self._store[key].set(value)
    def __getattr__(self, key): return self._store[key]
    def __setattr__(self, key, value):
        if key == "_store": super().__setattr__(key, value)
        else: self._store[key].set(value)

class Array:
    """A Pre-Allocated Virtual Array utilizing Native Variables."""
    def __init__(self, size: int, default_val=0):
        self.size = size
        self._store = []
        
        for _ in range(size):
            if isinstance(default_val, bool): self._store.append(BoolVar(start_val=default_val))
            elif isinstance(default_val, float): self._store.append(FloatVar(start_val=default_val))
            elif isinstance(default_val, int): self._store.append(IntVar(start_val=default_val))

    def __getitem__(self, index: int): return self._store[index]
    def __setitem__(self, index: int, value): self._store[index].set(value)
    def __len__(self): return self.size

    def read(self, index_port, on_read_callback):
        for i in range(self.size):
            with If(index_port == i):
                on_read_callback(self._store[i])
                
    def write(self, index_port, value):
        for i in range(self.size):
            with If(index_port == i):
                self._store[i].set(value)            


