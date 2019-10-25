from pyengine2.WorldSystems.EntitySystem import EntitySystem


class World:
    def __init__(self, window):
        """
            Create World

            :param window: Window where world can be showed

            .. note:: Window create a first world. If you use only one world, use it.
        """
        self.window = window
        self.entity_system = EntitySystem(self)
        self.dirty_rects = []
        self.dirty_rects_debug = []

    def event(self, evt):
        """
            Call event

            :param evt: Event

            .. note:: You may not use this method. Window make it for you
        """
        self.entity_system.event(evt)

    def update(self):
        """
            Update World

            .. note:: You may not use this method. Window make it for you
        """
        self.entity_system.update()

    def show(self, screen):
        """
            Show world on screen

            :param screen: Screen where World must be showed

            .. note:: You may not use this method. Window make it for you.
        """
        self.dirty_rects = self.entity_system.show(screen)

    def show_debug(self, screen):
        """
            Show world on screen

            :param screen: Screen where World must be showed

            .. note:: You may not use this method. Window make it for you.
        """
        self.dirty_rects_debug = self.entity_system.show_debug(screen)
