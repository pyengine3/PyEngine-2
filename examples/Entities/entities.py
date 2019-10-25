from pyengine2 import Window
from pyengine2.Entities import Entity
from pyengine2.Components import *
from pyengine2.Utils import Vec2

import os

images = [os.path.join(os.path.dirname(__file__), "sprite0.png")]

game = Window(780, 500, debug=True)

e = Entity()

e.add_component(ShowComponent())  # Doesn't work because Required Components are not added

e.add_component(PositionComponent(10, 10))
e.add_component(SpriteComponent(images[0], size=Vec2(50, 50), rotation=45))
e.add_component(ShowComponent())
e.add_component(ControlComponent("FOURDIRECTION"))

e2 = Entity()

e2.add_component(PositionComponent(500, 20))
e2.add_component(TextComponent("Ceci est un test"))
e2.add_component(ShowComponent(False))

game.world.entity_system.add_entity(e)
game.world.entity_system.add_entity(e2)

game.run()