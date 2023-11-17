import os
import pygame
from clases.music import Music, Sounds

# RUTA PRICIPAL
RUTA_PRINCIPAL = 'C:\MisProyectos\Python\Pygame\juego2D'

# FONT
FONT = "assets/font.ttf"
FONT = os.path.join(RUTA_PRINCIPAL, FONT)
FONT = os.path.abspath(FONT)

# ICO
ICO = "assets/fondo_circulo.png"
ICO = os.path.join(RUTA_PRINCIPAL, ICO)
ICO = os.path.abspath(ICO)
ICO = pygame.image.load(ICO)

# FONDO MENU
FONDO_MENU = "assets/fondo.png"
FONDO_MENU = os.path.join(RUTA_PRINCIPAL, FONDO_MENU)
FONDO_MENU = os.path.abspath(FONDO_MENU)
FONDO_MENU = pygame.image.load(FONDO_MENU)

# FONDO PEDEDOR FACIL
FONDO_PERDEDOR_FACIL = "assets/perdedor_facil.png"
FONDO_PERDEDOR_FACIL = os.path.join(RUTA_PRINCIPAL, FONDO_PERDEDOR_FACIL)
FONDO_PERDEDOR_FACIL = os.path.abspath(FONDO_PERDEDOR_FACIL)
FONDO_PERDEDOR_FACIL = pygame.image.load(FONDO_PERDEDOR_FACIL)

# FONDO PEDEDOR MEDIO
FONDO_PERDEDOR_MEDIO = "assets/perdedor_medio.png"
FONDO_PERDEDOR_MEDIO = os.path.join(RUTA_PRINCIPAL, FONDO_PERDEDOR_MEDIO)
FONDO_PERDEDOR_MEDIO = os.path.abspath(FONDO_PERDEDOR_MEDIO)
FONDO_PERDEDOR_MEDIO = pygame.image.load(FONDO_PERDEDOR_MEDIO)

# FONDO PEDEDOR DIFICIL
FONDO_PERDEDOR_DIFICIL = "assets/perdedor_dificil.png"
FONDO_PERDEDOR_DIFICIL = os.path.join(RUTA_PRINCIPAL, FONDO_PERDEDOR_DIFICIL)
FONDO_PERDEDOR_DIFICIL = os.path.abspath(FONDO_PERDEDOR_DIFICIL)
FONDO_PERDEDOR_DIFICIL = pygame.image.load(FONDO_PERDEDOR_DIFICIL)

# FONDO GANADOR FACIL
FONDO_GANADOR_FACIL = "assets/ganador_facil.png"
FONDO_GANADOR_FACIL = os.path.join(RUTA_PRINCIPAL, FONDO_GANADOR_FACIL)
FONDO_GANADOR_FACIL = os.path.abspath(FONDO_GANADOR_FACIL)
FONDO_GANADOR_FACIL = pygame.image.load(FONDO_GANADOR_FACIL)

# FONDO GANADOR MEDIO
FONDO_GANADOR_MEDIO = "assets/ganador_medio.png"
FONDO_GANADOR_MEDIO = os.path.join(RUTA_PRINCIPAL, FONDO_GANADOR_MEDIO)
FONDO_GANADOR_MEDIO = os.path.abspath(FONDO_GANADOR_MEDIO)
FONDO_GANADOR_MEDIO = pygame.image.load(FONDO_GANADOR_MEDIO)

# FONDO GANADOR DIFICIL
FONDO_GANADOR_DIFICIL = "assets/ganador_dificil.png"
FONDO_GANADOR_DIFICIL = os.path.join(RUTA_PRINCIPAL, FONDO_GANADOR_DIFICIL)
FONDO_GANADOR_DIFICIL = os.path.abspath(FONDO_GANADOR_DIFICIL)
FONDO_GANADOR_DIFICIL = pygame.image.load(FONDO_GANADOR_DIFICIL)

# BUTTON
BUTTON = "assets/button.png"
BUTTON = os.path.join(RUTA_PRINCIPAL, BUTTON)
BUTTON = os.path.abspath(BUTTON)
BUTTON = pygame.image.load(BUTTON)

# MUSIC MENU
MUSIC_MENU = "sounds/once-in-paris.mp3"
MUSIC_MENU = os.path.join(RUTA_PRINCIPAL, MUSIC_MENU)
MUSIC_MENU = os.path.abspath(MUSIC_MENU)
MUSIC_MENU = Music(MUSIC_MENU)

# MUSIC MENU
MUSIC = "sounds/thinking-time.mp3"
MUSIC = os.path.join(RUTA_PRINCIPAL, MUSIC)
MUSIC = os.path.abspath(MUSIC)
MUSIC = Music(MUSIC)

# LOSE MUSIC
LOSE_MUSIC = "sounds/lose.mp3"
LOSE_MUSIC = os.path.join(RUTA_PRINCIPAL, LOSE_MUSIC)
LOSE_MUSIC = os.path.abspath(LOSE_MUSIC)
LOSE_MUSIC = Music(LOSE_MUSIC)

# YOU WIN MUSIC
YOU_WIN_MUSIC = "sounds/winner.mp3"
YOU_WIN_MUSIC = os.path.join(RUTA_PRINCIPAL, YOU_WIN_MUSIC)
YOU_WIN_MUSIC = os.path.abspath(YOU_WIN_MUSIC)
YOU_WIN_MUSIC = Music(YOU_WIN_MUSIC)

# VICTORY SOUND
VICTORY_SOUND = "sounds/victory.mp3"
VICTORY_SOUND = os.path.join(RUTA_PRINCIPAL, VICTORY_SOUND)
VICTORY_SOUND = os.path.abspath(VICTORY_SOUND)
VICTORY_SOUND = Sounds(VICTORY_SOUND)

# FAIL SOUND
FAIL_SOUND = "sounds/fail.mp3"
FAIL_SOUND = os.path.join(RUTA_PRINCIPAL, FAIL_SOUND)
FAIL_SOUND = os.path.abspath(FAIL_SOUND)
FAIL_SOUND = Sounds(FAIL_SOUND)

def getPath(path_root):
    IMAGE = path_root
    IMAGE = os.path.join(RUTA_PRINCIPAL, IMAGE)
    IMAGE = os.path.abspath(IMAGE)
    IMAGE = pygame.image.load(IMAGE)
    return IMAGE

def getPathMusic(path_root):
    MUSIC = path_root
    MUSIC = os.path.join(RUTA_PRINCIPAL, MUSIC)
    MUSIC = os.path.abspath(MUSIC)
    MUSIC = Music(MUSIC)
    return MUSIC

def getPathSounds(path_root):
    SOUND = path_root
    SOUND = os.path.join(RUTA_PRINCIPAL, SOUND)
    SOUND = os.path.abspath(SOUND)
    SOUND = Music(SOUND)
    return SOUND
