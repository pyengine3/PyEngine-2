from pyengine2.Components.Component import Component
from pyengine2.Components.PositionComponent import PositionComponent
from pyengine2.Components.SpriteComponent import SpriteComponent
from pyengine2.Components.CollisionComponent import CollisionComponent

from pyengine2.Utils import Vec2


class AutoComponent(Component):
    def __init__(self, movement=Vec2.zero(), rotation=0):
        """
            Create AutoComponent

            This Component is here to add auto movement (direction, rotation) to entity
            Required Components : If movement != Vec2.zero() PositionComponent
                                  If rotation != 0 SpriteComponent

            :param movement: Vector of Automatic Movement
            :param rotation: Number of Automatic Rotation
        """
        super(AutoComponent, self).__init__()
        self.movement = movement
        self.rotation = rotation

        if self.movement != Vec2.zero():
            self.required_components.add(PositionComponent)
        if self.rotation != 0:
            self.required_components.add(SpriteComponent)

    def update(self):
        """
            Update values

            .. note:: You may not use this method. Entity make it for you
        """
        if self.movement != Vec2.zero():
            pos = self.entity.get_component(PositionComponent).position()
            pos.x += self.movement.x
            pos.y += self.movement.y

            if self.entity.has_component(CollisionComponent):
                if self.entity.get_component(CollisionComponent).can_go(pos.x, pos.y, "AUTOCOMPONENT"):
                    self.entity.get_component(PositionComponent).set_position(pos.x, pos.y)
            else:
                self.entity.get_component(PositionComponent).set_position(pos.x, pos.y)

        if self.rotation != 0:
            self.entity.get_component(SpriteComponent).rotation += self.rotation
            self.entity.get_component(SpriteComponent).update_image()

