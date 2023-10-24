import pygame, sys
from clases.button import Button
from niveles.facil import level1

pygame.init()

SCREEN = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Dificultad")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("DIFICULTAD", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))
        

        EASY_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 240), 
                            text_input="FACIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        MEDIUN_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 360), 
                            text_input="MEDIO", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        HARD_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 480), 
                            text_input="DIFICIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [EASY_BUTTON, MEDIUN_BUTTON, HARD_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level1.level1()
                if MEDIUN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # pygame.quit()
                    # sys.exit()
                    pass

        pygame.display.update()