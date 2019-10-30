from pyengine2 import Window
from pyengine2.Widgets import Label
from pyengine2.Utils import Config, Font, Color

import os


window = Window(500, 500, debug=True)
config = Config(os.path.join(os.path.dirname(__file__), "config.json"))

if not config.created:
    dic = {
        "label": {
            "text": "Bonjour",
            "color": "RED"
        }
    }
    config.create(dic)

l = Label(100, 100, config.get("label.text", "Bonjour"), Font(color=Color.from_name(config.get("label.color", "RED"))))

window.world.ui_system.add_widget(l)

window.run()
