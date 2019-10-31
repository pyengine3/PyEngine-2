from pyengine2.Widgets.Widget import Widget
from pyengine2.Utils import Vec2, Font

import pygame
import pygame.locals as const


class Checkbox(Widget):
    def __init__(self, x, y, text, font=Font(), checked=False, scale=1):
        """
            Create checkbox

            :param x: X Pos
            :param y: Y Pos
            :param text: Text of Checkbox
            :param font: Font of Checkbox
            :param checked: True if checkbox is checked or False
            :param scale: Scale of checkbox
        """
        super(Checkbox, self).__init__(x, y)
        self.text = text
        self.font = font
        self.checked = checked
        self.scale = scale
        self.render = None
        self.old_render = None
        self.old_pos = None
        self.update_render()

    def update_render(self):
        """
            Update render of Checkbox

            .. note:: You must use this method after any change in Checkbox
        """
        self.render = pygame.Surface((20 * self.scale + 5 + self.font.rendered_size(self.text)[0], 20 * self.scale))
        gray = pygame.Surface((20 * self.scale, 20 * self.scale))
        gray.fill((50, 50, 50))
        white = pygame.Surface((16*self.scale, 16*self.scale))
        white.fill((255, 255, 255))
        gray.blit(white, (gray.get_width() / 2 - white.get_width() / 2,
                          gray.get_height() / 2 - white.get_height() / 2))

        if self.checked:
            black = pygame.Surface((14*self.scale, 14*self.scale))
            black.fill((0, 0, 0))
            gray.blit(black, (gray.get_width() / 2 - black.get_width() / 2,
                              gray.get_height() / 2 - black.get_height() / 2))

        self.render.blit(gray, (0, 0))
        self.render.blit(self.font.render(self.text), (20 * self.scale + 5,
                                                       20 * self.scale / 2 - self.font.rendered_size(self.text)[1] / 2))

    def show(self, screen):
        """
            Show Button to screen

            :param screen: Screen where widget must be showed
            :return: Rects must be updated

            .. note:: You may not use this method. UISystem make it for you
        """
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

    def event(self, evt):
        """
            Manage Event

            :param evt: Event triggered

            .. note:: You may not use this method. UISystem make it for you
        """
        if evt.type == const.MOUSEBUTTONDOWN:
            if evt.button == const.BUTTON_LEFT:
                if self.render.get_rect(x=self.x, y=self.y).collidepoint(evt.pos[0], evt.pos[1]):
                    self.checked = not self.checked
                    self.update_render()
