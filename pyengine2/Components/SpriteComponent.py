import pygame
from pyengine2.Components.Component import Component


class SpriteComponent(Component):
    def __init__(self, sprite):
        """
            Create SpriteComponent

            This Component is here to add sprite to entity

            :param sprite: Path to file of sprite
        """
        super(SpriteComponent, self).__init__()
        self.sprite = sprite
        self.image = pygame.image.load(sprite)
