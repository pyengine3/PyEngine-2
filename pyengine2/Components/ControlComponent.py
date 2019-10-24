from pyengine2.Components.Component import Component
from pyengine2.Components.PositionComponent import PositionComponent
from pyengine2.Utils import logger

import pygame.locals as const


class ControlComponent(Component):
    types = ["FOURDIRECTION"]

    def __init__(self, control_type, speed=5):
        super(ControlComponent, self).__init__()
        self.control_type = control_type
        if self.control_type not in ControlComponent.types:
            logger.error("Unknown ControlType : "+str(control_type))

        self.speed = speed

        self.controls = {
            "UPJUMP": const.K_UP,
            "LEFT": const.K_LEFT,
            "RIGHT": const.K_RIGHT,
            "DOWN": const.K_DOWN
        }

        self.keypressed = set()

        self.required_components.add(PositionComponent)

    def update(self):
        for i in self.keypressed:
            self.move_by_key(i)

    def move_by_key(self, key):
        if key == self.controls["UPJUMP"]:
            if self.control_type == "FOURDIRECTION":
                for i in self.entities:
                    i.get_component(PositionComponent).y -= self.speed
        elif key == self.controls["DOWN"]:
            if self.control_type == "FOURDIRECTION":
                for i in self.entities:
                    i.get_component(PositionComponent).y += self.speed
        elif key == self.controls["RIGHT"]:
            if self.control_type == "FOURDIRECTION":
                for i in self.entities:
                    i.get_component(PositionComponent).x += self.speed
        elif key == self.controls["LEFT"]:
            if self.control_type == "FOURDIRECTION":
                for i in self.entities:
                    i.get_component(PositionComponent).x -= self.speed

    def keyup(self, evt):
        if evt.key in self.keypressed:
            self.keypressed.remove(evt.key)

    def keypress(self, evt):
        if evt.key not in self.keypressed:
            self.keypressed.add(evt.key)