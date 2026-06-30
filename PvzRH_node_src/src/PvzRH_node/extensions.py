from . import nodes
from .core import ctx
from .node_base import ExecutionPath, BaseNode
from enum import Enum


class If:
    """Syntactic sugar that acts as a safe visual scripting 'if/elif/else' block."""
    def __init__(self, condition):
        self.node = nodes.branch_node(condition=condition)
        
    def __enter__(self):
        self.node.Output.Then.__enter__()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.node.Output.Then.__exit__(exc_type, exc_val, exc_tb)
        
    @property
    def Else(self):
        return self.node.Output.Else
        
    def Elif(self, condition):
        ctx.trigger_stack.append(self.node.Output.Else)
        new_branch = If(condition)
        ctx.trigger_stack.pop()
        return new_branch

#region Variables

class IntVar:
    """Use to create a Variable Int Value. Don't use = to set the value, use .set() instead."""
    def __init__(self, start_val=0, node_ref=None):
        self._node = node_ref if node_ref else nodes.int_variable() 
        if start_val != 0:
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            init_trigger = nodes.on_board_start()
            ctx.add_connection(init_trigger.id, "触发", nodes.set_int_variable_value(variable=self._node.variable, value=start_val).id, "触发")
            ctx.trigger_stack.extend(saved_stack)

    def _is_float_port(self): return False
    def _get_primary_port(self): return self.value

    @property
    def value(self):
        return nodes.get_int_variable_value(variable=self._node.variable).value
        
    def set(self, target_value):
        casted_val = self._cast_to_int(target_value)
        set_node = nodes.set_int_variable_value(variable=self._node.variable, value=casted_val)
        if ctx.trigger_stack:
            current = ctx.trigger_stack[-1]
            ctx.add_connection(current.id, current.out_trigger, set_node.id, "触发")
            ctx.trigger_stack[-1] = ExecutionPath(set_node.id, "完成")
        return set_node

    def _cast_to_int(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "IntVar": return val.value
        if cls_name == "FloatVar": return nodes.float_to_int(float_val=val.value).int
        if cls_name == "BoolVar": 
            raise TypeError("❌ Type Error: Cannot implicitly cast a BoolVar to an IntVar.")
            
        if isinstance(val, bool): return 1 if val else 0
        if isinstance(val, int): return val
        if isinstance(val, float): return int(val)
            
        if hasattr(val, 'node'):
            t = val.node.type
            float_nodes = ["FloatVariableNode", "GetFloatVariableValueNode", "RandomFloatNode", "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"]
            if t in float_nodes: return nodes.float_to_int(float_val=val).int
            return val
            
        raise TypeError(f"❌ Type Error: Unsupported type '{type(val).__name__}' passed to IntVariable.")

    def to_string(self, decimals=0):
        from .nodes import int_to_float, float_to_string, int_value
        f_val = int_to_float(int_val=self.value).float
        dec_node = int_value(val=decimals).value 
        return float_to_string(float_val=f_val, decimals=dec_node).result

    def __iadd__(self, other): self.set(nodes.int_add(a=self.value, b=self._cast_to_int(other)).result); return self
    def __isub__(self, other): self.set(nodes.int_subtract(a=self.value, b=self._cast_to_int(other)).result); return self
    def __imod__(self, other): self.set(nodes.int_modulo(a=self.value, b=self._cast_to_int(other)).result); return self

    def __add__(self, other): return nodes.int_add(a=self.value, b=self._cast_to_int(other)).result
    def __radd__(self, other): return nodes.int_add(a=self._cast_to_int(other), b=self.value).result
    def __sub__(self, other): return nodes.int_subtract(a=self.value, b=self._cast_to_int(other)).result
    def __rsub__(self, other): return nodes.int_subtract(a=self._cast_to_int(other), b=self.value).result
    def __mod__(self, other): return nodes.int_modulo(a=self.value, b=self._cast_to_int(other)).result
    def __rmod__(self, other): return nodes.int_modulo(a=self._cast_to_int(other), b=self.value).result
    
    def __itruediv__(self, other):
        from .nodes import int_to_float, divide_node, float_to_int, float_value
        f_self = int_to_float(int_val=self.value).float
        
        if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value
        elif hasattr(other, 'value') and other.__class__.__name__ == "IntVar": f_other = int_to_float(int_val=other.value).float
        elif isinstance(other, (int, float)): f_other = float_value(val=float(other)).value
        elif hasattr(other, 'node'):
            t = other.node.type
            int_nodes = ["IntVariableNode", "GetIntVariableValueNode", "RandomIntNode", "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", "IntDivideNode", "IntModuloNode", "CounterNode"]
            if t in int_nodes: f_other = int_to_float(int_val=other).float
            else: f_other = other
        else: raise TypeError(f"❌ Type Error: Unsupported divisor type '{type(other).__name__}' for division.")

        f_result = divide_node(a=f_self, b=f_other).result
        self.set(float_to_int(float_val=f_result).int)
        return self

    def __truediv__(self, other):
        from .nodes import int_to_float, divide_node, float_value
        f_self = int_to_float(int_val=self.value).float
        
        if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value
        elif hasattr(other, 'value') and other.__class__.__name__ == "IntVar": f_other = int_to_float(int_val=other.value).float
        elif isinstance(other, (int, float)): f_other = float_value(val=float(other)).value
        elif hasattr(other, 'node'):
            t = other.node.type
            int_nodes = ["IntVariableNode", "GetIntVariableValueNode", "RandomIntNode", "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", "IntDivideNode", "IntModuloNode", "CounterNode"]
            if t in int_nodes: f_other = int_to_float(int_val=other).float
            else: f_other = other
        else: raise TypeError(f"❌ Type Error: Unsupported divisor type '{type(other).__name__}' for division.")
            
        return divide_node(a=f_self, b=f_other).result

    def __rtruediv__(self, other):
        from .nodes import int_to_float, divide_node, float_value
        f_self = int_to_float(int_val=self.value).float
        
        if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value
        elif hasattr(other, 'value') and other.__class__.__name__ == "IntVar": f_other = int_to_float(int_val=other.value).float
        elif isinstance(other, (int, float)): f_other = float_value(val=float(other)).value
        elif hasattr(other, 'node'):
            t = other.node.type
            int_nodes = ["IntVariableNode", "GetIntVariableValueNode", "RandomIntNode", "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", "IntDivideNode", "IntModuloNode", "CounterNode"]
            if t in int_nodes: f_other = int_to_float(int_val=other).float
            else: f_other = other
        else: raise TypeError(f"❌ Type Error: Unsupported dividend type '{type(other).__name__}' for division.")
            
        return divide_node(a=f_other, b=f_self).result

    def __ifloordiv__(self, other): self.set(nodes.int_divide(a=self.value, b=self._cast_to_int(other)).result); return self
    def __floordiv__(self, other): return nodes.int_divide(a=self.value, b=self._cast_to_int(other)).result
    def __rfloordiv__(self, other): return nodes.int_divide(a=self._cast_to_int(other), b=self.value).result

    def __imul__(self, other):
        from .nodes import int_to_float, multiply_node, float_to_int, float_value, int_multiply
        is_float_op = False
        if isinstance(other, float) or (hasattr(other, 'value') and other.__class__.__name__ == "FloatVar"): is_float_op = True
        elif hasattr(other, 'node'):
            t = other.node.type
            float_nodes = ["FloatVariableNode", "GetFloatVariableValueNode", "RandomFloatNode", "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"]
            if t in float_nodes: is_float_op = True

        if is_float_op:
            f_self = int_to_float(int_val=self.value).float
            if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value #type: ignore
            elif isinstance(other, float): f_other = float_value(val=other).value
            else: f_other = other
            f_result = multiply_node(a=f_self, b=f_other).result
            self.set(float_to_int(float_val=f_result).int)
        else: self.set(int_multiply(a=self.value, b=self._cast_to_int(other)).result)
        return self

    def __mul__(self, other):
        from .nodes import int_to_float, multiply_node, float_value, int_multiply
        is_float_op = False
        if isinstance(other, float) or (hasattr(other, 'value') and other.__class__.__name__ == "FloatVar"): is_float_op = True
        elif hasattr(other, 'node'):
            t = other.node.type
            float_nodes = ["FloatVariableNode", "GetFloatVariableValueNode", "RandomFloatNode", "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"]
            if t in float_nodes: is_float_op = True

        if is_float_op:
            f_self = int_to_float(int_val=self.value).float
            if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value #type: ignore
            elif isinstance(other, float): f_other = float_value(val=other).value
            else: f_other = other
            return multiply_node(a=f_self, b=f_other).result
        else: return int_multiply(a=self.value, b=self._cast_to_int(other)).result

    def __rmul__(self, other):
        from .nodes import int_to_float, multiply_node, float_value, int_multiply
        is_float_op = False
        if isinstance(other, float) or (hasattr(other, 'value') and other.__class__.__name__ == "FloatVar"): is_float_op = True
        elif hasattr(other, 'node'):
            t = other.node.type
            float_nodes = ["FloatVariableNode", "GetFloatVariableValueNode", "RandomFloatNode", "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"]
            if t in float_nodes: is_float_op = True

        if is_float_op:
            f_self = int_to_float(int_val=self.value).float
            if hasattr(other, 'value') and other.__class__.__name__ == "FloatVar": f_other = other.value #type: ignore
            elif isinstance(other, float): f_other = float_value(val=other).value
            else: f_other = other
            return multiply_node(a=f_other, b=f_self).result
        else: return int_multiply(a=self._cast_to_int(other), b=self.value).result
        
    def __eq__(self, other): return self.value == self._cast_to_int(other) #type: ignore
    def __ne__(self, other): return self.value != self._cast_to_int(other) #type: ignore
    def __gt__(self, other): return self.value > self._cast_to_int(other)
    def __lt__(self, other): return self.value < self._cast_to_int(other)
    def __ge__(self, other): return self.value >= self._cast_to_int(other)
    def __le__(self, other): return self.value <= self._cast_to_int(other)

class FloatVar:
    """Use to create a Variable Float Value. Don't use = to set the value, use .set() instead."""
    def __init__(self, start_val=0.0, node_ref=None):
        self._node = node_ref if node_ref else nodes.float_variable() 
        if start_val != 0.0:
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            init_trigger = nodes.on_board_start()
            ctx.add_connection(init_trigger.id, "触发", nodes.set_float_variable_value(variable=self._node.variable, value=start_val).id, "触发")
            ctx.trigger_stack.extend(saved_stack)

    def _is_float_port(self): return True
    def _get_primary_port(self): return self.value

    @property
    def value(self):
        return nodes.get_float_variable_value(variable=self._node.variable).value

    def set(self, target_value):
        casted_val = self._cast_to_float(target_value)
        set_node = nodes.set_float_variable_value(variable=self._node.variable, value=casted_val)
        if ctx.trigger_stack:
            current = ctx.trigger_stack[-1]
            ctx.add_connection(current.id, current.out_trigger, set_node.id, "触发")
            ctx.trigger_stack[-1] = ExecutionPath(set_node.id, "完成")
        return set_node

    def _cast_to_float(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "FloatVar": return val.value
        if cls_name == "IntVar": return nodes.int_to_float(int_val=val.value).float
        if cls_name == "BoolVar": 
            raise TypeError("❌ Type Error: Cannot implicitly cast a BoolVar to a FloatVar.")
            
        if isinstance(val, bool): return 1.0 if val else 0.0
        if isinstance(val, float): return val
        if isinstance(val, int): return float(val)
            
        if hasattr(val, 'node'):
            t = val.node.type
            int_nodes = ["IntVariableNode", "GetIntVariableValueNode", "RandomIntNode", "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", "IntDivideNode", "IntModuloNode", "CounterNode"]
            if t in int_nodes: return nodes.int_to_float(int_val=val).float
            return val
            
        raise TypeError(f"❌ Type Error: Unsupported type '{type(val).__name__}' passed to FloatVar.")

    def to_string(self, decimals=2):
        from .nodes import float_to_string, int_value
        dec_node = int_value(val=decimals).value 
        return float_to_string(float_val=self.value, decimals=dec_node).result

    def __iadd__(self, other): self.set(nodes.add_node(a=self.value, b=self._cast_to_float(other)).result); return self
    def __isub__(self, other): self.set(nodes.subtract_node(a=self.value, b=self._cast_to_float(other)).result); return self
    def __imul__(self, other): self.set(nodes.multiply_node(a=self.value, b=self._cast_to_float(other)).result); return self
    def __itruediv__(self, other): self.set(nodes.divide_node(a=self.value, b=self._cast_to_float(other)).result); return self

    def __add__(self, other): return nodes.add_node(a=self.value, b=self._cast_to_float(other)).result
    def __radd__(self, other): return nodes.add_node(a=self._cast_to_float(other), b=self.value).result
    def __sub__(self, other): return nodes.subtract_node(a=self.value, b=self._cast_to_float(other)).result
    def __rsub__(self, other): return nodes.subtract_node(a=self._cast_to_float(other), b=self.value).result
    def __mul__(self, other): return nodes.multiply_node(a=self.value, b=self._cast_to_float(other)).result
    def __rmul__(self, other): return nodes.multiply_node(a=self._cast_to_float(other), b=self.value).result
    def __truediv__(self, other): return nodes.divide_node(a=self.value, b=self._cast_to_float(other)).result
    def __rtruediv__(self, other): return nodes.divide_node(a=self._cast_to_float(other), b=self.value).result

    def __eq__(self, other): return self.value == self._cast_to_float(other) #type: ignore
    def __ne__(self, other): return self.value != self._cast_to_float(other) #type: ignore
    def __gt__(self, other): return self.value > self._cast_to_float(other)
    def __lt__(self, other): return self.value < self._cast_to_float(other)
    def __ge__(self, other): return self.value >= self._cast_to_float(other)
    def __le__(self, other): return self.value <= self._cast_to_float(other)

class BoolVar:
    """Use to create a Variable Bool Value. Don't use = to set the value, use .set() instead."""
    def __init__(self, start_val=False, node_ref=None):
        self._node = node_ref if node_ref else nodes.bool_variable() 
        if start_val:
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            init_trigger = nodes.on_board_start()
            ctx.add_connection(init_trigger.id, "触发", nodes.set_bool_variable_value(variable=self._node.variable, value=True).id, "触发")
            ctx.trigger_stack.extend(saved_stack)

    def _is_float_port(self): return False
    def _get_primary_port(self): return self.value

    @property
    def value(self):
        return nodes.get_bool_variable_value(variable=self._node.variable).value

    def set(self, target_state: bool):
        casted_val = self._cast_to_bool(target_state)
        set_node = nodes.set_bool_variable_value(variable=self._node.variable, value=casted_val)
        if ctx.trigger_stack:
            current = ctx.trigger_stack[-1]
            ctx.add_connection(current.id, current.out_trigger, set_node.id, "触发")
            ctx.trigger_stack[-1] = ExecutionPath(set_node.id, "完成")
        return set_node

    def _cast_to_bool(self, val):
        cls_name = val.__class__.__name__
        if cls_name == "BoolVar": return val.value
        if cls_name in ["IntVar", "FloatVar"]:
            raise TypeError("❌ Type Error: Cannot perform implicit boolean logic on numeric Variables.")
            
        if isinstance(val, bool): return val
        if isinstance(val, (int, float)): return bool(val)
            
        if hasattr(val, 'node'):
            t = val.node.type 
            bool_nodes = ["BoolVariableNode", "GetBoolVariableValueNode", "ToggleNode", "CompareIntNode", "CompareFloatNode", "CompareGameObjectNode", "AndNode", "OrNode", "NotNode"]
            if t in bool_nodes: return val
            raise TypeError(f"❌ Type Error: The node output '{t}' is not a valid boolean.")
            
        raise TypeError(f"❌ Type Error: Unsupported type '{type(val).__name__}' passed to BoolVar.")

    def toggle(self):
        with If(self.value == True) as flow:
            self.set(False)
        with flow.Else:
            self.set(True)

    def __iand__(self, other): self.set(nodes.and_node(a=self.value, b=self._cast_to_bool(other)).Output); return self #type: ignore
    def __ior__(self, other): self.set(nodes.or_node(a=self.value, b=self._cast_to_bool(other)).Output); return self #type: ignore

    def __and__(self, other): return nodes.and_node(a=self.value, b=self._cast_to_bool(other)).Output
    def __rand__(self, other): return nodes.and_node(a=self._cast_to_bool(other), b=self.value).Output
    def __or__(self, other): return nodes.or_node(a=self.value, b=self._cast_to_bool(other)).Output
    def __ror__(self, other): return nodes.or_node(a=self._cast_to_bool(other), b=self.value).Output
    def __invert__(self): return nodes.not_node(inp=self.value).Output

    def __eq__(self, other): return self.value == self._cast_to_bool(other) #type: ignore
    def __ne__(self, other): return self.value != self._cast_to_bool(other) #type: ignore

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

#endregion

class MultiSelectMenu:
    """Deferred UI Builder for Multiple Choice Menus."""
    def __init__(self, is_rerollable: bool = True, reroll_count: int = 3, is_skippable: bool = False, window_count: int = 3):
        self.refreshable = is_rerollable
        self.refreshCount = reroll_count
        self.cancelable = is_skippable
        self.windowCount = window_count
        self._options = {}
        self._option_id_counter = 0
        self._show_node_id = None
        self.Output = self._Outputs(self)

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

    def add_option(self, title: str, description: str, callback, plant_type: int = 254, zombie_type: int = -1) -> str:
        opt_id = f"opt_{self._option_id_counter}"
        self._option_id_counter += 1
        self._options[opt_id] = {"title": title, "description": description, "callback": callback, "plant_type": plant_type, "zombie_type": zombie_type}
        return opt_id

    def show(self):
        current_list_node_id, current_list_port_name = None, None
        
        for opt_id, opt_data in self._options.items():
            node_id = ctx.generate_uuid()
            kwargs = {
                "class": "AddMultipleChoiceOptionNode", "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp",
                "title": opt_data["title"], "description": opt_data["description"], "plantType": opt_data["plant_type"], "zombieType": opt_data["zombie_type"],
                "list_PortName": "选项列表", "title_PortName": "标题", "description_PortName": "描述",
                "plantType_PortName": "植物类型", "zombieType_PortName": "僵尸类型", "optionSelected_PortName": "选项被点击"
            }
            ctx.nodes.append({"id": node_id, "type": "AddMultipleChoiceOptionNode", "kwargs": kwargs})
            
            if current_list_node_id:
                ctx.add_connection(current_list_node_id, current_list_port_name, node_id, "选项列表") # type: ignore
            
            current_list_node_id, current_list_port_name = node_id, "选项列表"
            
            if opt_data["callback"]:
                prev_trigger = ctx.trigger_stack[-1]
                class OptionClickTrigger:
                    def __init__(self, n_id): self.id, self.out_trigger = n_id, "选项被点击"
                ctx.trigger_stack[-1] = OptionClickTrigger(node_id)
                opt_data["callback"]()
                ctx.trigger_stack[-1] = prev_trigger

        self._show_node_id = ctx.generate_uuid()
        show_kwargs = {
            "class": "ShowMultipleChoiceMenuNode", "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp",
            "refreshable": self.refreshable, "refreshCount": self.refreshCount, "cancelable": self.cancelable, "windowCount": self.windowCount,
            "trigger_PortName": "触发", "options_PortName": "选项列表", "refreshable_PortName": "可刷新",
            "refreshCount_PortName": "刷新次数", "cancelable_PortName": "可取消", "windowCount_PortName": "窗口数量",
            "actionOnExit_PortName": "退出时触发", "actionOnRefresh_PortName": "刷新时触发"
        }
        ctx.nodes.append({"id": self._show_node_id, "type": "ShowMultipleChoiceMenuNode", "kwargs": show_kwargs})
        
        current_execution = ctx.trigger_stack[-1]
        ctx.add_connection(current_execution.id, current_execution.out_trigger, self._show_node_id, "触发")
        
        if current_list_node_id:
            ctx.add_connection(current_list_node_id, current_list_port_name, self._show_node_id, "选项列表") # type: ignore
            
        ctx.trigger_stack[-1] = nodes.wait_node(0.0)

    class _Outputs:
        def __init__(self, parent): self.parent = parent
        def on_exit(self): return ExecutionPath(self.parent._show_node_id, "退出时触发")
        def on_refresh(self): return ExecutionPath(self.parent._show_node_id, "刷新时触发")           

class ForEachPlant:
    """Safely loops through plants and yields a Plant Object."""
    def __init__(self, plant_list_port):
        self.node = nodes.for_each_plant(plant_list=plant_list_port)
        
    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()   

    @property
    def plant(self):
        """Returns the current iterated plant wrapped in a Smart Object."""
        return Plant(self.node.currentPlant)

    @property
    def index(self):
        return self.node.currentIndex
 
class ForEachPlantType:
    """Safely loops through a list of Plant Types natively."""
    def __init__(self, type_list_port):
        self.node = nodes.for_each_plant_type(type_list=type_list_port)
        
    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.node.id, "循环体"))
        return self.node
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()

class Plant:
    """A smart wrapper for a Plant pointer that exposes built-in actions."""
    def __init__(self, plant_ref):
        self.ref = plant_ref

    def die(self):
        """Instantly destroys the plant."""
        nodes.die_plant(plant=self.ref)

    def damage(self, amount):
        nodes.damage_plant(plant=self.ref, damage=amount)

    def heal(self, amount):
        nodes.heal_plant(plant=self.ref, heal_amount=amount)

    def add_shield(self, amount):
        nodes.give_plant_shield(plant=self.ref, shield=amount)

    def move(self, row, col, force=False):
        """force bypasses all ingame checks."""
        nodes.move_plant(plant=self.ref, row=row, column=col, force=force)
        
    def move_relative(self, row_diff, col_diff, force=False):
        """force bypasses all ingame checks."""
        nodes.move_plant(plant=self.ref, row=self.row + row_diff, column=self.col + col_diff, force=force)

    # Automatically unrolls the plant_split node to fetch properties!
    @property
    def plantType(self): return nodes.plant_split(plant=self.ref).plantType
    
    @property
    def row(self): return nodes.plant_split(plant=self.ref).row
    
    @property
    def col(self): return nodes.plant_split(plant=self.ref).column
    
    @property
    def attributeCD(self): return nodes.plant_split(plant=self.ref).attributeCountdown

