from pyengine2.Components.Component import Component
from pyengine2.Components.PositionComponent import PositionComponent
from pyengine2.Components.CollisionComponent import CollisionComponent


class PhysicsComponent(Component):
    def __init__(self, gravity=5, time_gravity=5):
        """
            Create PhysicsComponent

            This Component is here to add physics to entity
            Required Components : PositionComponent

            :param gravity: Gravity force on Entity
            :param time_gravity: Time to add 1 to gravity
        """
        super(PhysicsComponent, self).__init__()
        self.gravity = gravity
        self.max_gravity = gravity
        self.grounded = False
        self.time_gravity = time_gravity
        self.time = time_gravity
        self.required_components.add(PositionComponent)

    def update(self):
        """
            Update PhysicsComponent

            .. note:: You may not this method. Entity make it for you
        """
        pos = self.entity.get_component(PositionComponent).position()
        pos.y += self.gravity

        if self.entity.has_component(CollisionComponent):
            if self.entity.get_component(CollisionComponent).can_go(pos.x, pos.y, "GRAVITY"):
                self.grounded = False
                self.entity.get_component(PositionComponent).set_position(pos.x, pos.y)
            elif self.gravity > 0:
                self.grounded = True
                self.gravity = 2

            if self.time <= 0 and self.gravity < self.max_gravity and not self.grounded:
                self.gravity += 1
                self.time = self.time_gravity
            self.time -= 1
        else:
            self.entity.get_component(PositionComponent).set_position(pos.x, pos.y)
