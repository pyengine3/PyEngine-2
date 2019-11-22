from pyengine2 import Window
from pyengine2.Widgets import Label, Button, Entry
from pyengine2.Utils import Color, Font


def screenshot():
    title = en.text
    if title == "":
        title = "screen"
    title += ".jpg"
    game.screenshot(path=title)


game = Window(600, 300, debug=True)

label = Label(300 - Font(size=30).rendered_size("Screenshot")[0] / 2, 40, "Screenshot", font=Font(size=30))
b = Button(250, 160, "Screen", screenshot)
en = Entry(200, 100, font=Font(size=18, color=Color.from_name("BLACK")))

game.world.ui_system.add_widget(label)
game.world.ui_system.add_widget(b)
game.world.ui_system.add_widget(en)

game.run()
