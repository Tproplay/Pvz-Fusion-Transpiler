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
    node_type = "AppendIntListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class AppendFloatListNode(Node):
    node_type = "AppendFloatListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class AppendBoolListNode(Node):
    node_type = "AppendBoolListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Bool),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class AppendStringListNode(Node):
    node_type = "AppendStringListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.String),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class AppendPlantTypeListNode(Node):
    node_type = "AppendPlantTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.PlantType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class AppendZombieTypeListNode(Node):
    node_type = "AppendZombieTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.ZombieType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class AppendObjectListNode(Node):
    node_type = "AppendObjectListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.GameObject),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }


# =============================================================================
# INSERT NODES
# =============================================================================

class InsertIntListNode(Node):
    node_type = "InsertIntListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class InsertFloatListNode(Node):
    node_type = "InsertFloatListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class InsertBoolListNode(Node):
    node_type = "InsertBoolListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Bool),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class InsertStringListNode(Node):
    node_type = "InsertStringListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.String),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class InsertPlantTypeListNode(Node):
    node_type = "InsertPlantTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.PlantType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class InsertZombieTypeListNode(Node):
    node_type = "InsertZombieTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.ZombieType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class InsertObjectListNode(Node):
    node_type = "InsertObjectListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.GameObject),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }


# =============================================================================
# REPLACE NODES
# =============================================================================

class ReplaceIntListNode(Node):
    node_type = "ReplaceIntListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class ReplaceFloatListNode(Node):
    node_type = "ReplaceFloatListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class ReplaceBoolListNode(Node):
    node_type = "ReplaceBoolListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.Bool),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class ReplaceStringListNode(Node):
    node_type = "ReplaceStringListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.String),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class ReplacePlantTypeListNode(Node):
    node_type = "ReplacePlantTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.PlantType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class ReplaceZombieTypeListNode(Node):
    node_type = "ReplaceZombieTypeListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.ZombieType),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class ReplaceObjectListNode(Node):
    node_type = "ReplaceObjectListNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Input, PortType.GameObject),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }


# =============================================================================
# GET ITEM NODES
# =============================================================================

class GetIntListItemNode(Node):
    node_type = "GetIntListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.Int),
    }

class GetFloatListItemNode(Node):
    node_type = "GetFloatListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.Float),
    }

class GetBoolListItemNode(Node):
    node_type = "GetBoolListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.Bool),
    }

class GetStringListItemNode(Node):
    node_type = "GetStringListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.String),
    }

class GetPlantTypeListItemNode(Node):
    node_type = "GetPlantTypeListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.PlantType),
    }

class GetZombieTypeListItemNode(Node):
    node_type = "GetZombieTypeListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.ZombieType),
    }

class GetObjectListItemNode(Node):
    node_type = "GetObjectListItemNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "值": PortDef("值", PortDirection.Output, PortType.GameObject),
    }


# =============================================================================
# FIND VALUE NODES
# =============================================================================

class FindIntListValueNode(Node):
    node_type = "FindIntListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Int),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

class FindFloatListValueNode(Node):
    node_type = "FindFloatListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Float),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

class FindBoolListValueNode(Node):
    node_type = "FindBoolListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.Bool),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

class FindStringListValueNode(Node):
    node_type = "FindStringListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.String),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

class FindPlantTypeListValueNode(Node):
    node_type = "FindPlantTypeListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.PlantType),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

class FindZombieTypeListValueNode(Node):
    node_type = "FindZombieTypeListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.ZombieType),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }

class FindObjectListValueNode(Node):
    node_type = "FindObjectListValueNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "值": PortDef("值", PortDirection.Input, PortType.GameObject),
        "索引": PortDef("索引", PortDirection.Output, PortType.Int),
        "存在": PortDef("存在", PortDirection.Output, PortType.Bool),
    }


# =============================================================================
# GENERAL LIST UTILITY NODES
# =============================================================================

class ClearListValuesNode(Node):
    node_type = "ClearListValuesNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class RemoveListItemNode(Node):
    node_type = "RemoveListItemNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "索引": PortDef("索引", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

class GetListLengthNode(Node):
    node_type = "GetListLengthNode"
    _class_ports = {
        "列表": PortDef("列表", PortDirection.Input, PortType.ListVariable),
        "长度": PortDef("长度", PortDirection.Output, PortType.Int),
    }

class CopyListValuesNode(Node):
    node_type = "CopyListValuesNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "源列表": PortDef("源列表", PortDirection.Input, PortType.ListVariable),
        "目标列表": PortDef("目标列表", PortDirection.Input, PortType.ListVariable),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }
