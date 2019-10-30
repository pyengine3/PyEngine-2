from pyengine2.Widgets.Widget import Widget
from pyengine2.Utils import Font, logger


class Label(Widget):
    def __init__(self, x, y, text, font=Font()):
        """
            Create Label

            :param x: X Pos
            :param y: Y Pos
            :param text: Text of Label
            :param font: Font of Label
        """
        super(Label, self).__init__(x, y)
        self.text = text
        self.font = font
        self.render = self.font.render(text)
        self.old_render = None

    @property
    def text(self):
        """
            Get text of Label

            :return: Text of Label
        """
        return self.__text

    @text.setter
    def text(self, text):
        """
            Set text of Label

            :param text: Text
        """
        self.__text = text

        if "\n" in text:
            logger.warning("Label doesn't support multiline. Use MultilineLabel")

    def update_render(self):
        """
            Update render of Label

            .. note:: You must use this method after any change in Label
        """
        self.render = self.font.render(self.text)

    def show(self, screen):
        """
            Show Label to screen

            :param screen: Screen where widget must be showed
            :return: Rects must be updated

            .. note:: You may not use this method. UISystem make it for you
        """
        screen.blit(self.render, (self.x, self.y))
        if self.old_render != self.render:
            self.old_render = self.render
            yield self.render.get_rect(x=self.x, y=self.y)
