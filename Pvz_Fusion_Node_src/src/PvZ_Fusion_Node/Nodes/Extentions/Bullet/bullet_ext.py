from __future__ import annotations
from typing import Any, Optional, Union
from ..extension_node import ExtensionNode
from ....Core.context import ctx, ExecutionPath
from ...Original.BulletManipulation.bullet_type_value_node import BulletTypeValueNode
from ...Original.BulletManipulation.shoot_event_bullet_node import ShootEventBulletNode
from ...Original.BulletManipulation.modify_event_bullet_node import ModifyEventBulletNode
from ...Original.ObjectOperation.make_vector3_node import MakeVector3Node
from ...Original.Node import to_port


class Bullet(ExtensionNode):
    """High-level visual scripting Extension class representing a game bullet."""

    def __init__(self, bullet_port: Any = None):
        self._bullet_port = bullet_port
        super().__init__(root_node=getattr(bullet_port, "node", None))

    @property
    def port(self) -> Any:
        return self._bullet_port

    def _get_primary_port(self) -> Any:
        return self._bullet_port

    @classmethod
    def create_type(cls, bullet_type: int) -> Any:
        """Returns a BulletType port reference for a numeric bullet type ID."""
        node = BulletTypeValueNode(bullet_type=bullet_type)
        return node.get_output(BulletTypeValueNode.BulletType_output_bullettype)

    @classmethod
    def shoot(
        cls,
        bullet_type: Any,
        position: Any = None,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0,
    ) -> Bullet:
        """Shoots a bullet of specified type at given coordinates or Vector3 port."""
        if position is None:
            v_node = MakeVector3Node(x=x, y=y, z=z)
            position = v_node.get_output(MakeVector3Node.Vector_output_vector3)

        if isinstance(bullet_type, int):
            bullet_type = cls.create_type(bullet_type)

        shoot_node = ShootEventBulletNode()
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, shoot_node.node_id, ShootEventBulletNode.Trigger_input_trigger)

        b_type_port = to_port(bullet_type) if not hasattr(bullet_type, "connect") else bullet_type
        if hasattr(b_type_port, "connect"):
            b_type_port.connect(shoot_node.get_input(ShootEventBulletNode.BulletType_input_bullettype))

        pos_port = to_port(position) if not hasattr(position, "connect") else position
        if hasattr(pos_port, "connect"):
            pos_port.connect(shoot_node.get_input(ShootEventBulletNode.Position_input_vector3))

        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(shoot_node.node_id, ShootEventBulletNode.Complete_output_trigger)

        return cls(shoot_node.get_output(ShootEventBulletNode.Bullet_output_bullet))

    def modify(self, value: Any, property_id: int = 0) -> Bullet:
        """Modifies a runtime property (e.g., speed, damage) of this bullet."""
        node = ModifyEventBulletNode(property_id=property_id)
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, node.node_id, ModifyEventBulletNode.Trigger_input_trigger)

        if self._bullet_port and hasattr(self._bullet_port, "connect"):
            self._bullet_port.connect(node.get_input(ModifyEventBulletNode.Bullet_input_bullet))

        val_port = to_port(value)
        if hasattr(val_port, "connect"):
            val_port.connect(node.get_input(ModifyEventBulletNode.Value_input_float))

        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(node.node_id, ModifyEventBulletNode.Complete_output_trigger)

        return self