class Zombie:
    """A smart wrapper for a Zombie pointer that exposes built-in actions."""
    def __init__(self, zombie_ref):
        self.ref = zombie_ref

    def damage(self, amount):
        nodes.damage_zombie(zombie=self.ref, damage=amount)

    def set_health_multiplier(self, ratio):
        nodes.modify_zombie_health(zombie=self.ref, ratio=ratio)

    def hypnotize(self):
        nodes.set_zombie_mind_controlled(zombie=self.ref)

    def move(self, row, col):
        nodes.move_zombie(zombie=self.ref, row=row, column=col)

    def play_animation(self, anim_name : str | ZombieAnimation = "idle"): # type: ignore
        if isinstance(anim_name, Enum):
            anim_name = anim_name.value
        nodes.play_zombie_anim(zombie=self.ref, animation_name=anim_name)
    
    @property
    def zombieType(self): return nodes.zombie_split(zombie=self.ref).zombieType
    
    @property
    def row(self): return nodes.zombie_split(zombie=self.ref).row
    
    @property
    def col(self): return nodes.zombie_split(zombie=self.ref).column
    
class While:
    """
    A continuous execution loop that runs as long as a condition port evaluates to True.
    
    Usage:
        with pvn.While(sun_boost < 500):
            sun_boost += 10
    """
    def __init__(self, condition):
        self.branch = nodes.branch_node(condition=condition)
        
    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.branch.id, "真（触发）"))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.add_connection(self.branch.id, "真（触发）", self.branch.id, "触发")
        ctx.trigger_stack.pop()

