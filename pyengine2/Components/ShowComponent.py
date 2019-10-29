from pyengine2.Components.Component import Component
from pyengine2.Components.SpriteComponent import SpriteComponent
from pyengine2.Components.PositionComponent import PositionComponent
from pyengine2.Components.TextComponent import TextComponent


class ShowComponent(Component):
    def __init__(self, use_sprite=True):
        """
            Create ShowComponent

            This Component is here to add showing of entity
        """
        super(ShowComponent, self).__init__()
        self.required_components.add(PositionComponent)
        if use_sprite:
            self.required_components.add(SpriteComponent)
        else:
            self.required_components.add(TextComponent)
        self.use_sprite = use_sprite
        self.old_pos = None
        self.old_debug_pos = None
        self.old_image = None

    def show(self, screen):
        """
            Show entity to screen

            :param screen: Screen where entity is showed
            :return: Rects must be updated

            .. note:: You may not use this method. EntitySystem make it for you
        """
        pos = self.entity.get_component(PositionComponent).position()
        if self.use_sprite:
            image = self.entity.get_component(SpriteComponent).transformed_image
        else:
            image = self.entity.get_component(TextComponent).render
        if self.old_pos != pos or self.old_image != image:
            if self.old_pos is not None and self.old_image is not None:
                dirty_rect = self.old_image.get_rect(x=self.old_pos.x, y=self.old_pos.y)
                screen.fill(self.entity.system.world.window.color.get_rgba(), dirty_rect)
            else:
                dirty_rect = None
            self.old_pos = pos
            self.old_image = image
            image_rect = True
        else:
            dirty_rect = None
            image_rect = False

        screen.blit(image, pos.coords())

        if dirty_rect:
            yield dirty_rect
        if image_rect:
            yield image.get_rect(x=pos.x, y=pos.y)

    def show_debug(self, screen):
        """
            Show debug entity to screen

            :param screen: Screen where entity is showed
            :return: Rects must be updated

            .. note:: You may not use this method. EntitySystem make it for you
        """
        pos = self.entity.get_component(PositionComponent).position()
        image = self.entity.system.world.window.debug_font.render("ID : "+str(self.entity.identity))
        if self.old_debug_pos is None or self.old_debug_pos != pos:
            if self.old_debug_pos is not None:
                dirty_rect = image.get_rect(x=self.old_debug_pos.x, y=self.old_debug_pos.y - 20)
                screen.fill(self.entity.system.world.window.color.get_rgba(), dirty_rect)
            else:
                dirty_rect = None
            self.old_debug_pos = pos
            image_rect = True
        else:
            dirty_rect = None
            image_rect = False

        screen.blit(image, (pos.x, pos.y - 20))

        if dirty_rect:
            yield dirty_rect
        if image_rect:
            yield image.get_rect(x=pos.x, y=pos.y-20)

