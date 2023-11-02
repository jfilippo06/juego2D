import pygame, sys
from clases.button import Button
from clases.music import Music
from functions.functions import get_font, text
from pantallas import menu

pygame.init()

SCREEN = pygame.display.set_mode((700, 650))
MUSIC = Music("sounds/once-in-paris.mp3")

PLAY_BACK = Button(image=None, pos=(370, 300), 
                    text_input="VOLVER AL MENU PRINCIPAL", font=get_font(22), base_color="White", hovering_color="Green")

def perdedor():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.set_caption("Perdiste")

        SCREEN.fill("black")

        text("HAZ PERDIDO", "white", 40, 370, 200, SCREEN)

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