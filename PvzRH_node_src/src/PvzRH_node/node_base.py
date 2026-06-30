import uuid
from .core import ctx

class PortReference(tuple):
    def __new__(cls, node, port_name):
        return super().__new__(cls, (node, port_name))

    @property
    def node(self): return self[0]
    @property
    def port_name(self): return self[1]

    # ==========================================================
    # TYPE-SAFE MATH ENGINE (Prevents Unity C# Cast Crashes)
    # ==========================================================
    def _is_float_port(self):
        """Intelligently detects if the underlying Unity node outputs a Float."""
        t = self.node.type
        float_nodes = ["FloatValueNode", "RandomFloatNode", "IntToFloatNode", "AddNode", "SubtractNode", "MultiplyNode", "DivideNode"]
        int_nodes = ["IntValueNode", "RandomIntNode", "FloatToIntNode", "IntAddNode", "IntSubtractNode", "IntMultiplyNode", "IntDivideNode", "IntModuloNode", "CounterNode"]
        
        if t in float_nodes: return True
        if t in int_nodes: return False
        if "Float" in t and "ToInt" not in t: return True
        return False

    def _ensure_float(self, val):
        """Forces any value or node into a safe Float Port."""
        from . import nodes
        if isinstance(val, float): return nodes.float_value(val=val).value
        if isinstance(val, int): return nodes.float_value(val=float(val)).value
        if hasattr(val, "_is_float_port") and val._is_float_port(): return val
        return nodes.int_to_float(int_val=val).float

    def _ensure_int(self, val):
        """Forces any value or node into a safe Int Port."""
        from . import nodes
        if isinstance(val, int): return nodes.int_value(val=val).value
        if isinstance(val, float): return nodes.int_value(val=int(val)).value
        if hasattr(val, "_is_float_port") and not val._is_float_port(): return val
        return nodes.float_to_int(float_val=val).int

    def _execute_op(self, other, op_type):
        from . import nodes
        
        self_is_f = self._is_float_port()
        other_is_f = isinstance(other, float) or (hasattr(other, "_is_float_port") and other._is_float_port())
        
        # If either side is a Float, elevate the entire operation to Float Math
        if self_is_f or other_is_f:
            f_self = self._ensure_float(self)
            f_other = self._ensure_float(other)
            
            if op_type == "add": return nodes.add_node(a=f_self, b=f_other).result
            elif op_type == "sub": return nodes.subtract_node(a=f_self, b=f_other).result
            elif op_type == "mul": return nodes.multiply_node(a=f_self, b=f_other).result
            elif op_type == "div": return nodes.divide_node(a=f_self, b=f_other).result
            elif op_type == "mod": raise TypeError("Modulo operations are not supported on Float configurations.")
            
        # Otherwise, perform safe Integer Math
        else:
            i_self = self._ensure_int(self)
            i_other = self._ensure_int(other)
            
            if op_type == "add": return nodes.int_add(a=i_self, b=i_other).result
            elif op_type == "sub": 
                # ENGINE BUG BYPASS: Unity's IntSubtractNode is natively broken. 
                # Route all Int Subtraction through the Float nodes safely!
                f_a = nodes.int_to_float(int_val=i_self).float
                f_b = nodes.int_to_float(int_val=i_other).float
                f_sub = nodes.subtract_node(a=f_a, b=f_b).result
                return nodes.float_to_int(float_val=f_sub).int
                
            elif op_type == "mul": return nodes.int_multiply(a=i_self, b=i_other).result
            elif op_type == "div": return nodes.int_divide(a=i_self, b=i_other).result
            elif op_type == "mod": return nodes.int_modulo(a=i_self, b=i_other).result

    def _execute_rop(self, other, op_type):
        from . import nodes
        if isinstance(other, (int, float)):
            wrapped = nodes.float_value(val=float(other)).value if isinstance(other, float) else nodes.int_value(val=int(other)).value
            return wrapped._execute_op(self, op_type)
        return other._execute_op(self, op_type)

    def _execute_comp(self, other, comp_type):
        from . import nodes
        
        self_is_f = self._is_float_port()
        other_is_f = isinstance(other, float) or (hasattr(other, "_is_float_port") and other._is_float_port())
        
        if self_is_f or other_is_f:
            f_self = self._ensure_float(self)
            f_other = self._ensure_float(other)
            comp_node = nodes.compare_float(a=f_self, b=f_other)
        else:
            i_self = self._ensure_int(self)
            i_other = self._ensure_int(other)
            comp_node = nodes.compare_int(a=i_self, b=i_other)

        if comp_type == "eq": return comp_node.equal
        if comp_type == "gt": return comp_node.greater
        if comp_type == "lt": return comp_node.less
        if comp_type == "ne": return nodes.not_node(inp=comp_node.equal).output
        if comp_type == "ge": return nodes.not_node(inp=comp_node.less).output
        if comp_type == "le": return nodes.not_node(inp=comp_node.greater).output

    def _to_string_port(self):
        """Magically auto-casts any Integer or Float node into a String node!"""
        from . import nodes
        
        if "String" in self.node.type or "Concat" in self.node.type:
            return self
            
        # FIX: Uses the typing engine to know if it's REALLY a float
        if self._is_float_port():
            return nodes.float_to_string(float_val=self, decimals=1).result
            
        # If it's a true integer, cast it to 0 decimals!
        f_val = nodes.int_to_float(int_val=self).float
        return nodes.float_to_string(float_val=f_val, decimals=0).result

    def __add__(self, other):
        if hasattr(other, "_get_primary_port"): other = other._get_primary_port()
        elif hasattr(other, 'value'): other = other.value
            
        from . import nodes
        
        is_other_str = isinstance(other, str) or (hasattr(other, 'node') and ("String" in other.node.type or "Concat" in other.node.type))
        is_self_str = "String" in self.node.type or "Concat" in self.node.type
        
        if is_other_str or is_self_str:
            str_self = self._to_string_port()
            str_other = nodes.string_value(val=other).value if isinstance(other, str) else other._to_string_port()
            return nodes.string_concat(a=str_self, b=str_other).result

        return self._execute_op(other, "add")

    def __radd__(self, other):
        if hasattr(other, "_get_primary_port"): other = other._get_primary_port()
        elif hasattr(other, 'value'): other = other.value
            
        from . import nodes
        
        if isinstance(other, str):
            str_self = self._to_string_port()
            str_other = nodes.string_value(val=other).value
            return nodes.string_concat(a=str_other, b=str_self).result
            
        return self._execute_rop(other, "add")
    
    def __sub__(self, other): return self._execute_op(other, "sub")
    def __mul__(self, other): return self._execute_op(other, "mul")
    def __truediv__(self, other): return self._execute_op(other, "div")
    def __mod__(self, other): return self._execute_op(other, "mod")
    def __rsub__(self, other): return self._execute_rop(other, "sub")
    def __rmul__(self, other): return self._execute_rop(other, "mul")
    def __rtruediv__(self, other): return self._execute_rop(other, "div")
    def __rmod__(self, other): return self._execute_rop(other, "mod")

    # Inside node_base.py -> class PortReference(tuple):

    def __eq__(self, other):
        from . import nodes
        from enum import Enum
        
        if self.port_name == "植物类型":
            if isinstance(other, Enum):
                other = other.value
                
            if isinstance(other, int):
                other_node = nodes.plant_type_value(val=other)
                other = other_node.value

            return nodes.compare_plant_type(a=self, b=other).equal
        
        if self.port_name == "僵尸类型":
            if isinstance(other, Enum): 
                other = other.value
                
            if isinstance(other, int):
                other_node = nodes.zombie_type_value(val=other)
                other = other_node.value

            return nodes.compare_zombie_type(a=self, b=other).equal

        return self._execute_comp(other, "eq")

    def __ne__(self, other):
        from . import nodes
        from enum import Enum
        
        if self.port_name == "植物类型":
            if isinstance(other, Enum):
                other = other.value
                
            if isinstance(other, int):
                other = nodes.plant_type_value(val=other).value
                
            eq_port = nodes.compare_plant_type(a=self, b=other).equal
            return nodes.not_node(inp=eq_port).output
        
        if self.port_name == "僵尸类型":
            if isinstance(other, Enum):
                other = other.value
                
            if isinstance(other, int):
                other = nodes.zombie_type_value(val=other).value
                
            eq_port = nodes.compare_zombie_type(a=self, b=other).equal
            return nodes.not_node(inp=eq_port).output
            
        return self._execute_comp(other, "ne")
    
    def __gt__(self, other): return self._execute_comp(other, "gt")
    def __lt__(self, other): return self._execute_comp(other, "lt")
    def __ge__(self, other): return self._execute_comp(other, "ge")
    def __le__(self, other): return self._execute_comp(other, "le")

    def __and__(self, other):
        from . import nodes
        return nodes.and_node(a=self, b=other).output  

    def __or__(self, other):
        from . import nodes
        return nodes.or_node(a=self, b=other).output

