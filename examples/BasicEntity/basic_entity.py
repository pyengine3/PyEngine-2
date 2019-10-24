from pyengine2 import Window
from pyengine2.Entities import Entity
from pyengine2.Components import PositionComponent, SpriteComponent, ShowComponent

import os


game = Window(250, 250, debug=True)

e = Entity()

e.add_component(ShowComponent())  # Doesn't work because Required Components are not added

e.add_component(PositionComponent(10, 10))
e.add_component(SpriteComponent(os.path.join(os.path.dirname(__file__), "sprite0.png")))
e.add_component(ShowComponent())

game.world.entity_system.add_entity(e)

game.run()