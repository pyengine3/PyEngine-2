from pyengine2 import Window
from pyengine2.Widgets import Button, Label
from pyengine2.Utils import Lang

import os


def change_lang():
    global english, nbclick

    nbclick += 1

    if not english:
        b.text = "Francais"
        b.update_render()
        l.text = en.get_translate("accueil", "Welcome {}", nbclick)
        l.update_render()
        english = True
    else:
        b.text = "English"
        b.update_render()
        l.text = fr.get_translate("accueil", "Welcome {}", nbclick)
        l.update_render()
        english = False


window = Window(500, 500, debug=True)
en = Lang(os.path.join(os.path.dirname(__file__), "en.lang"))
fr = Lang(os.path.join(os.path.dirname(__file__), "fr.lang"))

english = False
nbclick = 0
l = Label(100, 100, fr.get_translate("accueil", "Welcome {}", nbclick))
b = Button(200, 200, "English", change_lang)

window.world.ui_system.add_widget(l)
window.world.ui_system.add_widget(b)

window.run()
