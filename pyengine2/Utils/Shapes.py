from pyengine2.Utils.Logger import logger
from pyengine2.Utils.Color import Color
from pyengine2.Utils.Vec2 import Vec2
import math
import pygame


class Rect:
    def __init__(self, width, height, color=Color.from_name("WHITE"), full=True):
        self.width = width
        self.height = height
        self.color = color
        self.full = full

    def show(self, x, y, screen):
        if self.full:
            return pygame.draw.rect(screen, self.color.get_rgba(), pygame.Rect(x, y, self.width, self.height))
        else:
            return pygame.draw.rect(screen, self.color.get_rgba(), pygame.Rect(x, y, self.width, self.height), 4)


class Polygon:
    def __init__(self,  *points, color=Color.from_name("WHITE"), full=True):
        self.points = points
        self.color = color
        self.full = full
        if len(self.points) < 2:
            logger.warning("Polygon have less than 3 points.")

    def show(self, x, y, screen):
        points = ((x, y), *tuple((i + Vec2(x, y)).coords() for i in self.points))
        if self.full:
            return pygame.draw.polygon(screen, self.color.get_rgba(), points)
        else:
            return pygame.draw.polygon(screen, self.color.get_rgba(), points, 4)


class Circle:
    def __init__(self, radius, color=Color.from_name("WHITE"), full=True):
        self.radius = radius
        self.color = color
        self.full = full

    def show(self, x, y, screen):
        if self.full:
            return pygame.draw.circle(screen, self.color.get_rgba(), (x, y), self.radius)
        else:
            return pygame.draw.circle(screen, self.color.get_rgba(), (x, y), self.radius, 4)


class Ellipse(Rect):
    def __init__(self, width, height, color=Color.from_name("WHITE"), full=True):
        super(Ellipse, self).__init__(width, height, color, full)

    def show(self, x, y, screen):
        if self.full:
            return pygame.draw.ellipse(screen, self.color.get_rgba(), pygame.Rect(x, y, self.width, self.height))
        else:
            return pygame.draw.ellipse(screen, self.color.get_rgba(), pygame.Rect(x, y, self.width, self.height), 4)


class Arc(Rect):
    def __init__(self, width, height, start_angle, stop_angle, color=Color.from_name("WHITE"), width_line=1):
        super(Arc, self).__init__(width, height, color, True)
        self.start_angle = math.radians(start_angle)
        self.stop_angle = math.radians(stop_angle)
        self.width_line = width_line

    def show(self, x, y, screen):
        return pygame.draw.arc(screen, self.color.get_rgba(), pygame.Rect(x, y, self.width, self.height),
                                   self.start_angle, self.stop_angle, self.width_line)


class Line:
    def __init__(self, xlength, ylength, color=Color.from_name("WHITE"), width_line=1):
        self.xlength = xlength
        self.ylength = ylength
        self.color = color
        self.width_line = width_line

    def show(self, x, y, screen):
        return pygame.draw.line(screen, self.color.get_rgb(), (x, y), (x+self.xlength, y+self.ylength), self.width_line)
