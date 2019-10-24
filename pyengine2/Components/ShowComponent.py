from pyengine2.Components.Component import Component
from pyengine2.Components.SpriteComponent import SpriteComponent
from pyengine2.Components.PositionComponent import PositionComponent


class ShowComponent(Component):
    def __init__(self):
        """
            Create ShowComponent

            This Component is here to add showing of entity
        """
        super(ShowComponent, self).__init__()
        self.required_components.add(SpriteComponent)
        self.required_components.add(PositionComponent)

    def show(self, screen):
        """
            Show entity to screen

            :param screen: Screen where entity is showed

            .. note:: You may not use this method. EntitySystem make it for you
        """
        for i in self.entities:
            x, y = i.get_component(PositionComponent).get_position()
            image = i.get_component(SpriteComponent).image
            screen.blit(image, (x, y))
