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

    def show(self, screen):
        """
            Show world on screen

            :param screen: Screen where World must be showed

            .. note:: You may not use this method. Window make it for you.
        """
        self.entity_system.show(screen)
