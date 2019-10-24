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
        self.old_pos = None

    def show(self, screen):
        """
            Show entity to screen

            :param screen: Screen where entity is showed
            :return: Rects must be updated

            .. note:: You may not use this method. EntitySystem make it for you
        """
        dirty_rects = []
        for i in self.entities:
            x, y = i.get_component(PositionComponent).get_position()
            image = i.get_component(SpriteComponent).image
            if self.old_pos is None or self.old_pos != (x, y):
                self.old_pos = (x, y)
                screen.blit(image, (x, y))
                dirty_rects.append(image.get_rect(x=x, y=y))
        return dirty_rects
