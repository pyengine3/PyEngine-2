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


