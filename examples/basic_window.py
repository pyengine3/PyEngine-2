from pyengine2 import Window
from pyengine2.Utils import Color


def start():
    print("START CALLBACK")


def stop():
    print("STOP CALLBACK")


window = Window(250, 250, color=Color.from_name("NAVY_BLUE"), debug=True)
window.set_callback("START", start)
window.set_callback("STOP", stop)
window.run()
