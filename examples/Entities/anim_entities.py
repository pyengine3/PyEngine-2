from pyengine2 import Window
from pyengine2.Entities import Entity
from pyengine2.Components import PositionComponent, SpriteComponent, ShowComponent, AnimListComponent,\
    AnimSheetComponent


game = Window(200, 200, debug=True)

e = Entity()
e.add_component(PositionComponent(50, 50))
e.add_component(SpriteComponent("sprite0.png"))
e.add_component(AnimListComponent("sprite0.png", "sprite1.png"))
e.add_component(ShowComponent())

e2 = Entity()
e2.add_component(PositionComponent(150, 150))
e2.add_component(SpriteComponent("sprite0.png"))
e2.add_component(AnimSheetComponent("spritesheet.png", 2))
e2.add_component(ShowComponent())

game.world.entity_system.add_entity(e)
game.world.entity_system.add_entity(e2)

game.run()
