from pyengine2.Components.Component import Component
from pyengine2.Components.SpriteComponent import SpriteComponent

from pyengine2.Utils.Logger import logger

import pygame


class AnimComponent(Component):
    def __init__(self, time=20):
        """
            Create AnimComponent

            :param time: Time between two sprites
        """
        super(AnimComponent, self).__init__()
        self.required_components.add(SpriteComponent)
        self.anims = dict()
        self.time = time
        self.timer = 0
        self.current_sprite = 0
        self.playing = None

    def add_anim_list(self, name, *sprites):
        """
            Add animation with a list of sprites

            :param name: Name of Animation
            :param sprites: List of sprites
        """
        if name in self.anims.keys():
            logger.warning("Animation overrided : "+name)

        self.anims[name] = tuple(pygame.image.load(i).convert() for i in sprites)

    def add_anim_sheet(self, name, sheet, tile_x=1, tile_y=1):
        """
            Add animation with a spritesheet

            :param name: Name of animation
            :param sheet: Path of spritesheet
            :param tile_x: Number of sprite in X Pos
            :param tile_y: Number of sprite in Y Pos
        """
        if name in self.anims.keys():
            logger.warning("Animation overrided : "+name)

        sheet_image = pygame.image.load(sheet).convert()
        x_diff = sheet_image.get_rect().width // tile_x
        y_diff = sheet_image.get_rect().height // tile_y
        self.anims[name] = []
        for x in range(tile_x):
            for y in range(tile_y):
                self.anims[name].append(sheet_image.subsurface(pygame.Rect(x * x_diff, y * y_diff, x_diff, y_diff)))

    def play(self, name):
        """
            Play an animation

            :param name: Name of animation
        """
        if self.playing == name:
            logger.warning("Animation already play")
        else:
            self.playing = name
            self.timer = 0
            self.current_sprite = 0

    def stop(self):
        """
            Stop animations
        """
        self.playing = None

    def update(self):
        """
            Update AnimComponent

            .. note:: You may not this method. Entity make it for you
        """
        if self.playing:
            if self.timer <= 0:
                if self.current_sprite + 1 == len(self.anims[self.playing]):
                    self.current_sprite = 0
                else:
                    self.current_sprite += 1
                self.entity.get_component(SpriteComponent).image = self.anims[self.playing][self.current_sprite]
                self.entity.get_component(SpriteComponent).update_image()
                self.timer = self.time

            self.timer -= 1
