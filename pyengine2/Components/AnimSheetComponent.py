from pyengine2.Components.Component import Component
from pyengine2.Components.SpriteComponent import SpriteComponent

import pygame


class AnimSheetComponent(Component):
    def __init__(self, sheet, tile_x=1, tile_y=1, time=30):
        """
            Create AnimSheetComponent

            This Component is here to create animation for entity
            Required Components : SpriteComponent

            :param sheet: Path to spritesheet
            :param tile_x: Number of sprite in x coord
            :param tile_y: Number of sprite in y coord
            :param time: Time in number of update between changement of sprite
        """
        super(AnimSheetComponent, self).__init__()

        self.required_components.add(SpriteComponent)
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.sheet = sheet
        self.time = time
        self.timer = 0
        self.current_sprite = 0
        self.play = True

    @property
    def sheet(self):
        """
            Get path of spritesheet

            :return: Paths of spritesheet
        """
        return self.__sheet

    @sheet.setter
    def sheet(self, sheet):
        """
            Set paths of spritesheet

            :param images: Path of spritesheet
        """
        self.__sheet = sheet
        sheet_image = pygame.image.load(sheet).convert()
        x_diff = sheet_image.get_rect().width // self.tile_x
        y_diff = sheet_image.get_rect().height // self.tile_y
        self.sprites = []
        for x in range(self.tile_x):
            for y in range(self.tile_y):
                self.sprites.append(sheet_image.subsurface(pygame.Rect(x*x_diff, y*y_diff, x_diff, y_diff)))

        self.timer = 0

    def update(self):
        """
            Update AnimComponent

            .. note:: You may not this method. Entity make it for you
        """
        if self.play:
            if self.timer <= 0:
                if self.current_sprite + 1 == len(self.sprites):
                    self.current_sprite = 0
                else:
                    self.current_sprite += 1
                self.entity.get_component(SpriteComponent).image = self.sprites[self.current_sprite]
                self.entity.get_component(SpriteComponent).update_image()
                self.timer = self.time

            self.timer -= 1


