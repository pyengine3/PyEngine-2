from pyengine2 import Window
from pyengine2.Entities import Entity
from pyengine2.Components import PositionComponent, SpriteComponent, ShowComponent, ControlComponent
from pyengine2.Widgets import *
from pyengine2.Utils import Vec2, Font, Color

import os


def label_management():
    l.showed = not l.showed
    c.active = not c.active


images = [os.path.join(os.path.dirname(__file__), "sprite0.png")]

game = Window(750, 500, debug=True)

l = Label(100, 100, "Label")
b = Button(200, 200, "Button", label_management)
c = Checkbox(300, 300, "checkbox", scale=2)
i = Image(100, 200, "sprite0.png", Vec2(20, 20))
en = Entry(100, 300, font=Font(size=20, color=Color.from_name("BLACK")))
select = Selector(200, 100, "Ceci", "est", "un", "test", "!", "SELECTOR !")

e = Entity()

e.add_component(PositionComponent(0, 0))
e.add_component(SpriteComponent("sprite0.png", size=Vec2(78, 50), rotation=45))
e.add_component(ShowComponent())
e.add_component(ControlComponent("FOURDIRECTION"))

game.world.ui_system.add_widget(l)
game.world.ui_system.add_widget(b)
game.world.ui_system.add_widget(c)
game.world.ui_system.add_widget(i)
game.world.ui_system.add_widget(en)
game.world.ui_system.add_widget(select)
game.world.entity_system.add_entity(e)

game.run()
