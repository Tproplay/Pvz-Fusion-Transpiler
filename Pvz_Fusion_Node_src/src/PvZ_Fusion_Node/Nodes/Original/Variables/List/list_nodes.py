"""
Low-level node definitions for Unity EventNodes list operations.
Supports Int, Float, Bool, String, PlantType, ZombieType, and Object lists.
"""

from typing import Optional
from ...Node import Node, PortDef, PortDirection, PortType


# =============================================================================
# APPEND NODES
# =============================================================================

class AppendIntListNode(Node):
    # Status in Extensions: Implemented
    node_type = "AppendIntListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Value_input_int : str = "值"
    Complete_output_trigger : str = "完成"

class AppendFloatListNode(Node):
    # Status in Extensions: Implemented
    node_type = "AppendFloatListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Value_input_float : str = "值"
    Complete_output_trigger : str = "完成"

class AppendBoolListNode(Node):
    # Status in Extensions: Implemented
    node_type = "AppendBoolListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Bool),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Value_input_bool : str = "值"
    Complete_output_trigger : str = "完成"

class AppendStringListNode(Node):
    # Status in Extensions: Implemented
    node_type = "AppendStringListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.String),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Value_input_string : str = "值"
    Complete_output_trigger : str = "完成"

class AppendPlantTypeListNode(Node):
    # Status in Extensions: Implemented
    node_type = "AppendPlantTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.PlantType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Value_input_planttype : str = "值"
    Complete_output_trigger : str = "完成"

class AppendZombieTypeListNode(Node):
    # Status in Extensions: Implemented
    node_type = "AppendZombieTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.ZombieType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Value_input_zombietype : str = "值"
    Complete_output_trigger : str = "完成"

class AppendObjectListNode(Node):
    # Status in Extensions: Implemented
    node_type = "AppendObjectListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.GameObject),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Value_input_gameobject : str = "值"
    Complete_output_trigger : str = "完成"


# =============================================================================
# INSERT NODES
# =============================================================================

class InsertIntListNode(Node):
    # Status in Extensions: Implemented
    node_type = "InsertIntListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_int : str = "值"
    Complete_output_trigger : str = "完成"

class InsertFloatListNode(Node):
    # Status in Extensions: Implemented
    node_type = "InsertFloatListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_float : str = "值"
    Complete_output_trigger : str = "完成"

class InsertBoolListNode(Node):
    # Status in Extensions: Implemented
    node_type = "InsertBoolListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Bool),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_bool : str = "值"
    Complete_output_trigger : str = "完成"

class InsertStringListNode(Node):
    # Status in Extensions: Implemented
    node_type = "InsertStringListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.String),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_string : str = "值"
    Complete_output_trigger : str = "完成"

class InsertPlantTypeListNode(Node):
    # Status in Extensions: Implemented
    node_type = "InsertPlantTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.PlantType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_planttype : str = "值"
    Complete_output_trigger : str = "完成"

class InsertZombieTypeListNode(Node):
    # Status in Extensions: Implemented
    node_type = "InsertZombieTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.ZombieType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_zombietype : str = "值"
    Complete_output_trigger : str = "完成"

class InsertObjectListNode(Node):
    # Status in Extensions: Implemented
    node_type = "InsertObjectListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.GameObject),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_gameobject : str = "值"
    Complete_output_trigger : str = "完成"


# =============================================================================
# REPLACE NODES
# =============================================================================

class ReplaceIntListNode(Node):
    # Status in Extensions: Implemented
    node_type = "ReplaceIntListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_int : str = "值"
    Complete_output_trigger : str = "完成"

class ReplaceFloatListNode(Node):
    # Status in Extensions: Implemented
    node_type = "ReplaceFloatListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_float : str = "值"
    Complete_output_trigger : str = "完成"

class ReplaceBoolListNode(Node):
    # Status in Extensions: Implemented
    node_type = "ReplaceBoolListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Bool),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_bool : str = "值"
    Complete_output_trigger : str = "完成"

