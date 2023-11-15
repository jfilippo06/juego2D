import os
import pygame
from clases.music import Music

# RUTA PRICIPAL
RUTA_PRINCIPAL = 'C:\MisProyectos\Python\Pygame\juego2D'

# FONT
FONT = "assets/font.ttf"
FONT = os.path.join(RUTA_PRINCIPAL, FONT)
FONT = os.path.abspath(FONT)

# FONDO
FONDO_MENU = "assets/fondo.png"
FONDO_MENU = os.path.join(RUTA_PRINCIPAL, FONDO_MENU)
FONDO_MENU = os.path.abspath(FONDO_MENU)
BG = pygame.image.load(FONDO_MENU)

# ICO
FONDO_ICO = "assets/fondo_circulo.png"
FONDO_ICO = os.path.join(RUTA_PRINCIPAL, FONDO_ICO)
FONDO_ICO = os.path.abspath(FONDO_ICO)
ICO = pygame.image.load(FONDO_ICO)

# MUSIC
MUSIC_MENU = "sounds/once-in-paris.mp3"
MUSIC_MENU = os.path.join(RUTA_PRINCIPAL, MUSIC_MENU)
MUSIC_MENU = os.path.abspath(MUSIC_MENU)
MUSIC = Music(MUSIC_MENU)

# PLAY BUTTON
BUTTON = "assets/button.png"
BUTTON = os.path.join(RUTA_PRINCIPAL, BUTTON)
BUTTON = os.path.abspath(BUTTON)
BUTTON = pygame.image.load(BUTTON)
