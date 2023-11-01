import pygame
import sys
import random
from clases.music import Music, Sounds
from clases.contador import Counter
from functions.functions import text
from functions import countdown, life
from pantallas import menu, dificultad, perdiste, ganaste
from functions.buttons import EASY_BUTTON, MEDIUN_BUTTON, HARD_BUTTON, BACK_BUTTON
from functions.buttons import EASY_LEVEL1_QUESTION, EASY_LEVEL1_ANSWER1, EASY_LEVEL1_ANSWER2, EASY_LEVEL1_ANSWER3, EASY_LEVEL1_ANSWER4, EASY_LEVEL1_BACK_BUTTON
from functions.buttons import EASY_LEVEL2_QUESTION, EASY_LEVEL2_ANSWER1, EASY_LEVEL2_ANSWER2, EASY_LEVEL2_ANSWER3, EASY_LEVEL2_ANSWER4, EASY_LEVEL2_BACK_BUTTON
from functions.buttons import EASY_LEVEL3_QUESTION, EASY_LEVEL3_ANSWER1, EASY_LEVEL3_ANSWER2, EASY_LEVEL3_ANSWER3, EASY_LEVEL3_ANSWER4, EASY_LEVEL3_BACK_BUTTON

pygame.init()

SCREEN = pygame.display.set_mode((700, 600))
BG = pygame.image.load("assets/fondo.png")

MUSIC = Music("sounds/thinking-time.mp3")
LOSE_MUSIC = Music("sounds/lose.mp3")
YOU_WIN_MUSIC = Music("sounds/winner.mp3")
VICTORY_SOUND = Sounds("sounds/victory.mp3")
FAIL_SOUND = Sounds("sounds/fail.mp3")

COUNTER1 = Counter()
COUNTER2 = Counter()
COUNTER3 = Counter()

clock = pygame.time.Clock()

def lifeClock():
    global generador_niveles
    if life.LIFE <= 1:
        life.LIFE = 5
        generador_niveles = obtener_elemento(niveles)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    countdown.reset_timer(90)
    life.restar_vida()

def lifeButton(COUNTER):
    global generador_niveles
    if life.LIFE <= 1:
        life.LIFE = 5
        generador_niveles = obtener_elemento(niveles)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    else:
        if COUNTER.counter:
            COUNTER.off_counter()
            # FAIL_SOUND.play()
            life.restar_vida()

def volver():
    global generador_niveles
    generador_niveles = obtener_elemento(niveles)
    life.LIFE = 5
    COUNTER1.on_counter()
    COUNTER2.on_counter()
    COUNTER3.on_counter()
    # MUSIC.play()
    # MUSIC.set_volume(0.5)
    dificultad.main_menu()

def ganador():
    # VICTORY_SOUND.play()
    countdown.start_timer(90)
    reset_counter()
    niveles_aleatorios()

def reset_counter():
    COUNTER1.on_counter()
    COUNTER2.on_counter()
    COUNTER3.on_counter()

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
                    niveles_aleatorios()
                if MEDIUN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu.main_menu()

        pygame.display.update()

def easy_level1():
    while True:
        pygame.display.set_caption("Nivel 1")

        BG = pygame.image.load("assets/dificultad/facil/nivel1.png")
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        text("NIVEL 1", "black", 12, 570, 30, SCREEN)
        text(f"Vidas:{HEARTS}", "black", 12,  570, 60, SCREEN)
        text("Tiempo:" + countdown.get_time(), "black", 12,  595, 90, SCREEN)

        for button in [EASY_LEVEL1_QUESTION, EASY_LEVEL1_ANSWER1, EASY_LEVEL1_ANSWER2, EASY_LEVEL1_ANSWER3, EASY_LEVEL1_ANSWER4, EASY_LEVEL1_BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == countdown.timer_event:
                lifeClock()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_LEVEL1_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    ganador()
                if EASY_LEVEL1_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER1)
                if EASY_LEVEL1_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER2)
                if EASY_LEVEL1_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER3)
                if EASY_LEVEL1_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volver()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)

def easy_level2():
    while True:
        pygame.display.set_caption("Nivel 2")
        BG = pygame.image.load("assets/dificultad/facil/nivel1.png")
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        text("NIVEL 2", "black", 12, 570, 30, SCREEN)
        text(f"Vidas:{HEARTS}", "black", 12,  570, 60, SCREEN)
        text("Tiempo:" + countdown.get_time(), "black", 12,  595, 90, SCREEN)

        for button in [EASY_LEVEL2_QUESTION, EASY_LEVEL2_ANSWER1, EASY_LEVEL2_ANSWER2, EASY_LEVEL2_ANSWER3, EASY_LEVEL2_ANSWER4, EASY_LEVEL2_BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == countdown.timer_event:
                lifeClock()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_LEVEL2_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    ganador()
                if EASY_LEVEL2_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER1)
                if EASY_LEVEL2_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER2)
                if EASY_LEVEL2_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER3)
                if EASY_LEVEL2_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volver()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)

def easy_level3():
    while True:
        pygame.display.set_caption("Nivel 3")
        BG = pygame.image.load("assets/dificultad/facil/nivel1.png")
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        text("NIVEL 3", "black", 12, 570, 30, SCREEN)
        text(f"Vidas:{HEARTS}", "black", 12,  570, 60, SCREEN)
        text("Tiempo:" + countdown.get_time(), "black", 12,  595, 90, SCREEN)

        for button in [EASY_LEVEL3_QUESTION, EASY_LEVEL3_ANSWER1, EASY_LEVEL3_ANSWER2, EASY_LEVEL3_ANSWER3, EASY_LEVEL3_ANSWER4, EASY_LEVEL3_BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == countdown.timer_event:
                lifeClock()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_LEVEL3_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    ganador()
                if EASY_LEVEL3_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER1)
                if EASY_LEVEL3_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER2)
                if EASY_LEVEL3_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButton(COUNTER3)
                if EASY_LEVEL3_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volver()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)

niveles = [easy_level1, easy_level2, easy_level3]

def obtener_elemento(niveles):
    random.shuffle(niveles)
    for nivel in niveles:
        yield nivel

generador_niveles = obtener_elemento(niveles)

def niveles_aleatorios():
    global generador_niveles
    siguiente = next(generador_niveles, None)
    if siguiente is None:
        generador_niveles = obtener_elemento(niveles)
        # YOU_WIN_MUSIC.play()
        life.LIFE = 5
        ganaste.ganador()
    else:
        siguiente()

