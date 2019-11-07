from pyengine2.Widgets.Widget import Widget
from pyengine2.Utils import Font, clamp, Color

import string
import pygame
pygame.scrap.init()
import pygame.locals as const


class Entry(Widget):
    otherkeys = {const.K_SPACE: [" ", " "]}

    def __init__(self, x, y, width=200, font=Font(color=Color.from_name("BLACK")),
                 accepted="éèàçù€ " + string.digits + string.ascii_letters + string.punctuation, image=None):
        """
            Create Entry

            :param x: X Pos
            :param y: Y Pos
            :param width: Width of Widget
            :param font: Font of Widget
            :param image: Background Image of Widget (or None)
        """
        super(Entry, self).__init__(x, y)
        self.width = width
        self.font = font
        self.image = image
        self.text = ""
        self.cursor = False
        self.focus = False
        self.cursortimer = 20
        self.accepted = accepted
        self.update_render()

    def update(self):
        """
            Update Entry

            .. note:: You may not use this method. UISystem make it for you
        """
        if self.showed and self.active and self.focus:
            if self.cursortimer <= 0:
                self.cursor = not self.cursor
                self.cursortimer = 20
                self.update_render()
            self.cursortimer -= 1

    def event(self, evt):
        """
            Manage Event

            :param evt: Event triggered

            .. note:: You may not use this method. UISystem make it for you
        """
        if self.showed and self.active:
            if evt.type == const.KEYDOWN and self.focus:
                self.keypress(evt.key, evt.mod)
            elif evt.type == const.MOUSEBUTTONDOWN and evt.button == const.BUTTON_LEFT:
                if self.render.get_rect(x=self.x, y=self.y).collidepoint(evt.pos[0], evt.pos[1]):
                    self.focus = True
                else:
                    self.focus = False
                    self.cursor = False
                    self.update_render()

    def keypress(self, key, mod):
        """
            Manage KEYDOWN Event

            :param evt: Event

            .. note:: You may not use this method. Entry make it for you
        """
        mod -= 4096
        if key == const.K_BACKSPACE:
            if len(self.text):
                self.text = self.text[:-1]
                self.update_render()
        elif key == const.K_v and (mod == const.KMOD_CTRL or mod == const.KMOD_LCTRL):
            clipboard = pygame.scrap.get(const.SCRAP_TEXT)
            if clipboard:
                self.text += clipboard.decode()[:-1]
                self.update_render()
        elif key == const.K_c and (mod == const.KMOD_CTRL or mod == const.KMOD_LCTRL):
            pygame.scrap.put(pygame.SCRAP_TEXT, self.text.encode())
        elif len(pygame.key.name(key)) == 1 or key in self.otherkeys.keys():
            if mod == const.KMOD_CAPS or mod == const.KMOD_LSHIFT or mod == const.KMOD_RSHIFT or \
                    mod == const.KMOD_SHIFT:
                if len(pygame.key.name(key)) == 1:
                    self.text += pygame.key.name(key).upper()
                else:
                    self.text += self.otherkeys[key][1]
            else:
                if len(pygame.key.name(key)) == 1:
                    self.text += pygame.key.name(key)
                else:
                    self.text += self.otherkeys[key][0]
            self.update_render()

    def update_render(self):
        """
            Update render of Entry

            .. note:: You must use this method after any change in Entry
        """
        if self.cursor:
            text = self.font.render(self.text+"I")
        else:
            text = self.font.render(self.text)

        x = clamp(self.width - text.get_rect().width - 10, maxi=10)

        if self.image:
            self.render = pygame.image.load(self.image).convert()
            self.render = pygame.transform.scale(self.image, (self.width, 35))
        else:
            self.render = pygame.Surface((self.width, 35), pygame.SRCALPHA, 32).convert_alpha()
            self.render.fill((50, 50, 50))
            white = pygame.Surface((self.width - 8, 35))
            white.fill((255, 255, 255))
            self.render.blit(white, (4, 4))
        if len(self.text) or self.cursor:
            self.render.blit(text, (x, self.render.get_rect().height / 2 - text.get_rect().height / 2))
