from pyengine2.Widgets.Widget import Widget
from pyengine2.Utils import Vec2

import pygame


class ProgressBar(Widget):
    def __init__(self, x, y, sprites=None, size=Vec2(150, 10), value=0):
        """
            Create ProgressBar

            :param x: X Pos
            :param y: Y Pos
            :param sprites: List of background and foreground or None
            :param size: Size of ProgressBar
            :param value: Percent of ProgressBar
        """
        super(ProgressBar, self).__init__(x, y)
        self.size = size
        self.sprites = sprites
        self.value = value
        self.update_render()

    def update_render(self):
        """
            Update render of Image

            .. note:: You must use this method after any change in ProgressBar
        """
        if self.sprites is None:
            self.render = pygame.Surface(self.size.coords(), pygame.SRCALPHA, 32).convert_alpha()
            self.render.fill((50, 50, 50))
            white = pygame.Surface((self.size.x - 2, self.size.y - 2), pygame.SRCALPHA, 32).convert_alpha()
            white.fill((255, 255, 255))
            self.render.blit(white, (1, 1))
            green = pygame.Surface((int((self.size.x - 4) * (self.value / 100)), self.size.y - 4),
                                   pygame.SRCALPHA, 32).convert_alpha()
            green.fill((0, 255, 0))
            self.render.blit(green, (2, 2))
        else:
            self.render = pygame.image.load(self.sprites[0]).convert()
            self.render = pygame.transform.scale(self.render, self.size.coords())
            barre = pygame.image.load(self.sprites[1]).convert()
            barre = pygame.transform.scale(barre, (int((self.size.x - 4) * (self.value / 100)), self.size.y - 4))
            self.render.blit(barre, (2, 2))
