from pyengine2.Components.Component import Component
from pyengine2.Components.SpriteComponent import SpriteComponent

import pygame


class AnimComponent(Component):
    def __init__(self, time, *images):
        """
            Create AnimComponent

            This Component is here to create animation for entity
            Required Components : SpriteComponent

            :param time: Time in number of update between changement of sprite
            :param images: Path to sprites
        """
        super(AnimComponent, self).__init__()

        self.required_components.add(SpriteComponent)
        self.images = images
        self.time = time
        self.timer = 0
        self.current_sprite = 0
        self.play = True

    @property
    def images(self):
        """
            Get path of sprites

            :return: List of paths of sprites
        """
        return self.__images

    @images.setter
    def images(self, images):
        """
            Set paths of sprites

            :param images: List of path of sprites
        """
        self.__images = images
        self.sprites = [pygame.image.load(image).convert() for image in images]
        self.timer = 0

    def update(self):
        """
            Update AnimComponent

            .. note:: You may not this method. Entity make it for you
        """
        if self.play:
            if self.timer <= 0:
                if self.current_sprite + 1 == len(self.images):
                    self.current_sprite = 0
                else:
                    self.current_sprite += 1
                self.entity.get_component(SpriteComponent).image = self.sprites[self.current_sprite]
                self.entity.get_component(SpriteComponent).update_image()
                self.timer = self.time

            self.timer -= 1


