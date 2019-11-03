from pyengine2.Widgets.Widget import Widget
from pyengine2.Utils import Vec2

import pygame


class Image(Widget):
    def __init__(self, x, y, sprite, size=None):
        """
            Create Image

            :param x: X Pos
            :param y: Y Pos
            :param sprite: Path of image
            :param size: Size of image or None
        """
        super(Image, self).__init__(x, y)

        self.sprite = sprite
        self.size = size

        self.render = None
        self.old_render = None
        self.old_pos = None
        self.update_render()

    def update_render(self):
        """
            Update render of Image

            .. note:: You must use this method after any change in Image
        """
        self.render = pygame.image.load(self.sprite)
        if self.size is not None:
            self.render = pygame.transform.scale(self.render, self.size.coords())

    def show(self, screen):
        """
            Show Image to screen

            :param screen: Screen where widget must be showed
            :return: Rects must be updated

            .. note:: You may not use this method. UISystem make it for you
        """
        if self.showed:
            if self.old_render != self.render or self.old_pos != Vec2(self.x, self.y):
                if self.old_render is not None and self.old_pos is not None:
                    screen.fill(self.system.world.window.color.get_rgba(), self.old_render.get_rect(x=self.old_pos.x,
                                                                                                    y=self.old_pos.y))
                screen.blit(self.render, (self.x, self.y))
                self.old_render = self.render
                self.old_pos = Vec2(self.x, self.y)
                yield self.render.get_rect(x=self.x, y=self.y)
            else:
                screen.blit(self.render, (self.x, self.y))


