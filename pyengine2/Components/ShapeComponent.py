from pyengine2.Components.Component import Component
from pyengine2.Components.PositionComponent import PositionComponent


class ShapeComponent(Component):
    def __init__(self, shape):
        """
            Create ShapeComponent

            This Component is here to add shape showing of entity
            Required Components : PositionComponent
            Incompatible Component : ShowComponent
        """
        super(ShapeComponent, self).__init__()

        from pyengine2.Components.ShowComponent import ShowComponent  # Avoid circular import

        self.incompatible_components.add(ShowComponent)
        self.required_components.add(PositionComponent)
        self.shape = shape
        self.old_debug_pos = None
        self.old_shape = None

    def show(self, screen):
        """
            Show entity to screen

            :param screen: Screen where entity is showed
            :return: Rects must be updated

            .. note:: You may not use this method. EntitySystem make it for you
        """
        rects = []
        pos = self.entity.get_component(PositionComponent).position()
        shape = self.shape.show(pos.x, pos.y, screen)
        if self.old_shape != shape:
            if self.old_shape is not None:
                rects.append(self.old_shape)
                screen.fill(self.entity.system.world.window.color.get_rgba(), self.old_shape)
                self.shape.show(pos.x, pos.y, screen)
            self.old_shape = shape
            rects.append(shape)
        return rects

    def show_debug(self, screen):
        """
            Show debug entity to screen

            :param screen: Screen where entity is showed
            :return: Rects must be updated

            .. note:: You may not use this method. EntitySystem make it for you
        """
        rects = []
        pos = self.entity.get_component(PositionComponent).position()
        image = self.entity.system.debug_font.render("ID : "+str(self.entity.identity))
        if self.old_debug_pos != pos:
            if self.old_debug_pos is not None:
                rect = image.get_rect(x=self.old_debug_pos.x, y=self.old_debug_pos.y - 20)
                rects.append(rect)
                screen.fill(self.entity.system.world.window.color.get_rgba(), rect)
            self.old_debug_pos = pos
            rects.append(image.get_rect(x=pos.x, y=pos.y-20))

        screen.blit(image, (pos.x, pos.y - 20))
        return rects
