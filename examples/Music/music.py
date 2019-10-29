from pyengine2 import Window
import pygame.locals as const


class Game(Window):
    def __init__(self):
        super(Game, self).__init__(50, 50, debug=True)

        self.music_system.loop = True
        self.music_system.add("Ridsa - Laisser couler.mp3")
        self.music_system.add("Ridsa - On sen ira.mp3")

    def process_event(self, evt):
        if evt.type == const.KEYUP:
            if evt.key == const.K_p:
                self.music_system.play()
            elif evt.key == const.K_s:
                self.music_system.stop()
            elif evt.key == const.K_u:
                self.music_system.unpause()
            elif evt.key == const.K_n:
                self.music_system.next_song()
            elif evt.key == const.K_a:
                self.music_system.pause()
        super(Game, self).process_event(evt)


game = Game()
game.run()
