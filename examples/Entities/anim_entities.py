from pyengine2 import Window
from pyengine2.Entities import Entity
from pyengine2.Components import PositionComponent, SpriteComponent, ShowComponent, AnimComponent


game = Window(200, 200, debug=True)

e = Entity()
e.add_component(PositionComponent(100, 100))
e.add_component(SpriteComponent("sprite0.png"))
e.add_component(AnimComponent(20, "sprite0.png", "sprite1.png"))
e.add_component(ShowComponent())

game.world.entity_system.add_entity(e)

game.run()
