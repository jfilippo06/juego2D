import pygame
import sys
from clases.button import Button
from functions.functions import get_font, text
from pantallas import dificultad
from rutas import FONDO_MENU, ICO, MUSIC_MENU, BUTTON

pygame.init()

SCREEN = pygame.display.set_mode((700, 650))
MUSIC_MENU.set_volume(0.5)
# MUSIC_MENU.play()


PLAY_BUTTON = Button(image=BUTTON, pos=(360, 260),
                     text_input="INICIAR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
QUIT_BUTTON = Button(image=BUTTON, pos=(360, 380),
                     text_input="SALIR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")


def main_menu():
    while True:
        pygame.display.set_caption("Animal Quiz")
        pygame.display.set_icon(ICO)

        SCREEN.blit(FONDO_MENU, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        text("ANIMAL QUIZ", "#b68f40", 40, 360, 110, SCREEN)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    dificultad.main_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
