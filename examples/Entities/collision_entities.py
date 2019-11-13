from pyengine2 import Window
from pyengine2.Entities import Entity
from pyengine2.Components import PositionComponent, SpriteComponent, ShowComponent, CollisionComponent, ControlComponent
from pyengine2.Utils import Vec2

import os


def collision(other_entity, cause):
    pass


images = [os.path.join(os.path.dirname(__file__), "sprite0.png")]

game = Window(780, 500, debug=True)

e = Entity()

e.add_component(ShowComponent())  # Doesn't work because Required Components are not added

e.add_component(PositionComponent(100, 100))
e.add_component(SpriteComponent(images[0], size=Vec2(78, 50)))
e.add_component(ShowComponent())
e.add_component(CollisionComponent(collision))
e.add_component(PhysicsComponent())
e.add_component(ControlComponent("CLASSICJUMP"))

e2 = Entity()

e2.add_component(PositionComponent(100, 300))
e2.add_component(SpriteComponent(images[0], size=Vec2(78, 50)))
e2.add_component(ShowComponent())
e2.add_component(CollisionComponent())

game.world.entity_system.add_entity(e)
game.world.entity_system.add_entity(e2)

game.run()
