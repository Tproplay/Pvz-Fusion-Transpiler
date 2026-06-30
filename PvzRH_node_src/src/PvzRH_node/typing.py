from .core import ctx

def enforce_int(value) -> str:
    if hasattr(value, "id"): return value.id
    if isinstance(value, str): raise TypeError(f"Cannot cast string '{value}' to an Integer.")
    
    value = int(value) if isinstance(value, float) else value
    value = 1 if isinstance(value, bool) else value

    node_id = ctx.generate_uuid()
    ctx.nodes.append({
        "id": node_id, 
        "type": "IntValueNode", 
        "kwargs": {
            "value": int(value),
            "value_PortName": "值"
        }
    })
    return node_id

def enforce_float(value) -> str:
    if hasattr(value, "id"): return value.id
    if isinstance(value, str): raise TypeError(f"Cannot cast string '{value}' to a Float.")

    node_id = ctx.generate_uuid()
    ctx.nodes.append({
        "id": node_id, 
        "type": "FloatValueNode", 
        "kwargs": {
            "value": float(value),
            "value_PortName": "值"
        }
    })
    return node_id

def enforce_bool(value) -> str:
    if hasattr(value, "id"): return value.id
    node_id = ctx.generate_uuid()
    ctx.nodes.append({
        "id": node_id, 
        "type": "BoolValueNode", 
        "kwargs": {
            "value": bool(value),
            "value_PortName": "值"
        }
    })
    return node_id

def enforce_string(value) -> str:
    if hasattr(value, "id"): return value.id
    node_id = ctx.generate_uuid()
    ctx.nodes.append({
        "id": node_id, 
        "type": "StringValueNode", 
        "kwargs": {
            "value": str(value),
            "value_PortName": "值"
        }
    })
    return node_id