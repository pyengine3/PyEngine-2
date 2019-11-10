from pyengine2.Components.ShowComponent import ShowComponent
from pyengine2.Components.PositionComponent import PositionComponent
from pyengine2.Components.SpriteComponent import SpriteComponent
from pyengine2.Components.TextComponent import TextComponent
from pyengine2.Components.ShapeComponent import ShapeComponent
from pyengine2.Utils import logger, Font, Color


class EntitySystem:
    def __init__(self, world):
        """
            Constructor of EntitySystem

            :param world: World of EntitySystem

            .. note:: You may not use this constructor. EntitySystem is already create in World
        """
        self.world = world
        self.entities = []
        self.debug_font = Font(bold=True, color=Color.from_name("BLUE"))

    def add_entity(self, entity):
        """
            Add an entity in EntitySystem

            :param entity: Entity to be added
        """
        if self.has_entity(entity):
            logger.warning("Entity already in EntitySystem")
        else:
            if len(self.entities):
                entity.identity = self.entities[-1].identity + 1
            else:
                entity.identity = 0
            entity.system = self
            self.entities.append(entity)

    def remove_entity(self, entity):
        """
            Remove an entity from EntitySystem

            :param entity: Entity to remove
        """
        if self.has_entity(entity):
            self.entities.remove(entity)
        else:
            logger.warning("Entity is not in EntitySystem")

    def has_entity(self, entity):
        """
            Verify if EntitySystem have an entity

            :param entity: Entity
            :return: True if entity is in EntitySystem else False
        """
        return entity in set(self.entities)

    def event(self, evt):
        """
            Call event

            :param evt: Event

            .. note:: You may not use this method. World make it for you
        """
        for i in self.entities:
            i.event(evt)

    def update(self):
        """
            Update EntitySystem

            .. note:: You may not use this method. Window make it for you
        """
        for i in self.entities:
            i.update()

            if i.has_component(PositionComponent):
                position = i.get_component(PositionComponent).position()
                if i.has_component(ShowComponent):
                    if i.get_component(ShowComponent).use_sprite:
                        image = i.get_component(SpriteComponent).transformed_image
                    else:
                        image = i.get_component(TextComponent).render
                    height = image.get_rect().height
                    width = image.get_rect().width
                    if position.x < 0 or position.y < 0 or position.x > self.world.window.width - width or \
                            position.y > self.world.window.height - height:
                        self.world.window.call("OUTOFWINDOW", i, position)
                elif i.has_component(ShapeComponent):
                    shape = i.get_component(ShapeComponent).old_shape
                    if shape is not None:
                        if position.x < 0 or position.y < 0 or position.x > self.world.window.width - shape.width or \
                                position.y > self.world.window.height - shape.height:
                            self.world.window.call("OUTOFWINDOW", i, position)

    def show(self, screen):
        """
            Show world in screen

            :param screen: Screen where world is showed
            :return: Rects must be updated

            .. note:: You may not use this method. World it this for you.
        """
        rects = []
        for entity in self.entities:
            if entity.has_component(ShowComponent):
                rects += entity.get_component(ShowComponent).show(screen)
            elif entity.has_component(ShapeComponent):
                rects += entity.get_component(ShapeComponent).show(screen)
        return rects

    def show_debug(self, screen):
        """
            Show debug world in screen

            :param screen: Screen where world is showed
            :return: Rects must be updated

            .. note:: You may not use this method. World it this for you.
        """
        rects = []
        for entity in self.entities:
            if entity.has_component(ShowComponent):
                rects += entity.get_component(ShowComponent).show_debug(screen)
            elif entity.has_component(ShapeComponent):
                rects += entity.get_component(ShapeComponent).show_debug(screen)
        return rects
