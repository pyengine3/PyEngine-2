import pygame
pygame.init()

import pygame.locals as const

import os

from pyengine2.Utils import Color, Font, logger
from pyengine2.World import World
from pyengine2.WindowSystems import MusicSystem, SoundSystem
import logging


class Window:
    def __init__(self, width, height, color=Color.from_name("BLACK"), title="PyEngine 2", icon=None,
                 limit_fps=None, update_rate=60, centered=True, debug=False):
        """
            Create Window

            :param width: Width of Window
            :param height: Height of Window
            :param color: Color of background of Window
            :param title: Title of Window
            :param icon: Icon of Window (None if you have any icon)
            :param limit_fps: Max FPS of Window (None if you don't want limit)
            :param update_rate: Rate of World's update
            :param centered: True if you want centered window, else False
            :param debug: True if you want some debug infos, else False
        """
        self.update_rate = update_rate
        self.debug = debug
        self.old_debug = debug
        self.color = color
        self.width = width
        self.height = height
        self.limit_fps = limit_fps

        if icon is not None:
            pygame.display.set_icon(pygame.image.load(icon))

        if centered:
            os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((width, height))
        pygame.time.set_timer(const.USEREVENT, round(1000/update_rate))

        self.clock = pygame.time.Clock()
        self.is_running = False
        self.debug_font = Font(bold=True, color=Color.from_name("ORANGE"))
        self.world = World(self)
        self.old_world = None

        self.music_system = MusicSystem()
        self.sound_system = SoundSystem()

        self.callbacks = {"START": None, "STOP": None, "OUTOFWINDOW": None, "CHANGEWORLD": None}

        self.fps_timer = 30
        try:
            self.fps_label = self.debug_font.render("FPS : " + str(round(self.clock.get_fps())))
        except OverflowError:
            self.fps_label = self.debug_font.render("FPS : Infinity")
        self.old_fps = None

        if debug:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

    def set_callback(self, callback, function):
        """
            Set callback of Window

            :param callback: Callback to set
            :param function: Function which is triggered by the callback
        """
        if callback in self.callbacks.keys():
            self.callbacks[callback] = function
        else:
            logger.warning("The callback '{}' doesn't exist.", callback)

    def call(self, callback, *param):
        """
            Call a callback

            :param callback: Callback to call
            :param param: Parameters of callback

            .. note:: You may not use this method. Window and EntitySystem make it for you
        """
        if callback in self.callbacks.keys() and self.callbacks[callback] is not None:
            self.callbacks[callback](*param)

    def stop(self):
        """Stop Window"""
        self.is_running = False
        self.call("STOP")
        logger.debug("Stop Window")

    def run(self):
        """Run Window"""
        self.is_running = True
        self.call("START")
        logger.debug("Start Window")
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)

            if self.old_world != self.world:
                self.call("CHANGEWORLD", self.old_world, self.world)
                self.screen.fill(self.color.get_rgba())
                self.old_world = self.world

            if self.old_debug != self.debug:
                self.screen.fill(self.color.get_rgba())
                self.old_debug = self.debug

            rects = self.world.show(self.screen)

            if self.debug:
                rects_debug = self.world.show_debug(self.screen)
                if len(rects_debug):
                    rects += rects_debug
                if self.old_fps != self.fps_label and self.old_fps is not None:
                    self.screen.fill(self.color.get_rgba(), self.old_fps.get_rect(x=10, y=10))
                self.screen.blit(self.fps_label, (10, 10))

            if self.limit_fps is None:
                self.clock.tick()
            else:
                self.clock.tick(self.limit_fps)

            if self.debug and self.old_fps != self.fps_label:
                self.old_fps = self.fps_label
                rects.append(self.fps_label.get_rect(x=10, y=10))

            pygame.display.update(rects)

        pygame.quit()

    def process_event(self, evt):
        """
            Process event

            :param evt: Event to be processed

            .. note:: You may not use this method. Window make it for you.
        """
        if evt.type == const.QUIT:
            self.stop()
        elif evt.type == const.USEREVENT:
            self.world.update()
            if self.debug:
                self.fps_timer -= 1
                if self.fps_timer <= 0:
                    try:
                        self.fps_label = self.debug_font.render("FPS : " + str(round(self.clock.get_fps())))
                    except OverflowError:
                        self.fps_label = self.debug_font.render("FPS : Infinity")
                    self.fps_timer = 30
        elif evt.type == self.music_system.ENDSOUND:
            self.music_system.next_song()
        else:
            self.world.event(evt)
