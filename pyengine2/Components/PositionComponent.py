from pyengine2.Components.Component import Component


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

    def get_position(self):
        """
            Get Position of Component

            :return: Tuple with X and Y Positions
        """
        return self.x, self.y

    def set_position(self, x, y):
        """
            Set Position of Component

            :param x: X Position
            :param y: Y Position
        """
        self.x = x
        self.y = y