from pyengine2.Utils import logger, Font, Color


class UISystem:
    def __init__(self, world):
        """
            Constructor of UISystem

            :param world: World of EntitySystem

            .. note:: You may not use this constructor. EntitySystem is already create in World
        """
        self.world = world
        self.widgets = []
        self.debug_font = Font(bold=True, color=Color.from_name("RED"))

    def add_widget(self, widget):
        """
            Add an widget in UISystem

            :param widget: Widget to be added
        """
        if self.has_widget(widget):
            logger.warning("Widget already in UISystem")
        else:
            if len(self.widgets):
                widget.identity = self.widgets[-1].identity + 1
            else:
                widget.identity = 0
            widget.system = self
            self.widgets.append(widget)

    def remove_widget(self, widget):
        """
            Remove an widget from UISystem

            :param widget: Widget to remove
        """
        if self.has_widget(widget):
            self.widgets.remove(widget)
        else:
            logger.warning("Widget is not in UISystem")

    def has_widget(self, widget):
        """
            Verify if UISystem have an widget

            :param widget: Widget
            :return: True if widget is in UISystem else False
        """
        return widget in set(self.widgets)

    def event(self, evt):
        """
            Call event

            :param evt: Event

            .. note:: You may not use this method. World make it for you
        """
        for i in self.widgets:
            i.event(evt)

    def update(self):
        """
            Update EntitySystem

            .. note:: You may not use this method. Window make it for you
        """
        for i in self.widgets:
            i.update()

    def show(self, screen):
        """
            Show world in screen

            :param screen: Screen where world is showed
            :return: Rects must be updated

            .. note:: You may not use this method. World it this for you.
        """
        rects = []
        for widget in self.widgets:
            rects += widget.show(screen)
        return rects

    def show_debug(self, screen):
        """
            Show debug world in screen

            :param screen: Screen where world is showed
            :return: Rects must be updated

            .. note:: You may not use this method. World it this for you.
        """
        rects = []
        for widget in self.widgets:
            rects += widget.show_debug(screen)
        return rects
