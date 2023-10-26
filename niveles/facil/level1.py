import pygame, sys
from clases.button import Button
from clases.functions import get_font, text
from pantallas import perdiste
from clases import life, contador

pygame.init()

SCREEN = pygame.display.set_mode((700, 600))
BG = pygame.image.load("assets/Background.png")

QUESTION = Button(image=pygame.image.load("assets/frame1.png"), pos=(265, 80), 
                    text_input="PREGUNTA", font=get_font(12), base_color="black", hovering_color="black")
ANSWER1 = Button(image=pygame.image.load("assets/frame.png"), pos=(175, 420), 
                    text_input="#1", font=get_font(12), base_color="black", hovering_color="black")
ANSWER2 = Button(image=pygame.image.load("assets/frame.png"), pos=(525, 420), 
                    text_input="#2", font=get_font(12), base_color="black", hovering_color="black")
ANSWER3 = Button(image=pygame.image.load("assets/frame.png"), pos=(175, 520), 
                    text_input="#3", font=get_font(12), base_color="black", hovering_color="black")
ANSWER4 = Button(image=pygame.image.load("assets/frame.png"), pos=(525, 520), 
                    text_input="#4", font=get_font(12), base_color="black", hovering_color="black")

COUNTER1 = contador.Counter()
COUNTER2 = contador.Counter()
COUNTER3 = contador.Counter()
COUNTER4 = contador.Counter()

def level1():
    while True:
        pygame.display.set_caption("Nivel 1")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)
        SCREEN.blit(BG, (0,0))

        text("NIVEL 1", "White", 12, 570, 30, SCREEN)
        text(f"Vidas:{HEARTS}", "White", 12,  570, 60, SCREEN)

        for button in [QUESTION, ANSWER1, ANSWER2, ANSWER3, ANSWER4]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    if life.LIFE <= 1:
                        life.LIFE = 5
                        perdiste.perdedor()
                    else:
                        if COUNTER1.counter:
                            COUNTER1.off_counter()
                            # ANSWER1.image.fill('black')
                            life.restar_vida()
                if ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    # ANSWER2.changeImage(image=pygame.image.load("assets/frame1.png"))
                    pass

        pygame.display.update()
