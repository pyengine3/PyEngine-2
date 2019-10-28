from pyengine2.Components.Component import Component

from pyengine2.Utils import Vec2


class PositionComponent(Component):
    def __init__(self, x, y):
        """
            Create PositionComponent

            This Component is here to add position to entity

            :param x: Position X
            :param y: Position Y
        """
        super(PositionComponent, self).__init__()
        self.x = x
        self.y = y

    def position(self):
        """
            Get Position of Component

            :return: Vec2 of Position
        """
        return Vec2(self.x, self.y)

    def set_position(self, x, y):
        """
            Set Position of Component

            :param x: X Position
            :param y: Y Position
        """
        self.x = x
        self.y = y
