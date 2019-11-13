from pyengine2 import Window
from pyengine2.Entities import Entity
from pyengine2.Components import PositionComponent, SpriteComponent, ShowComponent, AnimComponent


game = Window(200, 200, debug=True)

e = Entity()
e.add_component(PositionComponent(50, 50))
e.add_component(SpriteComponent("sprite0.png"))
anim = AnimComponent()
anim.add_anim_list("idle", "sprite0.png", "sprite1.png")
e.add_component(anim).play("idle")
e.add_component(ShowComponent())

e2 = Entity()
e2.add_component(PositionComponent(150, 150))
e2.add_component(SpriteComponent("sprite0.png"))
anim = AnimComponent()
anim.add_anim_sheet("idle", "spritesheet.png", 2)
e2.add_component(anim).play("idle")
e2.add_component(ShowComponent())

game.world.entity_system.add_entity(e)
game.world.entity_system.add_entity(e2)

game.run()
