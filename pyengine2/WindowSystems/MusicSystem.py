import pygame


class MusicSystem:
    def __init__(self):
        """
            Create MusicSystem

            .. note:: You may not use this contructor. Window make it for you
        """
        pygame.mixer.init()
        self.queue = []
        self.ENDSOUND = 231
        self.volume = 100
        self.loop = False
        pygame.mixer.music.set_endevent(self.ENDSOUND)

    @property
    def volume(self):
        """
            Return volume

            :return: Volume
        """
        return round(pygame.mixer.music.get_volume()*100)

    @volume.setter
    def volume(self, vol):
        """
            Set Volume

            :param vol: Volume (Between 0 and 100)
        """
        pygame.mixer.music.set_volume(vol/100)

    def next_song(self):
        """Pass to the next song"""
        if len(self.queue):
            pygame.mixer.music.load(self.queue[0])
            pygame.mixer.music.play()
            if self.loop:
                self.queue.append(self.queue[0])
            del self.queue[0]

    def clear_queue(self):
        """Clear the queue"""
        self.queue = []

    def play(self):
        """Play music"""
        if len(self.queue):
            pygame.mixer.music.load(self.queue[0])
            pygame.mixer.music.play()
            if self.loop:
                self.queue.append(self.queue[0])
            del self.queue[0]

    def add(self, file):
        """
            Add file to queue

            :param file: File to be played
        """
        self.queue.append(file)

    @staticmethod
    def stop():
        """Stop music"""
        pygame.mixer.music.stop()

    @staticmethod
    def pause():
        """Pause music"""
        pygame.mixer.music.pause()

    @staticmethod
    def unpause():
        """Unpause music"""
        pygame.mixer.music.unpause()

