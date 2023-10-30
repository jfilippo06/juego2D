import pygame, sys, random
from clases.button import Button
from clases.functions import get_font, text
from clases.music import Music, Sounds
from clases import life, contador, countdown
from pantallas import perdiste, ganaste

pygame.init()

SCREEN = pygame.display.set_mode((700, 600))
BG = pygame.image.load("assets/Background.png")
VICTORY_SOUND = Sounds("sounds/victory.mp3")
FAIL_SOUND = Sounds("sounds/fail.mp3")
LOSE_MUSIC = Music("sounds/lose.mp3")
YOU_WIN_MUSIC = Music("sounds/winner.mp3")

POSITIONS = [(175, 420), (525, 420), (175, 520), (525, 520)]
random.shuffle(POSITIONS)

QUESTION = Button(image=pygame.image.load("assets/frame1.png"), pos=(265, 80), 
                    text_input="PREGUNTA", font=get_font(12), base_color="black", hovering_color="black")
ANSWER1 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[0], 
                    text_input="#1", font=get_font(12), base_color="black", hovering_color="black")
ANSWER2 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[1], 
                    text_input="#2", font=get_font(12), base_color="black", hovering_color="black")
ANSWER3 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[2], 
                    text_input="#3", font=get_font(12), base_color="black", hovering_color="black")
ANSWER4 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[3], 
                    text_input="#4", font=get_font(12), base_color="black", hovering_color="black")

COUNTER1 = contador.Counter()
COUNTER2 = contador.Counter()
COUNTER3 = contador.Counter()
COUNTER4 = contador.Counter()

clock = pygame.time.Clock()

def level1():
    while True:
        pygame.display.set_caption("Nivel 1")
        
        SCREEN.blit(BG, (0,0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)
        
        text("NIVEL 1", "White", 12, 570, 30, SCREEN)
        text(f"Vidas:{HEARTS}", "White", 12,  570, 60, SCREEN)
        text("Tiempo:" + countdown.get_time(), "White", 12,  595, 90, SCREEN)
        
        for button in [QUESTION, ANSWER1, ANSWER2, ANSWER3, ANSWER4]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == countdown.timer_event:
                if life.LIFE <= 1:
                    LOSE_MUSIC.play()
                    life.LIFE = 5
                    perdiste.perdedor()
                countdown.reset_timer(90)
                life.restar_vida()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    if life.LIFE <= 1:
                        LOSE_MUSIC.play()
                        life.LIFE = 5
                        perdiste.perdedor()
                    else:
                        if COUNTER1.counter:
                            FAIL_SOUND.play()
                            # COUNTER1.off_counter()
                            life.restar_vida()
                if ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    VICTORY_SOUND.play()
                if ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    YOU_WIN_MUSIC.play()
                    life.LIFE = 5
                    ganaste.ganador()
                if ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    pass

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)
