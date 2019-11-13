from pyengine2 import Window
from pyengine2.Entities import Entity
from pyengine2.Components import PositionComponent, ShapeComponent
from pyengine2.Utils.Shapes import Rect, Polygon, Circle, Ellipse, Arc, Line
from pyengine2.Utils import Vec2, Color

import os

images = [os.path.join(os.path.dirname(__file__), "sprite0.png")]

game = Window(780, 500, debug=True)

rect = Entity()
rect.add_component(PositionComponent(30, 30))
rect.add_component(ShapeComponent(Rect(200, 200, color=Color.from_name("RED"), full=False)))

poly = Entity()
poly.add_component(PositionComponent(290, 30))
poly.add_component(ShapeComponent(Polygon(Vec2(200, -20), Vec2(80, 50), Vec2(50, 100), color=Color.from_name("BLUE"))))

circle = Entity()
circle.add_component(PositionComponent(650, 150))
circle.add_component(ShapeComponent(Circle(60, color=Color.from_name("YELLOW"), full=False)))

ellipse = Entity()
ellipse.add_component(PositionComponent(30, 280))
ellipse.add_component(ShapeComponent(Ellipse(89, 150, color=Color.from_name("GREEN"))))

arc = Entity()
arc.add_component(PositionComponent(290, 280))
arc.add_component(ShapeComponent(Arc(200, 200, 80, 180, color=Color.from_name("BROWN"), width_line=5)))

line = Entity()
line.add_component(PositionComponent(550, 280))
line.add_component(ShapeComponent(Line(185, 65, color=Color.from_name("FUCHSIA"))))

game.world.entity_system.add_entity(rect)
game.world.entity_system.add_entity(poly)
game.world.entity_system.add_entity(circle)
game.world.entity_system.add_entity(ellipse)
game.world.entity_system.add_entity(arc)
game.world.entity_system.add_entity(line)

game.run()
