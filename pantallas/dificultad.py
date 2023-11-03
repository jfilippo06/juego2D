import pygame
import sys
import random
from clases.music import Music, Sounds
from clases.contador import Counter
from clases.button import Button
from functions.functions import text
from functions import countdown, life
from pantallas import menu, dificultad, perdiste, ganaste
from functions.buttons import EASY_BUTTON, MEDIUN_BUTTON, HARD_BUTTON, BACK_BUTTON
from functions.buttons import EASY_LEVEL1_QUESTION, EASY_LEVEL1_ANSWER1, EASY_LEVEL1_ANSWER2, EASY_LEVEL1_ANSWER3, EASY_LEVEL1_ANSWER4, EASY_LEVEL1_BACK_BUTTON
from functions.buttons import EASY_LEVEL2_QUESTION, EASY_LEVEL2_ANSWER1, EASY_LEVEL2_ANSWER2, EASY_LEVEL2_ANSWER3, EASY_LEVEL2_ANSWER4, EASY_LEVEL2_BACK_BUTTON
from functions.buttons import EASY_LEVEL3_QUESTION, EASY_LEVEL3_ANSWER1, EASY_LEVEL3_ANSWER2, EASY_LEVEL3_ANSWER3, EASY_LEVEL3_ANSWER4, EASY_LEVEL3_BACK_BUTTON

pygame.init()

SCREEN = pygame.display.set_mode((700, 650))
BG = pygame.image.load("assets/fondo.png")

MUSIC = Music("sounds/thinking-time.mp3")
MUSIC_MENU = Music("sounds/once-in-paris.mp3")
LOSE_MUSIC = Music("sounds/lose.mp3")
YOU_WIN_MUSIC = Music("sounds/winner.mp3")
VICTORY_SOUND = Sounds("sounds/victory.mp3")
FAIL_SOUND = Sounds("sounds/fail.mp3")

COUNTER1 = Counter()
COUNTER2 = Counter()
COUNTER3 = Counter()

clock = pygame.time.Clock()
buttons_easy = [EASY_LEVEL1_ANSWER1, EASY_LEVEL1_ANSWER2, EASY_LEVEL1_ANSWER3, EASY_LEVEL1_ANSWER4,
                EASY_LEVEL2_ANSWER1, EASY_LEVEL2_ANSWER2, EASY_LEVEL2_ANSWER3, EASY_LEVEL2_ANSWER4,
                EASY_LEVEL3_ANSWER1, EASY_LEVEL3_ANSWER2, EASY_LEVEL3_ANSWER3, EASY_LEVEL3_ANSWER4,]


def update_positions(buttons):
    for button in buttons:
        Button.set_random_position(button)


def lifeClockEasy():
    global generado_niveles_easy
    if life.LIFE <= 1:
        life.LIFE = 5
        generado_niveles_easy = obtener_elemento(easy_levels)
        LOSE_MUSIC.play()
        perdiste.perdedor()
    countdown.reset_timer(90)
    FAIL_SOUND.play()
    life.restar_vida()


def lifeClockMediun():
    global generado_niveles_mediun
    if life.LIFE <= 1:
        life.LIFE = 5
        generado_niveles_mediun = obtener_elemento(mediun_levels)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    countdown.reset_timer(90)
    FAIL_SOUND.play()
    life.restar_vida()


def lifeClockHard():
    global generado_niveles_hard
    if life.LIFE <= 1:
        life.LIFE = 5
        generado_niveles_hard = obtener_elemento(hard_levels)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    countdown.reset_timer(90)
    FAIL_SOUND.play()
    life.restar_vida()


def lifeButtonEasy(COUNTER):
    global generado_niveles_easy
    if life.LIFE <= 1:
        life.LIFE = 5
        generado_niveles_easy = obtener_elemento(easy_levels)
        LOSE_MUSIC.play()
        perdiste.perdedor()
    else:
        if COUNTER.counter:
            COUNTER.off_counter()
            FAIL_SOUND.play()
            life.restar_vida()


def lifeButtonMediun(COUNTER):
    global generado_niveles_mediun
    if life.LIFE <= 1:
        life.LIFE = 5
        generado_niveles_mediun = obtener_elemento(mediun_levels)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    else:
        if COUNTER.counter:
            COUNTER.off_counter()
            # FAIL_SOUND.play()
            life.restar_vida()


def lifeButtonHard(COUNTER):
    global generado_niveles_hard
    if life.LIFE <= 1:
        life.LIFE = 5
        generado_niveles_hard = obtener_elemento(hard_levels)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    else:
        if COUNTER.counter:
            COUNTER.off_counter()
            # FAIL_SOUND.play()
            life.restar_vida()


def volverEasy():
    global generado_niveles_easy
    generado_niveles_easy = obtener_elemento(easy_levels)
    life.LIFE = 5
    reset_counter()
    MUSIC_MENU.play()
    MUSIC_MENU.set_volume(0.5)
    dificultad.main_menu()


def volverMediun():
    global generado_niveles_mediun
    generado_niveles_mediun = obtener_elemento(mediun_levels)
    life.LIFE = 5
    reset_counter()
    # MUSIC_MENU.play()
    # MUSIC_MENU.set_volume(0.5)
    dificultad.main_menu()