class ExecutionPath:
    def __init__(self, parent_id: str, out_trigger: str):
        self.id = parent_id
        self.out_trigger = out_trigger
    def __enter__(self): ctx.trigger_stack.append(self); return self
    def __exit__(self, exc_type, exc_val, exc_tb): ctx.trigger_stack.pop()

class PathAccessor:
    def __init__(self, node): self._node = node
    def __getattr__(self, name):
        if name in self._node._port_map: return self._node.path(name)
        normalized = name[0].lower() + name[1:]
        if normalized in self._node._port_map: return self._node.path(normalized)
        return self._node.path(name)
    def __dir__(self):
        ports = list(self._node._port_map.keys())
        return list(super().__dir__()) + ports + [k[0].upper() + k[1:] for k in ports if k]

class BaseNode:
    def __init__(self, node_type: str, out_trigger: str = "触发", in_trigger: str = "触发", **kwargs):
        self.id = ctx.generate_uuid()
        self.type = node_type
        self.out_trigger = out_trigger
        self.in_trigger = in_trigger
        self.kwargs = kwargs
        
        self._port_map = {}
        for key, val in kwargs.items():
            if key.endswith("_PortName") and isinstance(val, str):
                self._port_map[key.replace("_PortName", "")] = val
                
        ctx.nodes.append({"id": self.id, "type": self.type, "kwargs": self.kwargs})
        
        from .core import settings
        if settings.group_level >= 1:
            import inspect
            
            target_line = None
            user_frame_info = None
            
            # Pass 1: Attempt to find the primary __main__ script workspace frame
            for frame_info in inspect.stack():
                frame = frame_info.frame
                if frame.f_globals.get('__name__') == '__main__':
                    user_frame_info = frame_info
                    break
            
            # Pass 2: Fallback if running inside internal math operations or auto-casting wrappers
            if user_frame_info is None:
                for frame_info in inspect.stack():
                    filename = frame_info.filename
                    # Find the first file that isn't part of the core library framework files
                    if not any(x in filename for x in ["core.py", "node_base.py", "nodes.py", "extensions.py", "mathf.py"]):
                        user_frame_info = frame_info
                        break
            
            if user_frame_info:
                filename = user_frame_info.filename
                lineno = user_frame_info.lineno
                
                if not hasattr(ctx, '_file_cache'):
                    ctx._file_cache = {}
                if filename not in ctx._file_cache:
                    try:
                        with open(filename, "r", encoding="utf-8") as f:
                            ctx._file_cache[filename] = f.readlines()
                    except Exception:
                        ctx._file_cache[filename] = []
                
                lines = ctx._file_cache[filename]
                idx = lineno - 1
                
                if idx < len(lines):
                    if settings.group_level == 1:
                        target_line = lines[idx].strip()
                    else:
                        # Hierarchical block simulation for level 2+
                        context_stack = []
                        for i in range(min(idx + 1, len(lines))):
                            line_text = lines[i]
                            if not line_text.strip() or line_text.strip().startswith("#"):
                                continue
                            indent = len(line_text) - len(line_text.lstrip())
                            
                            while context_stack and context_stack[-1]["indent"] >= indent:
                                context_stack.pop()
                                
                            if line_text.rstrip().endswith(":"):
                                context_stack.append({"text": line_text.strip(), "indent": indent})
                        
                        if context_stack:
                            target_idx = -(settings.group_level - 1)
                            if abs(target_idx) <= len(context_stack):
                                target_line = context_stack[target_idx]["text"]
                            else:
                                target_line = context_stack[0]["text"]
                        else:
                            target_line = lines[idx].strip()
            
            if not target_line:
                target_line = "Custom Action"

            if target_line not in ctx.groups_map:
                ctx.groups_map[target_line] = {
                    "groupId": ctx.generate_uuid(),
                    "nodeIds": [],
                    "position": {"x": 0.0, "y": 0.0}
                }
            ctx.groups_map[target_line]["nodeIds"].append(self.id)
            # =====================================================================

        self.is_flow_node = "trigger_PortName" in kwargs
        
        is_event_root = "Node" in node_type and (
            node_type.startswith("On") or 
            "Event" in node_type or 
            "Click" in node_type or 
            "Press" in node_type
        )

        if self.is_flow_node and ctx.trigger_stack and not is_event_root:
            previous_node = ctx.trigger_stack[-1]
            ctx.add_connection(previous_node.id, previous_node.out_trigger, self.id, self.in_trigger)
            if not isinstance(previous_node, ExecutionPath):
                ctx.trigger_stack[-1] = self
    @property
    def Output(self): return PathAccessor(self)

    def __getattr__(self, name):
        if name in self._port_map: return PortReference(self, self._port_map[name])
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{name}'")

    def __dir__(self): return list(super().__dir__()) + list(self._port_map.keys())

    def _get_primary_port(self):
        for candidate in ["value", "result", "sum", "count", "currentPlant", "resultList"]:
            if candidate in self._port_map: return getattr(self, candidate)
        if self._port_map: return getattr(self, list(self._port_map.keys())[0])
        return PortReference(self, "值")

    def __add__(self, other): return self._get_primary_port().__add__(other)
    def __sub__(self, other): return self._get_primary_port().__sub__(other)
    def __mul__(self, other): return self._get_primary_port().__mul__(other)
    def __truediv__(self, other): return self._get_primary_port().__truediv__(other)
    def __mod__(self, other): return self._get_primary_port().__mod__(other)
    def __radd__(self, other): return self._get_primary_port().__radd__(other)
    def __rsub__(self, other): return self._get_primary_port().__rsub__(other)
    def __rmul__(self, other): return self._get_primary_port().__rmul__(other)
    def __rtruediv__(self, other): return self._get_primary_port().__rtruediv__(other)
    def __rmod__(self, other): return self._get_primary_port().__rmod__(other)

    def __eq__(self, other): return self._get_primary_port().__eq__(other)
    def __ne__(self, other): return self._get_primary_port().__ne__(other)
    def __gt__(self, other): return self._get_primary_port().__gt__(other)
    def __lt__(self, other): return self._get_primary_port().__lt__(other)
    def __ge__(self, other): return self._get_primary_port().__ge__(other)
    def __le__(self, other): return self._get_primary_port().__le__(other)
    def __bool__(self): return self._get_primary_port().__bool__()
    
    def path(self, trigger_name: str) -> ExecutionPath:
        return ExecutionPath(self.id, self._port_map.get(trigger_name, trigger_name))

    def add_trigger(self, target_node) -> None:
        ctx.add_connection(self.id, self.out_trigger, target_node.id, target_node.in_trigger)

    def __enter__(self): ctx.trigger_stack.append(self); return self
    def __exit__(self, exc_type, exc_val, exc_tb): ctx.trigger_stack.pop()



