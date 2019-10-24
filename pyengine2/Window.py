import pygame
pygame.init()

import pygame.locals as const

import os

from pyengine2.Utils.Color import Color


class Window:
    def __init__(self, width, height, color=Color.from_name("black"), title="PyEngine 2", icon=None,
                 limit_fps=None, update_rate=60, centered=True, debug=False):
        self.update_rate = update_rate
        self.debug = debug
        self.color = color
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

        self.fps_timer = 30

    def stop(self):
        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.__process_event(event)

            self.screen.fill(self.color.get_rgba())

            if self.limit_fps is None:
                self.clock.tick()
            else:
                self.clock.tick(self.limit_fps)

            pygame.display.update()
        pygame.quit()

    def __process_event(self, evt):
        if evt.type == const.QUIT:
            self.stop()
        elif evt.type == const.USEREVENT:
            if self.debug:
                self.fps_timer -= 1
                if self.fps_timer <= 0:
                    try:
                        print("FPS :", round(self.clock.get_fps()))
                    except OverflowError:
                        print("FPS : Infinity")
                    self.fps_timer = 30
