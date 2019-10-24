from pyengine2.Components.ShowComponent import ShowComponent
from pyengine2.Utils import logger


class EntitySystem:
    def __init__(self, world):
        """
            Constructor of EntitySystem

            :param world: World of EntitySystem

            .. note:: You may not use this constructor. EntitySystem is already create in World
        """
        self.world = world
        self.entities = set()

    def add_entity(self, entity):
        """
            Add an entity in EntitySystem

            :param entity: Entity to be added
        """
        if entity in self.entities:
            logger.warning("Entity already in EntitySystem")
        else:
            self.entities.add(entity)

    def remove_entity(self, entity):
        """
            Remove an entity from EntitySystem

            :param entity: Entity to remove
        """
        if entity in self.entities:
            self.entities.remove(entity)
        else:
            logger.warning("Entity is not in EntitySystem")

    def has_entity(self, entity):
        """
            Verify if EntitySystem have an entity

            :param entity: Entity
            :return: True if entity is in EntitySystem else False
        """
        return entity in self.entities

    def show(self, screen):
        """
            Show world in screen

            :param screen: Screen where world is showed

            .. note:: You may not use this method. World it this for you.
        """
        for entity in self.entities:
            if entity.has_component(ShowComponent):
                entity.get_component(ShowComponent).show(screen)
