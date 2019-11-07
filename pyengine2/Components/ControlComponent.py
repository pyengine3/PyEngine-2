from pyengine2.Components.Component import Component
from pyengine2.Components.PositionComponent import PositionComponent
from pyengine2.Components.CollisionComponent import CollisionComponent
from pyengine2.Components.PhysicsComponent import PhysicsComponent
from pyengine2.Utils import logger

import pygame.locals as const


class ControlComponent(Component):
    types = ["FOURDIRECTION", "UPDOWN", "LEFTRIGHT", "CLASSICJUMP"]

    def __init__(self, control_type, speed=5):
        """
            Create ControlComponent

            This Component is here to make player control entity
            Required Components : PositionComponent

            :param control_type: Type of control ("FOURDIRECTION", "UPDOWN", "LEFTRIGHT", "CLASSICJUMP")
            :param speed: Speed of movement
        """
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
        self.jumping = False

        self.required_components.add(PositionComponent)
        if self.control_type == "CLASSICJUMP":
            self.required_components.add(PhysicsComponent)

    def update(self):
        """
            Update ControlComponent

            .. note:: You may not this method. Entity make it for you
        """
        for i in self.keypressed:
            self.move_by_key(i)

    def move_by_key(self, key):
        """
            Move Entity by key pressed

            .. note:: You may not this method. ControlComponent make it for you
        """
        pos = self.entity.get_component(PositionComponent).position()
        cause = "UNKNOWN"
        if key == self.controls["UPJUMP"]:
            if self.control_type in ("FOURDIRECTION", "DOWNUP"):
                pos.y -= self.speed
                cause = "UPCONTROL"
            elif self.control_type == "CLASSICJUMP":
                phys = self.entity.get_component(PhysicsComponent)
                if phys.grounded and not self.jumping:
                    phys.grounded = False
                    self.jumping = True
                    phys.gravity = -phys.max_gravity
        elif key == self.controls["DOWN"]:
            if self.control_type in ("FOURDIRECTION", "DOWNUP"):
                pos.y += self.speed
                cause = "DOWNCONTROL"
        elif key == self.controls["RIGHT"]:
            if self.control_type in ("FOURDIRECTION", "LEFTRIGHT", "CLASSICJUMP"):
                pos.x += self.speed
                cause = "RIGHTCONTROL"
        elif key == self.controls["LEFT"]:
            if self.control_type in ("FOURDIRECTION", "LEFTRIGHT", "CLASSICJUMP"):
                pos.x -= self.speed
                cause = "LEFTCONTROL"

        if pos != self.entity.get_component(PositionComponent).position():
            if self.entity.has_component(CollisionComponent):
                if self.entity.get_component(CollisionComponent).can_go(pos.x, pos.y, cause):
                    self.entity.get_component(PositionComponent).set_position(pos.x, pos.y)
            else:
                self.entity.get_component(PositionComponent).set_position(pos.x, pos.y)

    def keyup(self, evt):
        """
            Event KEYUP

            .. note:: You may not this method. Entity make it for you
        """
        if evt.key in self.keypressed:
            self.keypressed.remove(evt.key)
        if self.control_type == "CLASSICJUMP" and evt.key == self.controls["UPJUMP"]:
            self.jumping = False

    def keypress(self, evt):
        """
            Event KEYDOWN

            .. note:: You may not this method. Entity make it for you
        """
        if evt.key not in self.keypressed:
            self.keypressed.add(evt.key)
