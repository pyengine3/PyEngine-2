from pyengine2.Components.Component import Component
from pyengine2.Utils import Font


class TextComponent(Component):
    def __init__(self, text, font=Font()):
        """
            Create TextComponent

            :param text: Text of Component
            :param font: Font of Component
        """
        super(TextComponent, self).__init__()
        self.font = font
        self.text = text
        self.render = self.font.render(self.text)

    def update_render(self):
        """
            Update the render of Component

            .. note:: You must use this method after any changes in component (Font or text)
        """
        self.render = self.font.render(self.text)
