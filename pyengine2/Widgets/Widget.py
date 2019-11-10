from pyengine2.Utils import Vec2


class Widget:
    def __init__(self, x, y):
        """
            Create Widget

            :param x: X Pos
            :param y: Y Pos

            .. note:: You may not use this constructor. Widget isn't util
        """
        self.x = x
        self.y = y
        self.identity = None
        self.system = None
        self.showed = True
        self.active = True
        self.old_debug_pos = None
        self.old_render = None
        self.render = None
        self.old_pos = None

    def event(self, evt):
        """
            Manage Event

            :param evt: Event triggered

            .. note:: You may not use this method. UISystem make it for you
        """
        pass

    def update(self):
        """
            Update Widget

            .. note:: You may not use this method. UISystem make it for you
        """
        pass

    def show(self, screen):
        """
            Show Widget to screen

            :param screen: Screen where widget must be showed
            :return: Rects must be updated

            .. note:: You may not use this method. UISystem make it for you
        """
        rects = []
        if self.showed:
            if self.old_render != self.render or self.old_pos != Vec2(self.x, self.y):
                if self.old_render is not None:
                    screen.fill(self.system.world.window.color.get_rgba(), self.old_render.get_rect(x=self.old_pos.x,
                                                                                                    y=self.old_pos.y))
                    rects.append(self.old_render.get_rect(x=self.old_pos.x, y=self.old_pos.y))
                screen.blit(self.render, (self.x, self.y))
                rects.append(self.render.get_rect(x=self.x, y=self.y))
                self.old_render = self.render
                self.old_pos = Vec2(self.x, self.y)
            else:
                screen.blit(self.render, (self.x, self.y))
        else:
            if self.old_render is not None:
                screen.fill(self.system.world.window.color.get_rgba(), self.old_render.get_rect(x=self.old_pos.x,
                                                                                                y=self.old_pos.y))
                rects.append(self.old_render.get_rect(x=self.old_pos.x, y=self.old_pos.y))
                self.old_render = None
                self.old_pos = None
        return rects

    def show_debug(self, screen):
        """
            Show debug widget to screen

            :param screen: Screen where entity is showed
            :return: Rects must be updated

            .. note:: You may not use this method. EntitySystem make it for you
        """
        rects = []
        if self.showed:
            pos = Vec2(self.x, self.y)
            image = self.system.debug_font.render("ID : "+str(self.identity))
            if self.old_debug_pos != pos:
                if self.old_debug_pos is not None:
                    rect = image.get_rect(x=self.old_debug_pos.x, y=self.old_debug_pos.y - 20)
                    rects.append(rect)
                    screen.fill(self.system.world.window.color.get_rgba(), rect)
                self.old_debug_pos = pos
                rects.append(image.get_rect(x=pos.x, y=pos.y-20))

            screen.blit(image, (pos.x, pos.y - 20))
        else:
            if self.old_debug_pos is not None:
                image = self.system.debug_font.render("ID : "+str(self.identity))
                screen.fill(self.system.world.window.color.get_rgba(),
                            image.get_rect(x=self.old_debug_pos.x, y=self.old_debug_pos.y - 20))
                rects.append(image.get_rect(x=self.old_debug_pos.x, y=self.old_debug_pos.y - 20))
                self.old_debug_pos = None
        return rects
