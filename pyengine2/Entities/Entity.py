from pyengine2.Utils import logger
from pyengine2.Components.ControlComponent import ControlComponent
from pyengine2.Components.AutoComponent import AutoComponent

import pygame.locals as const


class Entity:
    def __init__(self):
        """
            Create basic entity

            .. note:: Basic entity doesn't have any component. You can do nothing with it.
        """
        self.components = set()
        self.system = None
        self.identity = None

    def add_component(self, component):
        """
            Add component to entity

            :param component: Component to be added
            :return: Component added
        """
        if isinstance(component, tuple(type(c) for c in self.components)):
            logger.warning("Entity already have a " + str(component.__class__.__name__))
        else:
            for i in component.required_components:
                if i not in set(type(c) for c in self.components):
                    logger.warning(str(component.__class__.__name__) + " require " + str(i.__name__))
                    return
            component.entity = self
            self.components.add(component)
            return component

    def has_component(self, tcomponent):
        """
            Verify if entity have a type of component

            :param tcomponent: Type of Component
            :return: True if entity have component else False
        """
        if tcomponent in set(type(c) for c in self.components):
            return True
        return False

    def get_component(self, tcomponent):
        """
            Get component from entity with its type

            :param tcomponent: Type of Component
            :return: Component or None

            .. note:: Return None if entity hasn't this type of component
        """
        if self.has_component(tcomponent):
            return tuple(i for i in self.components if isinstance(i, tcomponent))[0]
        logger.warning("Entity doesn't have "+str(tcomponent))

    def remove_component(self, tcomponent):
        """
            Remove component with its type

            :param tcomponent: Type of Component

            .. warning:: This can be dangerous
        """
        logger.info("Remove component can be dangerous.")
        if self.has_component(tcomponent):
            self.components.remove(self.get_component(tcomponent))
        else:
            logger.warning("Entity doesn't have "+str(tcomponent))

    def event(self, evt):
        """
            Call event

            :param evt: Event

            .. note:: You may not use this method. EntitySystem make it for you
        """
        if evt.type == const.KEYDOWN:
            if self.has_component(ControlComponent):
                self.get_component(ControlComponent).keypress(evt)
        elif evt.type == const.KEYUP:
            if self.has_component(ControlComponent):
                self.get_component(ControlComponent).keyup(evt)

    def update(self):
        """
            Update Entity

            .. note:: You may not use this method. EntitySystem make it for you
        """
        if self.has_component(ControlComponent):
            self.get_component(ControlComponent).update()
        if self.has_component(AutoComponent):
            self.get_component(AutoComponent).update()
