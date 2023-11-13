import pygame
import sys
from clases.button import Button
from clases.music import Music
from functions.functions import get_font, text
from pantallas import menu

pygame.init()

SCREEN = pygame.display.set_mode((700, 650))
MUSIC = Music("sounds/once-in-paris.mp3")

PLAY_BACK = Button(image=None, pos=(370, 330),
                   text_input="VOLVER AL MENU PRINCIPAL", font=get_font(22), base_color="White", hovering_color="Green")


def ganador_facil():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        BG = pygame.image.load("assets/ganador_facil.png")
        SCREEN.blit(BG, (0, 0))
        text("HAZ GANADO", "white", 40, 370, 230, SCREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    MUSIC.play()
                    MUSIC.set_volume(0.5)
                    menu.main_menu()

        pygame.display.update()


def ganador_medio():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        BG = pygame.image.load("assets/ganador_medio.png")
        SCREEN.blit(BG, (0, 0))
        text("HAZ GANADO", "white", 40, 370, 230, SCREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    MUSIC.play()
                    MUSIC.set_volume(0.5)
                    menu.main_menu()

        pygame.display.update()


def ganador_dificil():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        BG = pygame.image.load("assets/ganador_dificil.png")
        SCREEN.blit(BG, (0, 0))
        text("HAZ GANADO", "white", 40, 370, 230, SCREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    MUSIC.play()
                    MUSIC.set_volume(0.5)
                    menu.main_menu()

        pygame.display.update()
