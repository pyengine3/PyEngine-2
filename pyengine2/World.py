from pyengine2.WorldSystems.EntitySystem import EntitySystem
from pyengine2.WorldSystems.UISystem import UISystem


class World:
    def __init__(self, window):
        """
            Create World

            :param window: Window where world can be showed

            .. note:: Window create a first world. If you use only one world, use it.
        """
        self.window = window
        self.entity_system = EntitySystem(self)
        self.ui_system = UISystem(self)
        self.dirty_rects = []

    def event(self, evt):
        """
            Call event

            :param evt: Event

            .. note:: You may not use this method. Window make it for you
        """
        self.entity_system.event(evt)
        self.ui_system.event(evt)

    def update(self):
        """
            Update World

            .. note:: You may not use this method. Window make it for you
        """
        self.entity_system.update()
        self.ui_system.update()

    def show(self, screen):
        """
            Show world on screen

            :param screen: Screen where World must be showed

            .. note:: You may not use this method. Window make it for you.
        """
        self.dirty_rects.append(self.entity_system.show(screen))
        self.dirty_rects.append(self.ui_system.show(screen))

    def show_debug(self, screen):
        """
            Show world on screen

            :param screen: Screen where World must be showed

            .. note:: You may not use this method. Window make it for you.
        """
        self.dirty_rects.append(self.entity_system.show_debug(screen))
        self.dirty_rects.append(self.ui_system.show_debug(screen))
