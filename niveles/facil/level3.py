import pygame, sys, random
from clases.button import Button
from clases.music import Music, Sounds
from clases import contador
from functions.functions import get_font, text
from functions import countdown, life
from pantallas import perdiste, ganaste, dificultad

pygame.init()

SCREEN = pygame.display.set_mode((700, 600))
BG = pygame.image.load("assets/dificultad/facil/nivel1.png")
VICTORY_SOUND = Sounds("sounds/victory.mp3")
FAIL_SOUND = Sounds("sounds/fail.mp3")
LOSE_MUSIC = Music("sounds/lose.mp3")
YOU_WIN_MUSIC = Music("sounds/winner.mp3")

POSITIONS = [(175, 420), (525, 420), (175, 520), (525, 520)]
random.shuffle(POSITIONS)

QUESTION = Button(image=pygame.image.load("assets/frame1.png"), pos=(265, 80), 
                    text_input="¿Qué animal juega con su presa antes de comérsela?", font=get_font(12), base_color="black", hovering_color="black")
ANSWER1 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[0], 
                    text_input="Orca", font=get_font(12), base_color="black", hovering_color="black")
ANSWER2 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[1], 
                    text_input="Delfín", font=get_font(12), base_color="black", hovering_color="black")
ANSWER3 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[2], 
                    text_input="León", font=get_font(12), base_color="black", hovering_color="black")
ANSWER4 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[3], 
                    text_input="Tigre", font=get_font(12), base_color="black", hovering_color="black")
BACK_BUTTON = Button(None, pos=(565,120), 
                    text_input="VOLVER", font=get_font(12), base_color="black", hovering_color="white")

COUNTER1 = contador.Counter()
COUNTER2 = contador.Counter()
COUNTER3 = contador.Counter()

clock = pygame.time.Clock()

def lifeButton(COUNTER):
    if life.LIFE <= 1:
        LOSE_MUSIC.play()
        life.LIFE = 5
        perdiste.perdedor()
    else:
        if COUNTER.counter:
            FAIL_SOUND.play()
            COUNTER.off_counter()
            life.restar_vida()

def ganador():
    YOU_WIN_MUSIC.play()
    life.LIFE = 5
    ganaste.ganador()

def main_level():
    while True:
        pygame.display.set_caption("Nivel 1")
        
        SCREEN.blit(BG, (0,0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)
        
        text("NIVEL 1", "black", 12, 570, 30, SCREEN)
        text(f"Vidas:{HEARTS}", "black", 12,  570, 60, SCREEN)
        text("Tiempo:" + countdown.get_time(), "black", 12,  595, 90, SCREEN)
        
        for button in [QUESTION, ANSWER1, ANSWER2, ANSWER3, ANSWER4, BACK_BUTTON]:
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
                    VICTORY_SOUND.play()
                if ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER1)
                if ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER2)                    
                if ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER3)
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    life.LIFE = 5
                    COUNTER1.on_counter()
                    COUNTER2.on_counter()
                    COUNTER3.on_counter()
                    dificultad.main_menu()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)
