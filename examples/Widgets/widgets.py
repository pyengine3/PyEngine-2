from pyengine2 import Window
from pyengine2.Entities import Entity
from pyengine2.Components import PositionComponent, SpriteComponent, ShowComponent, ControlComponent
from pyengine2.Widgets import Label
from pyengine2.Utils import Vec2

import os

images = [os.path.join(os.path.dirname(__file__), "sprite0.png")]

game = Window(550, 300, debug=True)

l = Label(100, 100, "Test Label :D")

e = Entity()

e.add_component(PositionComponent(0, 0))
e.add_component(SpriteComponent("sprite0.png", size=Vec2(78, 50), rotation=45))
e.add_component(ShowComponent())
e.add_component(ControlComponent("FOURDIRECTION"))

game.world.ui_system.add_widget(l)
game.world.entity_system.add_entity(e)

game.run()
