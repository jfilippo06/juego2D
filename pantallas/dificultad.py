import pygame, sys
from clases.button import Button
from clases.music import Music
from functions.functions import get_font, text
from functions import countdown
from niveles.facil import level1
from pantallas import menu

pygame.init()

SCREEN = pygame.display.set_mode((700, 600))
BG = pygame.image.load("assets/fondo.png")
MUSIC = Music("sounds/thinking-time.mp3")

EASY_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 240), 
                    text_input="FACIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
MEDIUN_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 360), 
                    text_input="MEDIO", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
HARD_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 480), 
                    text_input="DIFICIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
BACK_BUTTON = Button(None, pos=(610, 30), 
                    text_input="VOLVER", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

def main_menu():
    while True:
        pygame.display.set_caption("Dificultad")
        
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        text("DIFICULTAD", "#b68f40", 40, 360, 100, SCREEN)
 
        for button in [EASY_BUTTON, MEDIUN_BUTTON, HARD_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    MUSIC.play()
                    MUSIC.set_volume(0)
                    countdown.start_timer(90)   
                    level1.main_level1()
                if MEDIUN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu.main_menu()

        pygame.display.update()