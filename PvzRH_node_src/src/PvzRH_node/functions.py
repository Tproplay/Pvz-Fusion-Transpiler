from . import nodes
from .core import ctx
from .node_base import ExecutionPath, BaseNode
from .extensions import *

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






