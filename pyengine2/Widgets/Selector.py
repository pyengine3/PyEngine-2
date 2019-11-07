from pyengine2.Widgets.Widget import Widget
from pyengine2.Utils import Color, Font, clamp

import pygame
import pygame.locals as const


class Selector(Widget):
    def __init__(self, x, y, *texts):
        """
            Create Selector

            :param x: X Pos
            :param y: Y Pos
            :param texts: Texts which are to select

            .. warning:: You must give one text minimum.
        """
        super(Selector, self).__init__(x, y)
        self.texts = texts
        self.current = 0
        self.render_pred = None
        self.render_next = None
        self.max_size_text = None
        self.font = Font()
        self.update_max_size()
        self.update_render()

    def update_render(self):
        """
            Update render of Selector

            .. note:: You must use this method after any change of Selector
        """
        self.render_pred = pygame.Surface((25, 25), pygame.SRCALPHA, 32).convert_alpha()
        self.render_pred.fill(Color.from_name("GRAY").darker(5).get_rgba())
        text_render = self.font.render("<")
        x = 25 / 2 - text_render.get_rect().width / 2
        y = 25 / 2 - text_render.get_rect().height / 2
        self.render_pred.blit(text_render, (x, y))

        self.render_next = pygame.Surface((25, 25), pygame.SRCALPHA, 32).convert_alpha()
        self.render_next.fill(Color.from_name("GRAY").darker(5).get_rgba())
        text_render = self.font.render(">")
        x = 25 / 2 - text_render.get_rect().width / 2
        y = 25 / 2 - text_render.get_rect().height / 2
        self.render_next.blit(text_render, (x, y))

        text_render = self.font.render(self.texts[self.current])

        self.render = pygame.Surface((25 + 5 + self.max_size_text + 5 + 25, 25), pygame.SRCALPHA, 32).convert_alpha()
        self.render.blit(self.render_pred, (0, 0))
        self.render.blit(text_render, (25 + 5 + self.max_size_text / 2 - text_render.get_rect().width / 2,
                                       25 / 2 - text_render.get_rect().height / 2))
        self.render.blit(self.render_next, (25 + 5 + self.max_size_text + 5, 0))

    def update_max_size(self):
        """
            Update maxi_size_text of Selector

            .. note:: You must use this method after change list of texts in Selector
        """
        maxi = 0
        for i in self.texts:
            maxi = clamp(maxi, self.font.rendered_size(i)[0])
        self.max_size_text = maxi

    def event(self, evt):
        """
            Manage Event

            :param evt: Event triggered

            .. note:: You may not use this method. UISystem make it for you
        """
        if self.showed and self.active and evt.type == const.MOUSEBUTTONDOWN and evt.button == const.BUTTON_LEFT:
            if self.render_pred.get_rect(x=self.x, y=self.y).collidepoint(evt.pos[0], evt.pos[1]):
                if self.current == 0:
                    self.current = len(self.texts) - 1
                else:
                    self.current -= 1
                self.update_render()
            elif self.render_next.get_rect(x=self.x+40+self.max_size_text,
                                           y=self.y).collidepoint(evt.pos[0], evt.pos[1]):
                if self.current == len(self.texts) - 1:
                    self.current = 0
                else:
                    self.current += 1
                self.update_render()



