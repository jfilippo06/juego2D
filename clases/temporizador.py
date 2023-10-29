import pygame

class Temporizador:
    def __init__(self, intervalo):
        self.intervalo = intervalo
        self.evento_temporizador = pygame.USEREVENT + 1
        self.tiempo_inicio = pygame.time.get_ticks()
        pygame.time.set_timer(self.evento_temporizador, self.intervalo)

    def iniciar(self):
        self.activo = True

    def detener(self):
        self.activo = False
        