import pygame, sys
from clases.button import Button
from pantallas import menu

pygame.init()

SCREEN = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Nivel 1")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def level1():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0,0))

        PLAY_TEXT = get_font(40).render("NIVEL 1", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(370, 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        ANSWER1 = Button(image=pygame.image.load("assets/frame.png"), pos=(175, 420), 
                           text_input="VOLVER", font=get_font(12), base_color="black", hovering_color="black")
        ANSWER2 = Button(image=pygame.image.load("assets/frame.png"), pos=(525, 420), 
                            text_input="VOLVER", font=get_font(12), base_color="black", hovering_color="black")
        ANSWER3 = Button(image=pygame.image.load("assets/frame.png"), pos=(175, 520), 
                            text_input="VOLVER", font=get_font(12), base_color="black", hovering_color="black")
        ANSWER4 = Button(image=pygame.image.load("assets/frame.png"), pos=(525, 520), 
                            text_input="VOLVER", font=get_font(12), base_color="black", hovering_color="black")

        for button in [ANSWER1, ANSWER2, ANSWER3, ANSWER4]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    # menu.main_menu()
                    pass

        pygame.display.update()
