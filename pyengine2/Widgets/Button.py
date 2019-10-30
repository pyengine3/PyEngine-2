from pyengine2.Widgets.Widget import Widget
from pyengine2.Utils import Font, Color, Vec2, clamp

import pygame
import pygame.locals as const


class Button(Widget):
    def __init__(self, x, y, text, command, font=Font(), size=Vec2(100, 40),
                 background=Color.from_name("GRAY").darker(5)):
        """
            Create Button

            :param x: X Pos
            :param y: Y Pos
            :param text: Text of Button
            :param command: Function triggered when button is clicked
            :param font: Font of Button
            :param size: Size of Button
            :param background: Path of background image or Color
        """
        super(Button, self).__init__(x, y)
        self.text = text
        self.command = command
        self.font = font
        self.background = background
        self.size = size
        self.ishover = False
        self.render = None
        self.old_render = None
        self.old_pos = None
        self.update_render()

    def update_render(self):
        """
            Update render of Button

            .. note:: You must use this method after any change in Button
        """
        if isinstance(self.background, Color):
            self.render = pygame.Surface(self.size.coords())
            self.render.fill(self.background.get_rgba())
        else:
            self.render = pygame.image.load(self.background)
            self.render = pygame.transform.scale(self.render, self.size.coords())

        text_render = self.font.render(self.text)
        x = self.size.x - self.render.get_rect().width / 2 - text_render.get_rect().width / 2
        y = self.size.y - self.render.get_rect().height / 2 - text_render.get_rect().height / 2
        self.render.blit(text_render, (x, y))

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
                    self.command()
        elif evt.type == const.MOUSEMOTION:
            if self.render.get_rect(x=self.x, y=self.y).collidepoint(evt.pos[0], evt.pos[1]):
                if not self.ishover:
                    t = pygame.surfarray.array3d(self.render)
                    for l in range(len(t)):
                        for c in range(len(t[l])):
                            for p in range(3):
                                t[l, c, p] = clamp(t[l, c, p]+20, 0, 255)
                    try:
                        pygame.surfarray.blit_array(self.render, t)
                    except ValueError:
                        pass
                    self.ishover = True
            elif self.ishover:
                t = pygame.surfarray.array3d(self.render)
                for l in range(len(t)):
                    for c in range(len(t[l])):
                        for p in range(3):
                            t[l, c, p] = clamp(t[l, c, p]-20, 0, 255)
                try:
                    pygame.surfarray.blit_array(self.render, t)
                except ValueError:
                    pass
                self.ishover = False