class For:
    """
    A fixed-count loop structure that runs an execution block a specified number of times.
    Exposes the current loop index port dynamically.
    
    Usage:
        with pvn.For(5) as loop:
            pvn.Zombie.spawn(row=loop.index, column=10, zombie_type=0)
    """
    def __init__(self, count):
        self.loop_node = nodes.for_loop_node(count=count)
        
    def __enter__(self):
        ctx.trigger_stack.append(ExecutionPath(self.loop_node.id, "循环体"))
        return self

    @property
    def index(self):
        """Allows access to the loop index tracking output port directly inside scripts."""
        return (self.loop_node, "当前索引")

    def __exit__(self, exc_type, exc_val, exc_tb):
        ctx.trigger_stack.pop()
    
class Mathf:
    """Commonly used math functions"""
    
    class Counter:
        """
        A high-level wrapper for the Engine's native CounterNode.
        
        Usage:
            zombie_counter = pvn.Counter(start_val=0, reset_condition=is_wave_over)
            
            with pvn.nodes.on_zombie_die().trigger:
                zombie_counter.up()
        """
        def __init__(self, start_val=0, reset_condition=None):
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            
            self.ref = nodes.counter_node(start_val=start_val, reset=reset_condition)
            
            ctx.trigger_stack.extend(saved_stack)

        def up(self):
            """Increments the counter by 1 manually along the current execution timeline track."""
            if ctx.trigger_stack:
                previous_exec = ctx.trigger_stack[-1]
                ctx.add_connection(previous_exec.id, previous_exec.out_trigger, self.ref.id, "触发")
                
                ctx.trigger_stack[-1] = ExecutionPath(self.ref.id, "触发")
            return self

        @property
        def value(self):
            """Returns the data output port reference containing the current count."""
            return self.ref.count

        @property
        def on_count(self):
            """Exposes the '计数完成' execution track as a context manager timeline path."""
            return self.ref.path("计数完成")

    @staticmethod
    def abs(val):
        """
        Returns the absolute value of an integer or float wire configuration.
        Calculates natively via: result = (val < 0) ? (val * -1) : val
        """
        from . import nodes
        from .node_base import PortReference
        
        if isinstance(val, (int, float)) and not isinstance(val, PortReference):
            return abs(val)

        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        is_negative = val < 0 
        branch = nodes.branch_node(condition=is_negative)

        ctx.trigger_stack.append(ExecutionPath(branch.id, "真（触发）"))
        inverted_val = val * -1
        ctx.trigger_stack.pop()

        ctx.trigger_stack.extend(saved_stack)
        
        is_float = hasattr(val, "_is_float_port") and val._is_float_port()
        if is_float:
            result_reg = nodes.float_variable(var_name="abs_temp_f")
            ctx.add_connection(branch.id, "真（触发）", nodes.set_float_variable_value(variable=result_reg.variable, value=inverted_val).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_float_variable_value(variable=result_reg.variable, value=val).id, "触发")
            
            final_port = nodes.get_float_variable_value(variable=result_reg.variable).value
        else:
            result_reg = nodes.int_variable(var_name="abs_temp_i")
            
            ctx.add_connection(branch.id, "真（触发）", nodes.set_int_variable_value(variable=result_reg.variable, value=inverted_val).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_int_variable_value(variable=result_reg.variable, value=val).id, "触发")
            
            final_port = nodes.get_int_variable_value(variable=result_reg.variable).value

        if ctx.trigger_stack:
            prev_node = ctx.trigger_stack[-1]
            ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, "触发")
            ctx.trigger_stack[-1] = ExecutionPath(branch.id, "真（触发）")

        return final_port

    @staticmethod
    def max(*args):
        """
        Returns the largest of a variable number of arguments or a sequence loop.
        Usage: 
            Mathf.max(val1, val2, val3) or Mathf.max([val1, val2, val3])
        """
        from .node_base import PortReference
        
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            args = args[0]
            
        if not args:
            raise ValueError("Mathf.max() requires at least one argument.")
            
        if all(isinstance(x, (int, float)) and not isinstance(x, PortReference) for x in args):
            return max(args)

        res = args[0]
        for next_val in args[1:]:
            res = Mathf._binary_max(res, next_val)
        return res

    @staticmethod
    def _binary_max(a, b):
        """Internal helper to compare exactly two values inside the node graph."""
        from . import nodes
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        branch = nodes.branch_node(condition=(a > b))
        
        is_float = (hasattr(a, "_is_float_port") and a._is_float_port()) or (hasattr(b, "_is_float_port") and b._is_float_port())
        if is_float:
            reg = nodes.float_variable(var_name="max_temp_f")
            ctx.add_connection(branch.id, "真（触发）", nodes.set_float_variable_value(variable=reg.variable, value=a).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_float_variable_value(variable=reg.variable, value=b).id, "触发")
            final_port = nodes.get_float_variable_value(variable=reg.variable).value
        else:
            reg = nodes.int_variable(var_name="max_temp_i")
            ctx.add_connection(branch.id, "真（触发）", nodes.set_int_variable_value(variable=reg.variable, value=a).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_int_variable_value(variable=reg.variable, value=b).id, "触发")
            final_port = nodes.get_int_variable_value(variable=reg.variable).value

        ctx.trigger_stack.extend(saved_stack)
        if ctx.trigger_stack:
            prev_node = ctx.trigger_stack[-1]
            ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, "触发")
            ctx.trigger_stack[-1] = ExecutionPath(branch.id, "真（触发）")

        return final_port

    @staticmethod
    def min(*args):
        """
        Returns the smallest of a variable number of arguments or a sequence loop.
        Usage: 
            Mathf.min(val1, val2, val3) or Mathf.min([val1, val2, val3])
        """
        from .node_base import PortReference
        
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            args = args[0]
            
        if not args:
            raise ValueError("Mathf.min() requires at least one argument.")
            
        if all(isinstance(x, (int, float)) and not isinstance(x, PortReference) for x in args):
            return min(args)

        res = args[0]
        for next_val in args[1:]:
            res = Mathf._binary_min(res, next_val)
        return res

    @staticmethod
    def _binary_min(a, b):
        """Internal helper to compare exactly two values inside the node graph."""
        from . import nodes
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        branch = nodes.branch_node(condition=(a < b))
        
        is_float = (hasattr(a, "_is_float_port") and a._is_float_port()) or (hasattr(b, "_is_float_port") and b._is_float_port())
        if is_float:
            reg = nodes.float_variable(var_name="min_temp_f")
            ctx.add_connection(branch.id, "真（触发）", nodes.set_float_variable_value(variable=reg.variable, value=a).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_float_variable_value(variable=reg.variable, value=b).id, "触发")
            final_port = nodes.get_float_variable_value(variable=reg.variable).value
        else:
            reg = nodes.int_variable(var_name="min_temp_i")
            ctx.add_connection(branch.id, "真（触发）", nodes.set_int_variable_value(variable=reg.variable, value=a).id, "触发")
            ctx.add_connection(branch.id, "假（停止）", nodes.set_int_variable_value(variable=reg.variable, value=b).id, "触发")
            final_port = nodes.get_int_variable_value(variable=reg.variable).value

        ctx.trigger_stack.extend(saved_stack)
        if ctx.trigger_stack:
            prev_node = ctx.trigger_stack[-1]
            ctx.add_connection(prev_node.id, prev_node.out_trigger, branch.id, "触发")
            ctx.trigger_stack[-1] = ExecutionPath(branch.id, "真（触发）")

        return final_port

