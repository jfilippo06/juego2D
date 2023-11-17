import os
import pygame
from clases.music import Music, Sounds

# RUTA PRICIPAL
RUTA_PRINCIPAL = 'C:\Program Files\Animal Quiz\_internal'

# FONT
FONT = "assets/font.ttf"
FONT = os.path.join(RUTA_PRINCIPAL, FONT)
FONT = os.path.abspath(FONT)

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
    SOUND = Sounds(SOUND)
    return SOUND
