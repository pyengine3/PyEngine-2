from pyengine2.Widgets.Widget import Widget
from pyengine2.Utils import Font


class Label(Widget):
    def __init__(self, x, y, text, font=Font()):
        super(Label, self).__init__(x, y)
        self.text = text
        self.font = font
        self.render = self.font.render(text)
        self.old_render = None

    def update_render(self):
        self.render = self.font.render(self.text)

    def show(self, screen):
        screen.blit(self.render, (self.x, self.y))
        if self.old_render != self.render:
            self.old_render = self.render
            yield self.render.get_rect(x=self.x, y=self.y)
