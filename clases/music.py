import pygame

class Music:
    def __init__(self, archivo_musica):
        pygame.init()
        self.archivo_musica = archivo_musica

    def play(self):
        pygame.mixer.music.load(self.archivo_musica)
        pygame.mixer.music.play(-1)

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)


class Sounds:
    def __init__(self, archivo_musica):
        pygame.init()
        self.archivo_musica = archivo_musica

    def play(self):
        pygame.mixer.Sound(self.archivo_musica).play()
