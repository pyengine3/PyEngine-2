from pyengine2.Components.Component import Component
from pyengine2.Components.SpriteComponent import SpriteComponent
from pyengine2.Components.PositionComponent import PositionComponent
from pyengine2.Components.TextComponent import TextComponent
from pyengine2.Components.ShapeComponent import ShapeComponent


class ShowComponent(Component):
    def __init__(self, use_sprite=True):
        """
            Create ShowComponent

            This Component is here to add complex showing of entity
            Required Components : PositionComponent, (SpriteComponent or TextComponent)
            Incompatible Component : ShapeComponent
        """
        super(ShowComponent, self).__init__()
        self.incompatible_components.add(ShapeComponent)
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
        rects = []
        pos = self.entity.get_component(PositionComponent).position()
        if self.use_sprite:
            image = self.entity.get_component(SpriteComponent).transformed_image
        else:
            image = self.entity.get_component(TextComponent).render
        if self.old_pos != pos or self.old_image != image:
            if self.old_pos is not None:
                rect = self.old_image.get_rect(x=self.old_pos.x, y=self.old_pos.y)
                rects.append(rect)
                screen.fill(self.entity.system.world.window.color.get_rgba(), rect)
            self.old_pos = pos
            self.old_image = image
            rects.append(image.get_rect(x=pos.x, y=pos.y))

        screen.blit(image, pos.coords())
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
