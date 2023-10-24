import pygame, sys
from clases.button import Button
from pantallas import menu

pygame.init()

SCREEN = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Nivel 1")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def perdedor():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(40).render("HAZ PERDIDO", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(370, 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(370, 300), 
                            text_input="VOLVER AL MENU PRINCIPAL", font=get_font(22), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    menu.main_menu()

        pygame.display.update()