class ReplaceStringListNode(Node):
    # Status in Extensions: Implemented
    node_type = "ReplaceStringListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.String),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_string : str = "值"
    Complete_output_trigger : str = "完成"

class ReplacePlantTypeListNode(Node):
    # Status in Extensions: Implemented
    node_type = "ReplacePlantTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.PlantType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_planttype : str = "值"
    Complete_output_trigger : str = "完成"

class ReplaceZombieTypeListNode(Node):
    # Status in Extensions: Implemented
    node_type = "ReplaceZombieTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.ZombieType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_zombietype : str = "值"
    Complete_output_trigger : str = "完成"

class ReplaceObjectListNode(Node):
    # Status in Extensions: Implemented
    node_type = "ReplaceObjectListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.GameObject),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_input_gameobject : str = "值"
    Complete_output_trigger : str = "完成"


# =============================================================================
# GET ITEM NODES
# =============================================================================

class GetIntListItemNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetIntListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.Int),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_output_int : str = "值"

class GetFloatListItemNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetFloatListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.Float),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_output_float : str = "值"

class GetBoolListItemNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetBoolListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_output_bool : str = "值"

class GetStringListItemNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetStringListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.String),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_output_string : str = "值"

class GetPlantTypeListItemNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetPlantTypeListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.PlantType),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_output_planttype : str = "值"

class GetZombieTypeListItemNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetZombieTypeListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.ZombieType),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_output_zombietype : str = "值"

class GetObjectListItemNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetObjectListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.GameObject),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Value_output_gameobject : str = "值"


# =============================================================================
# FIND VALUE NODES
# =============================================================================

class FindIntListValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "FindIntListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Int),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Value_input_int : str = "值"
    Index_output_int : str = "索引"
    Exists_output_bool : str = "存在"

class FindFloatListValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "FindFloatListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Float),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Value_input_float : str = "值"
    Index_output_int : str = "索引"
    Exists_output_bool : str = "存在"

class FindBoolListValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "FindBoolListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Bool),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Value_input_bool : str = "值"
    Index_output_int : str = "索引"
    Exists_output_bool : str = "存在"

class FindStringListValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "FindStringListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.String),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Value_input_string : str = "值"
    Index_output_int : str = "索引"
    Exists_output_bool : str = "存在"

class FindPlantTypeListValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "FindPlantTypeListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.PlantType),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Value_input_planttype : str = "值"
    Index_output_int : str = "索引"
    Exists_output_bool : str = "存在"

class FindZombieTypeListValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "FindZombieTypeListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.ZombieType),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Value_input_zombietype : str = "值"
    Index_output_int : str = "索引"
    Exists_output_bool : str = "存在"

class FindObjectListValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "FindObjectListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.GameObject),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Value_input_gameobject : str = "值"
    Index_output_int : str = "索引"
    Exists_output_bool : str = "存在"


# =============================================================================
# GENERAL LIST UTILITY NODES
# =============================================================================

class ClearListValuesNode(Node):
    # Status in Extensions: Implemented
    node_type = "ClearListValuesNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Complete_output_trigger : str = "完成"

class RemoveListItemNode(Node):
    # Status in Extensions: Implemented
    node_type = "RemoveListItemNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    List_input_listvariable : str = "列表"
    Index_input_int : str = "索引"
    Complete_output_trigger : str = "完成"

class GetListLengthNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetListLengthNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "长度": PortDef("长度", PortDirection.Output, PortType.Int),
    }

    # Port name constants
    List_input_listvariable : str = "列表"
    Length_output_int : str = "长度"

class CopyListValuesNode(Node):
    # Status in Extensions: Implemented
    node_type = "CopyListValuesNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "源列表": PortDef("源列表", PortDirection.Input, PortType.ListVariable),
        "目标列表": PortDef("目标列表", PortDirection.Input, PortType.ListVariable),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    SourceList_input_listvariable : str = "源列表"
    TargetList_input_listvariable : str = "目标列表"
    Complete_output_trigger : str = "完成"
