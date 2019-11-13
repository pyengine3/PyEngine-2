from pyengine2.Widgets.Widget import Widget
from pyengine2.Utils import Font

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

        self.render_btn = None
        self.update_render()

    def update_render(self):
        """
            Update render of Checkbox

            .. note:: You must use this method after any change of Checkbox
        """
        self.render_btn = pygame.Surface((20 * self.scale, 20 * self.scale))
        self.render_btn.fill((50, 50, 50))
        white = pygame.Surface((16*self.scale, 16*self.scale))
        white.fill((255, 255, 255))
        self.render_btn.blit(white, (self.render_btn.get_width() / 2 - white.get_width() / 2,
                                     self.render_btn.get_height() / 2 - white.get_height() / 2))

        if self.checked:
            black = pygame.Surface((14*self.scale, 14*self.scale))
            black.fill((0, 0, 0))
            self.render_btn.blit(black, (self.render_btn.get_width() / 2 - black.get_width() / 2,
                                         self.render_btn.get_height() / 2 - black.get_height() / 2))

        render_label = self.font.render(self.text)

        self.render = pygame.Surface((20 * self.scale + 5 + render_label.get_width(), 20 * self.scale),
                                     pygame.SRCALPHA, 32).convert_alpha()
        self.render.blit(self.render_btn, (0, 0))
        self.render.blit(render_label, (20 * self.scale + 5, 20 * self.scale / 2 - render_label.get_height() / 2))

    def event(self, evt):
        """
            Manage Event

            :param evt: Event triggered

            .. note:: You may not use this method. UISystem make it for you
        """
        if self.showed and self.active and evt.type == const.MOUSEBUTTONDOWN and evt.button == const.BUTTON_LEFT:
            if self.render_btn.get_rect(x=self.x, y=self.y).collidepoint(evt.pos[0], evt.pos[1]):
                self.checked = not self.checked
                self.update_render()
