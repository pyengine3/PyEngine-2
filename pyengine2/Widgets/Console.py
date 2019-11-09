from pyengine2.Widgets.Widget import Widget

from pyengine2.Utils import Font, logger, Color

import pygame
import pygame.locals as const
import string


def print_command(console, window, args):
    console.set_return(" ".join(args))


def debug_command(console, window, args):
    if window.debug:
        console.set_return("Debug desactivated")
    else:
        console.set_return("Debug activated")
    window.debug = not window.debug


class Console(Widget):
    def __init__(self, x, y, window, width=None):
        """
            Create Console

            :param x: X Pos
            :param y: Y Pos
            :param window: Window of Program
            :param width: Width of Console or None if Width is width of window
        """
        super(Console, self).__init__(x, y)
        if width is None:
            width = window.width
        self.window = window
        self.width = width

        self.return_text = ""
        self.send_text = ""
        self.cursor = False
        self.focus = False
        self.cursortimer = 20
        self.accepted = "éèàçù€ " + string.digits + string.ascii_letters + string.punctuation
        self.render_entry = None

        self.commands = {}
        self.lastcommands = []
        self.current_command = 0

        self.font = Font(size=18, background=Color.from_name("WHITE"), color=Color.from_name("BLACK"))

        self.add_command("print", print_command)
        self.add_command("debug", debug_command)

        self.update_render()

    def update_render(self):
        """
            Update render of Console

            .. note:: You must use this method after any change in Console
        """
        font_render = self.font.render(self.return_text)
        self.render = pygame.Surface((self.width, 36+font_render.get_rect().height),
                                     pygame.SRCALPHA, 32).convert_alpha()
        self.render.blit(font_render, (4, 0))
        self.render_entry = pygame.Surface((self.width, 35), pygame.SRCALPHA, 32).convert_alpha()
        self.render_entry.fill((50, 50, 50))
        white = pygame.Surface((self.width - 8, 27))
        white.fill((255, 255, 255))
        self.render_entry.blit(white, (4, 4))
        if len(self.send_text) or self.cursor:
            if self.cursor:
                text = self.font.render(self.send_text+"I")
            else:
                text = self.font.render(self.send_text)
            self.render_entry.blit(text, (5, self.render_entry.get_rect().height / 2 - text.get_rect().height / 2))
        self.render.blit(self.render_entry, (0, font_render.get_rect().height + 1))

    def update(self):
        """
            Update Console

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
            elif evt.type == const.TEXTINPUT and self.focus:
                if evt.text in self.accepted:
                    self.send_text += evt.text
                    self.update_render()
            elif evt.type == const.MOUSEBUTTONDOWN and evt.button == const.BUTTON_LEFT:
                font_render = self.font.render(self.return_text)
                if self.render_entry.get_rect(
                        x=self.x, y=self.y+font_render.get_rect().height + 1).collidepoint(evt.pos[0], evt.pos[1]):
                    self.focus = True
                else:
                    self.focus = False
                    self.cursor = False
                    self.update_render()

    def keypress(self, key, mod):
        """
            Manage KEYDOWN Event

            :param key: Key Pressed
            :param mod: Modifier of Key

            .. note:: You may not use this method. Entry make it for you
        """
        mod -= 4096
        if key == const.K_BACKSPACE:
            if len(self.send_text):
                self.send_text = self.send_text[:-1]
                self.update_render()
        elif key == const.K_RETURN:
            self.lastcommands.append(self.send_text)
            self.current_command = len(self.lastcommands)
            self.execute_command(self.send_text)
            self.send_text = ""
        elif key == const.K_UP:
            if self.current_command > 0:
                self.current_command -= 1
                self.send_text = self.lastcommands[self.current_command]
                self.update_render()
        elif key == const.K_DOWN:
            if self.current_command < len(self.lastcommands) - 1:
                self.current_command += 1
                self.send_text = self.lastcommands[self.current_command]
                self.update_render()
            elif self.current_command < len(self.lastcommands):
                self.send_text = ""
                self.current_command += 1
                self.update_render()

    def set_return(self, text):
        """
            Set Return of Console

            :param text: Text to be in Return
        """
        self.return_text = "> " + text

    def add_command(self, command, function):
        """
            Add command to Console

            :param command: Command
            :param function: Function triggered when command is call
        """
        if command in self.commands.keys():
            logger.warning("Command overrided : "+command)
        self.commands[command] = function

    def delete_command(self, command):
        """
            Remove command from Console

            :param command: Command
        """
        try:
            del self.commands[command]
        except KeyError:
            logger.warning("Command '" + command + "' doesn't exist")

    def execute_command(self, command):
        """
            Execute command of Console

            :param command: Console to execute

            .. note:: You may not use this method. Console make it for you.
        """
        if len(command.split(" ")) > 1:
            args = command.split(" ")[1:]
        else:
            args = []
        command = command.split(" ")[0]
        if command in self.commands:
            self.commands[command](self, self.window, args)
        else:
            logger.warning("Unknown command : " + command)

