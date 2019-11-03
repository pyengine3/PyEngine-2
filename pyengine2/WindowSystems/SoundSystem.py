import pygame


class SoundSystem:
    def __init__(self):
        """
            Create SoundSystem

            .. note:: You may not use this contructor. Window make it for you
        """
        self.volume = 100

    @property
    def number_channel(self):
        """
            Get number of sounds can be played in the same time

            :return: Number of sounds
        """
        return pygame.mixer.get_num_channels()

    @number_channel.setter
    def number_channel(self, val):
        """
            Set number of sounds can be played in the same time

            :param val: Number of sounds
        """
        pygame.mixer.set_num_channels(val)

    def play(self, file):
        """
            Play a sound

            :param file: Path of Sound
        """
        sound = pygame.mixer.Sound(file)
        sound.set_volume(self.volume/100)
        sound.play()
