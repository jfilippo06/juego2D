import pygame, sys
from clases.button import Button
from clases.music import Music
from functions.functions import get_font, text
from pantallas import dificultad

pygame.init()

SCREEN = pygame.display.set_mode((700, 600))
BG = pygame.image.load("assets/fondo.png")
MUSIC = Music("sounds/once-in-paris.mp3")
MUSIC.set_volume(0)
MUSIC.play()


PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 250), 
                    text_input="INICIAR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 370), 
                    text_input="SALIR", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

def main_menu():
    while True:
        pygame.display.set_caption("Animal Questions")
         
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        text("ANIMAL QUESTIONS", "#b68f40", 40, 360, 110, SCREEN)

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