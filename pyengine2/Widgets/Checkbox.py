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

        self.render_btn = None
        self.render_label = None
        self.old_render_btn = None
        self.old_render_label = None
        self.old_pos = None
        self.update_render_btn()
        self.update_render_label()

    def update_render_btn(self):
        """
            Update render of button of Checkbox

            .. note:: You must use this method after any change of "x", "y", "checked" or "scale"
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

    def update_render_label(self):
        """
            Update render of button of Checkbox

            .. note:: You must use this method after any change of "x", "y", "font" or "text"
        """
        self.render_label = self.font.render(self.text)

    def show(self, screen):
        """
            Show Button to screen

            :param screen: Screen where widget must be showed
            :return: Rects must be updated

            .. note:: You may not use this method. UISystem make it for you
        """
        if self.showed:
            pos = Vec2(self.x, self.y)
            if self.old_render_btn != self.render_btn or self.old_pos != pos or self.old_render_label != self.render_label:
                if self.old_render_btn != self.render_btn or self.old_pos != pos:
                    if self.old_render_btn is not None:
                        screen.fill(self.system.world.window.color.get_rgba(), self.old_render_btn.get_rect(x=self.old_pos.x,
                                                                                                            y=self.old_pos.y))
                    screen.blit(self.render_btn, (self.x, self.y))
                    self.old_render_btn = self.render_btn
                    self.old_pos = Vec2(self.x, self.y)
                    yield self.render_btn.get_rect(x=self.x, y=self.y)
                if self.old_render_label != self.render_label or self.old_pos != pos:
                    if self.old_render_label is not None:
                        screen.fill(
                            self.system.world.window.color.get_rgba(),
                            self.old_render_label.get_rect(x=self.old_pos.x + 20*self.scale + 5,
                                                           y=self.y + 20*self.scale / 2 - self.render_label.get_height() / 2))
                    screen.blit(self.render_label, (self.x + 20*self.scale + 5,
                                                    self.y + 20*self.scale / 2 - self.render_label.get_height() / 2))
                    self.old_render_label = self.render_label
                    yield self.render_label.get_rect(x=self.x + 20*self.scale + 5,
                                                     y=self.y + 20*self.scale / 2 - self.render_label.get_height() / 2)
            else:
                screen.blit(self.render_btn, (self.x, self.y))
                screen.blit(self.render_label, (self.x + 20*self.scale + 5,
                                                self.y + 20*self.scale / 2 - self.render_label.get_height() / 2))

    def event(self, evt):
        """
            Manage Event

            :param evt: Event triggered

            .. note:: You may not use this method. UISystem make it for you
        """
        if self.showed and evt.type == const.MOUSEBUTTONDOWN and evt.button == const.BUTTON_LEFT:
            if self.render_btn.get_rect(x=self.x, y=self.y).collidepoint(evt.pos[0], evt.pos[1]):
                self.checked = not self.checked
                self.update_render_btn()