def volverHard():
    global generado_niveles_hard
    generado_niveles_hard = obtener_elemento(hard_levels)
    life.LIFE = 5
    reset_counter()
    # MUSIC_MENU.play()
    # MUSIC_MENU.set_volume(0.5)
    dificultad.main_menu()


def ganadorEasy():
    global get_name_levels
    get_name_levels = name_levels()
    VICTORY_SOUND.play()
    countdown.start_timer(90)
    reset_counter()
    niveles_aleatorios_easy()


def ganadorMediun():
    # VICTORY_SOUND.play()
    countdown.start_timer(90)
    reset_counter()
    niveles_aleatorios_mediun()


def ganadorHard():
    # VICTORY_SOUND.play()
    countdown.start_timer(90)
    reset_counter()
    niveles_aleatorios_hard()


def reset_counter():
    COUNTER1.on_counter()
    COUNTER2.on_counter()
    COUNTER3.on_counter()


def main_menu():
    while True:
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
                    update_positions(buttons_easy)
                    MUSIC.play()
                    MUSIC.set_volume(1)
                    countdown.start_timer(90)
                    niveles_aleatorios_easy()
                if MEDIUN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu.main_menu()

        pygame.display.update()


def easy_level1():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        for button in [EASY_LEVEL1_ANSWER1, EASY_LEVEL1_ANSWER2, EASY_LEVEL1_ANSWER3, EASY_LEVEL1_ANSWER4, EASY_LEVEL1_QUESTION, EASY_LEVEL1_BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        text(get_name_levels, "black", 12, 50, 14, SCREEN)
        text(f"Vidas:{HEARTS}", "black", 12,  650, 14, SCREEN)
        text("Tiempo:" + countdown.get_time(), "black", 12, 625, 640, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == countdown.timer_event:
                lifeClockEasy()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_LEVEL1_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL1_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL1_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if EASY_LEVEL1_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if EASY_LEVEL1_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def easy_level2():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        for button in [EASY_LEVEL2_ANSWER1, EASY_LEVEL2_ANSWER2, EASY_LEVEL2_ANSWER3, EASY_LEVEL2_ANSWER4, EASY_LEVEL2_QUESTION, EASY_LEVEL2_BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        text(get_name_levels, "black", 12, 50, 14, SCREEN)
        text(f"Vidas:{HEARTS}", "black", 12,  650, 14, SCREEN)
        text("Tiempo:" + countdown.get_time(), "black", 12, 625, 640, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == countdown.timer_event:
                lifeClockEasy()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_LEVEL2_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL2_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL2_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if EASY_LEVEL2_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if EASY_LEVEL2_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def easy_level3():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        for button in [EASY_LEVEL3_ANSWER1, EASY_LEVEL3_ANSWER2, EASY_LEVEL3_ANSWER3, EASY_LEVEL3_ANSWER4, EASY_LEVEL3_QUESTION, EASY_LEVEL3_BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        text(get_name_levels, "black", 12, 50, 14, SCREEN)
        text(f"Vidas:{HEARTS}", "black", 12,  650, 14, SCREEN)
        text("Tiempo:" + countdown.get_time(), "black", 12, 625, 640, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == countdown.timer_event:
                lifeClockEasy()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_LEVEL3_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if EASY_LEVEL3_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL3_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL3_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if EASY_LEVEL3_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


easy_levels = [easy_level1, easy_level2, easy_level3]
mediun_levels = []
hard_levels = []


def obtener_elemento(niveles):
    random.shuffle(niveles)
    for nivel in niveles:
        yield nivel


generado_niveles_easy = obtener_elemento(easy_levels)
generado_niveles_mediun = obtener_elemento(mediun_levels)
generado_niveles_hard = obtener_elemento(hard_levels)


def niveles_aleatorios_easy():
    global generado_niveles_easy
    siguiente = next(generado_niveles_easy, None)
    if siguiente is None:
        generado_niveles_easy = obtener_elemento(easy_levels)
        YOU_WIN_MUSIC.play()
        life.LIFE = 5
        ganaste.ganador()
    else:
        siguiente()


def niveles_aleatorios_mediun():
    global generado_niveles_mediun
    siguiente = next(generado_niveles_mediun, None)
    if siguiente is None:
        generado_niveles_mediun = obtener_elemento(mediun_levels)
        # YOU_WIN_MUSIC.play()
        life.LIFE = 5
        ganaste.ganador()
    else:
        siguiente()


def niveles_aleatorios_hard():
    global generado_niveles_hard
    siguiente = next(generado_niveles_hard, None)
    if siguiente is None:
        generado_niveles_hard = obtener_elemento(hard_levels)
        # YOU_WIN_MUSIC.play()
        life.LIFE = 5
        ganaste.ganador()
    else:
        siguiente()


def niveles():
    lista_niveles = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4",
                     "Nivel 5", "Nivel 6", "Nivel 7", "Nivel 8", "Nivel 9", "Nivel 10"]
    while True:
        for nivel in lista_niveles:
            yield nivel


gen = niveles()


def name_levels():
    return next(gen)


get_name_levels = name_levels()