class Time:
    
    class OnFixedUpdate:
        """
        High-frequency/timed event loop driven natively by ToggleCycleNode.
        Runs 20 times a second by default.
        Features a lazy-loaded frame tracker.
        
        ### Usage:
            with pvn.Time.OnFixedUpdate(interval=0.05) as update:
                pvn.Board.Sun += 1
                with pvn.If(update.tick == 100):
                    pvn.show_message("100 ticks have passed!")
        """
        def __init__(self, interval:float=0.05):
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            
            self.ref = nodes.toggle_cycle_node(interval=interval)
            
            ctx.trigger_stack.extend(saved_stack)
            
            if ctx.trigger_stack:
                previous_exec = ctx.trigger_stack[-1]
                ctx.add_connection(previous_exec.id, previous_exec.out_trigger, self.ref.id, "触发")
                
            self._counter = None 

        def __enter__(self):
            """Defaults straight into the repeating execution track loop body."""
            ctx.trigger_stack.append(ExecutionPath(self.ref.id, "周期事件"))
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            ctx.trigger_stack.pop()

        @property
        def tick(self):
            """
            Lazy getter. Spawns and wires an active CounterNode tracking the loop 
            the very first time this property is read in a level script.
            """
            if self._counter is None:
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()
                
                self._counter = nodes.counter_node(start_val=0, reset=None)
                
                ctx.add_connection(self.ref.id, "周期事件", self._counter.id, "触发")
                
                ctx.trigger_stack.extend(saved_stack)
                
            return self._counter.count

        @property
        def on_cycle(self):
            """Explicit access to the repeating loop execution track."""
            return ExecutionPath(self.ref.id, "周期事件")

        @property
        def on_enable(self):
            """Timeline track fired the exact instant the loop engine activates."""
            return ExecutionPath(self.ref.id, "切换开始时")

        @property
        def on_disable(self):
            """Timeline track fired when the loop engine is turned off."""
            return ExecutionPath(self.ref.id, "切换关闭时")

    class Wait:
        """A clean Syntactic Sugar context manager to pause execution timelines."""
        def __init__(self, duration):
            self.node = nodes.wait_node(duration=duration)
            
        def __enter__(self):
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "触发"))
            return self
            
        def __exit__(self, exc_type, exc_val, exc_tb):
            ctx.trigger_stack.pop()




