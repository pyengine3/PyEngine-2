from pyengine2.Components.Component import Component
from pyengine2.Components.SpriteComponent import SpriteComponent
from pyengine2.Components.PositionComponent import PositionComponent


class CollisionComponent(Component):
    def __init__(self, callback=None, solid=True):
        """
            Create CollisionComponent

            :param callback: Function will be trigger when there is collision
            :param solid: True if Entity is solid or not
        """
        super(CollisionComponent, self).__init__()
        self.required_components.add(PositionComponent)
        self.required_components.add(SpriteComponent)
        self.solid = solid
        self.callback = callback

    def can_go(self, x, y):
        """
            Know if Entity can go to x, y position

            :param x: X Pos
            :param y: Y Pos
        """
        rect = self.entity.get_component(SpriteComponent).transformed_image.get_rect(x=x, y=y)
        for entity in self.entity.system.entities:
            if entity.has_component(SpriteComponent) and entity.has_component(PositionComponent) and \
                    entity.has_component(CollisionComponent) and entity != self.entity:
                pos = entity.get_component(PositionComponent).position()
                other_rect = entity.get_component(SpriteComponent).transformed_image.get_rect(x=pos.x, y=pos.y)
                if rect.colliderect(other_rect):
                    if entity.get_component(CollisionComponent).solid and self.solid:
                        return False
                    self.callback(entity)
        return True
