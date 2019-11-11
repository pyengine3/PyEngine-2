import pygame
from pyengine2.Components.Component import Component

from pyengine2.Utils import Vec2


class SpriteComponent(Component):
    def __init__(self, sprite, rotation=0, size=None, flipx=False, flipy=False):
        """
            Create SpriteComponent

            This Component is here to add sprite to entity
            Required Components : /

            :param sprite: Path to file of sprite
        """
        super(SpriteComponent, self).__init__()
        self.sprite = sprite
        self.image = pygame.image.load(sprite).convert()
        if size is None:
            size = Vec2(self.image.get_rect().width, self.image.get_rect().height)
        self.size = size
        self.rotation = rotation
        self.flipx = flipx
        self.flipy = flipy
        self.transformed_image = None
        self.old_sprite = sprite
        self.update_image()

    def update_image(self):
        """
            Update the transformed image of entity

            .. note:: You must use this method after any change of the component
        """
        if self.old_sprite != self.sprite:
            self.image = pygame.image.load(self.sprite).convert()
            self.old_sprite = self.sprite
        image = pygame.transform.flip(self.image, self.flipx, self.flipy)
        image = pygame.transform.scale(image, self.size.coords())
        image = pygame.transform.rotate(image, self.rotation)
        self.transformed_image = image
