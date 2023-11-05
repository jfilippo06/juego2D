import pygame
import sys
import random
from clases.music import Music, Sounds
from clases.contador import Counter
from clases.button import Button
from functions.functions import text
from functions import countdown, life
from pantallas import menu, dificultad, perdiste, ganaste
from functions.buttons import EASY_BUTTON, MEDIUN_BUTTON, HARD_BUTTON, BACK_BUTTON, LEVEL_BACK_BUTTON
from functions.buttons import EASY_LEVEL1_QUESTION, EASY_LEVEL1_ANSWER1, EASY_LEVEL1_ANSWER2, EASY_LEVEL1_ANSWER3, EASY_LEVEL1_ANSWER4
from functions.buttons import EASY_LEVEL2_QUESTION, EASY_LEVEL2_ANSWER1, EASY_LEVEL2_ANSWER2, EASY_LEVEL2_ANSWER3, EASY_LEVEL2_ANSWER4
from functions.buttons import EASY_LEVEL3_QUESTION, EASY_LEVEL3_ANSWER1, EASY_LEVEL3_ANSWER2, EASY_LEVEL3_ANSWER3, EASY_LEVEL3_ANSWER4
from functions.buttons import EASY_LEVEL4_QUESTION, EASY_LEVEL4_ANSWER1, EASY_LEVEL4_ANSWER2, EASY_LEVEL4_ANSWER3, EASY_LEVEL4_ANSWER4
from functions.buttons import EASY_LEVEL5_QUESTION, EASY_LEVEL5_ANSWER1, EASY_LEVEL5_ANSWER2, EASY_LEVEL5_ANSWER3, EASY_LEVEL5_ANSWER4
from functions.buttons import EASY_LEVEL6_QUESTION, EASY_LEVEL6_ANSWER1, EASY_LEVEL6_ANSWER2, EASY_LEVEL6_ANSWER3, EASY_LEVEL6_ANSWER4
from functions.buttons import EASY_LEVEL7_QUESTION, EASY_LEVEL7_ANSWER1, EASY_LEVEL7_ANSWER2, EASY_LEVEL7_ANSWER3, EASY_LEVEL7_ANSWER4
from functions.buttons import EASY_LEVEL8_QUESTION, EASY_LEVEL8_ANSWER1, EASY_LEVEL8_ANSWER2, EASY_LEVEL8_ANSWER3, EASY_LEVEL8_ANSWER4
from functions.buttons import EASY_LEVEL9_QUESTION, EASY_LEVEL9_ANSWER1, EASY_LEVEL9_ANSWER2, EASY_LEVEL9_ANSWER3, EASY_LEVEL9_ANSWER4
from functions.buttons import EASY_LEVEL10_QUESTION, EASY_LEVEL10_ANSWER1, EASY_LEVEL10_ANSWER2, EASY_LEVEL10_ANSWER3, EASY_LEVEL10_ANSWER4
from functions.buttons import MEDIUN_LEVEL1_QUESTION, MEDIUN_LEVEL1_ANSWER1, MEDIUN_LEVEL1_ANSWER2, MEDIUN_LEVEL1_ANSWER3, MEDIUN_LEVEL1_ANSWER4
from functions.buttons import MEDIUN_LEVEL2_QUESTION, MEDIUN_LEVEL2_ANSWER1, MEDIUN_LEVEL2_ANSWER2, MEDIUN_LEVEL2_ANSWER3, MEDIUN_LEVEL2_ANSWER4

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
                EASY_LEVEL3_ANSWER1, EASY_LEVEL3_ANSWER2, EASY_LEVEL3_ANSWER3, EASY_LEVEL3_ANSWER4,
                EASY_LEVEL4_ANSWER1, EASY_LEVEL4_ANSWER2, EASY_LEVEL4_ANSWER3, EASY_LEVEL4_ANSWER4,
                EASY_LEVEL5_ANSWER1, EASY_LEVEL5_ANSWER2, EASY_LEVEL5_ANSWER3, EASY_LEVEL5_ANSWER4,
                EASY_LEVEL6_ANSWER1, EASY_LEVEL6_ANSWER2, EASY_LEVEL6_ANSWER3, EASY_LEVEL6_ANSWER4,
                EASY_LEVEL7_ANSWER1, EASY_LEVEL7_ANSWER2, EASY_LEVEL7_ANSWER3, EASY_LEVEL7_ANSWER4,
                EASY_LEVEL8_ANSWER1, EASY_LEVEL8_ANSWER2, EASY_LEVEL8_ANSWER3, EASY_LEVEL8_ANSWER4,
                EASY_LEVEL9_ANSWER1, EASY_LEVEL9_ANSWER2, EASY_LEVEL9_ANSWER3, EASY_LEVEL9_ANSWER4,
                EASY_LEVEL10_ANSWER1, EASY_LEVEL10_ANSWER2, EASY_LEVEL10_ANSWER3, EASY_LEVEL10_ANSWER4,]

buttons_mediun = [MEDIUN_LEVEL1_ANSWER1, MEDIUN_LEVEL1_ANSWER2, MEDIUN_LEVEL1_ANSWER3, MEDIUN_LEVEL1_ANSWER4,
                  MEDIUN_LEVEL2_ANSWER1, MEDIUN_LEVEL2_ANSWER2, MEDIUN_LEVEL2_ANSWER3, MEDIUN_LEVEL2_ANSWER4,]


def update_positions(buttons):
    for button in buttons:
        Button.set_random_position(button)


def lifeClockEasy():
    global generado_niveles_easy, get_name_levels
    if life.LIFE <= 1:
        life.LIFE = 5
        reset_gen()
        get_name_levels = name_levels()
        generado_niveles_easy = obtener_elemento(easy_levels)
        LOSE_MUSIC.play()
        perdiste.perdedor()
    countdown.reset_timer(90)
    FAIL_SOUND.play()
    life.restar_vida()


def lifeClockMediun():
    global generado_niveles_mediun, get_name_levels
    if life.LIFE <= 1:
        life.LIFE = 5
        reset_gen()
        get_name_levels = name_levels()
        generado_niveles_mediun = obtener_elemento(mediun_levels)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    countdown.reset_timer(60)
    FAIL_SOUND.play()
    life.restar_vida()


def lifeClockHard():
    global generado_niveles_hard, get_name_levels
    if life.LIFE <= 1:
        life.LIFE = 5
        reset_gen()
        get_name_levels = name_levels()
        generado_niveles_hard = obtener_elemento(hard_levels)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    countdown.reset_timer(90)
    FAIL_SOUND.play()
    life.restar_vida()


def lifeButtonEasy(COUNTER):
    global generado_niveles_easy, get_name_levels
    if life.LIFE <= 1:
        life.LIFE = 5
        reset_gen()
        get_name_levels = name_levels()
        generado_niveles_easy = obtener_elemento(easy_levels)
        LOSE_MUSIC.play()
        perdiste.perdedor()
    else:
        if COUNTER.counter:
            COUNTER.off_counter()
            FAIL_SOUND.play()
            life.restar_vida()


def lifeButtonMediun(COUNTER):
    global generado_niveles_mediun, get_name_levels
    if life.LIFE <= 1:
        life.LIFE = 5
        reset_gen()
        get_name_levels = name_levels()
        generado_niveles_mediun = obtener_elemento(mediun_levels)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    else:
        if COUNTER.counter:
            COUNTER.off_counter()
            FAIL_SOUND.play()
            life.restar_vida()


def lifeButtonHard(COUNTER):
    global generado_niveles_hard, get_name_levels
    if life.LIFE <= 1:
        life.LIFE = 5
        reset_gen()
        get_name_levels = name_levels()
        generado_niveles_hard = obtener_elemento(hard_levels)
        # LOSE_MUSIC.play()
        perdiste.perdedor()
    else:
        if COUNTER.counter:
            COUNTER.off_counter()
            # FAIL_SOUND.play()
            life.restar_vida()


def volverEasy():
    global generado_niveles_easy, get_name_levels
    reset_gen()
    get_name_levels = name_levels()
    generado_niveles_easy = obtener_elemento(easy_levels)
    life.LIFE = 5
    reset_counter()
    MUSIC_MENU.play()
    MUSIC_MENU.set_volume(0.5)
    dificultad.main_menu()


def volverMediun():
    global generado_niveles_mediun, get_name_levels
    reset_gen()
    get_name_levels = name_levels()
    generado_niveles_mediun = obtener_elemento(mediun_levels)
    life.LIFE = 5
    reset_counter()
    # MUSIC_MENU.play()
    # MUSIC_MENU.set_volume(0.5)
    dificultad.main_menu()


def volverHard():
    global generado_niveles_hard, get_name_levels
    reset_gen()
    get_name_levels = name_levels()
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
    global get_name_levels
    get_name_levels = name_levels()
    VICTORY_SOUND.play()
    countdown.start_timer(60)
    reset_counter()
    niveles_aleatorios_mediun()


def ganadorHard():
    global get_name_levels
    get_name_levels = name_levels()
    # VICTORY_SOUND.play()
    countdown.start_timer(90)
    reset_counter()
    niveles_aleatorios_hard()


def reset_counter():
    COUNTER1.on_counter()
    COUNTER2.on_counter()
    COUNTER3.on_counter()

# DICICULT SELECTION-------------------------------------


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
                    update_positions(buttons_mediun)
                    # MUSIC.play()
                    # MUSIC.set_volume(1)
                    countdown.start_timer(60)
                    niveles_aleatorios_mediun()
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu.main_menu()

        pygame.display.update()

# EASY LEVELS--------------------------------------------


def easy_level1():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [EASY_LEVEL1_ANSWER1, EASY_LEVEL1_ANSWER2, EASY_LEVEL1_ANSWER3, EASY_LEVEL1_ANSWER4, EASY_LEVEL1_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
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

        for button in [EASY_LEVEL2_ANSWER1, EASY_LEVEL2_ANSWER2, EASY_LEVEL2_ANSWER3, EASY_LEVEL2_ANSWER4, EASY_LEVEL2_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
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

        for button in [EASY_LEVEL3_ANSWER1, EASY_LEVEL3_ANSWER2, EASY_LEVEL3_ANSWER3, EASY_LEVEL3_ANSWER4, EASY_LEVEL3_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def easy_level4():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [EASY_LEVEL4_ANSWER1, EASY_LEVEL4_ANSWER2, EASY_LEVEL4_ANSWER3, EASY_LEVEL4_ANSWER4, EASY_LEVEL4_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if EASY_LEVEL4_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL4_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL4_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if EASY_LEVEL4_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def easy_level5():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [EASY_LEVEL5_ANSWER1, EASY_LEVEL5_ANSWER2, EASY_LEVEL5_ANSWER3, EASY_LEVEL5_ANSWER4, EASY_LEVEL5_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if EASY_LEVEL5_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL5_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if EASY_LEVEL5_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL5_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def easy_level6():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [EASY_LEVEL6_ANSWER1, EASY_LEVEL6_ANSWER2, EASY_LEVEL6_ANSWER3, EASY_LEVEL6_ANSWER4, EASY_LEVEL6_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if EASY_LEVEL6_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL6_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if EASY_LEVEL6_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL6_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def easy_level7():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [EASY_LEVEL7_ANSWER1, EASY_LEVEL7_ANSWER2, EASY_LEVEL7_ANSWER3, EASY_LEVEL7_ANSWER4, EASY_LEVEL7_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if EASY_LEVEL7_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if EASY_LEVEL7_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL7_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL7_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def easy_level8():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [EASY_LEVEL8_ANSWER1, EASY_LEVEL8_ANSWER2, EASY_LEVEL8_ANSWER3, EASY_LEVEL8_ANSWER4, EASY_LEVEL8_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if EASY_LEVEL8_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL8_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL8_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if EASY_LEVEL8_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def easy_level9():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [EASY_LEVEL9_ANSWER1, EASY_LEVEL9_ANSWER2, EASY_LEVEL9_ANSWER3, EASY_LEVEL9_ANSWER4, EASY_LEVEL9_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if EASY_LEVEL9_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL9_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL9_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if EASY_LEVEL9_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def easy_level10():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [EASY_LEVEL10_ANSWER1, EASY_LEVEL10_ANSWER2, EASY_LEVEL10_ANSWER3, EASY_LEVEL10_ANSWER4, EASY_LEVEL10_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

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
                if EASY_LEVEL10_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER1)
                if EASY_LEVEL10_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER2)
                if EASY_LEVEL10_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    ganadorEasy()
                if EASY_LEVEL10_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonEasy(COUNTER3)
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverEasy()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)

# MEDIUN LEVES-------------------------------------------


def mediun_level1():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [MEDIUN_LEVEL1_ANSWER1, MEDIUN_LEVEL1_ANSWER2, MEDIUN_LEVEL1_ANSWER3, MEDIUN_LEVEL1_ANSWER4, MEDIUN_LEVEL1_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

        text(get_name_levels, "black", 12, 50, 14, SCREEN)
        text(f"Vidas:{HEARTS}", "black", 12,  650, 14, SCREEN)
        text("Tiempo:" + countdown.get_time(), "black", 12, 625, 640, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == countdown.timer_event:
                lifeClockMediun()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MEDIUN_LEVEL1_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    ganadorMediun()
                if MEDIUN_LEVEL1_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonMediun(COUNTER1)
                if MEDIUN_LEVEL1_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonMediun(COUNTER2)
                if MEDIUN_LEVEL1_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonMediun(COUNTER3)
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverMediun()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


def mediun_level2():
    while True:
        SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        HEARTS = str(life.LIFE)

        for button in [MEDIUN_LEVEL2_ANSWER1, MEDIUN_LEVEL2_ANSWER2, MEDIUN_LEVEL2_ANSWER3, MEDIUN_LEVEL2_ANSWER4, MEDIUN_LEVEL2_QUESTION]:
            button.update(SCREEN)

        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(SCREEN, "#E8B03F", pygame.Rect(0, 625, 800, 25))

        LEVEL_BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL_BACK_BUTTON.update(SCREEN)

        text(get_name_levels, "black", 12, 50, 14, SCREEN)
        text(f"Vidas:{HEARTS}", "black", 12,  650, 14, SCREEN)
        text("Tiempo:" + countdown.get_time(), "black", 12, 625, 640, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == countdown.timer_event:
                lifeClockMediun()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MEDIUN_LEVEL2_ANSWER1.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonMediun(COUNTER1)
                if MEDIUN_LEVEL2_ANSWER2.checkForInput(PLAY_MOUSE_POS):
                    ganadorMediun()
                if MEDIUN_LEVEL2_ANSWER3.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonMediun(COUNTER2)
                if MEDIUN_LEVEL2_ANSWER4.checkForInput(PLAY_MOUSE_POS):
                    lifeButtonMediun(COUNTER3)
                if LEVEL_BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    volverMediun()

        pygame.display.update()
        pygame.display.flip()
        countdown.check_timer_event()
        clock.tick(60)


# HARD LEVES---------------------------------------------

easy_levels = [
    easy_level1, easy_level2, easy_level3, easy_level4, easy_level5,
    easy_level6, easy_level7, easy_level8, easy_level9, easy_level10
]
mediun_levels = [mediun_level1, mediun_level2]
hard_levels = []


def obtener_elemento(niveles):
    random.shuffle(niveles)
    for nivel in niveles:
        yield nivel


generado_niveles_easy = obtener_elemento(easy_levels)
generado_niveles_mediun = obtener_elemento(mediun_levels)
generado_niveles_hard = obtener_elemento(hard_levels)


def niveles_aleatorios_easy():
    global generado_niveles_easy, get_name_levels
    siguiente = next(generado_niveles_easy, None)
    if siguiente is None:
        life.LIFE = 5
        reset_gen()
        get_name_levels = name_levels()
        generado_niveles_easy = obtener_elemento(easy_levels)
        YOU_WIN_MUSIC.play()
        ganaste.ganador()
    else:
        siguiente()


def niveles_aleatorios_mediun():
    global generado_niveles_mediun, get_name_levels
    siguiente = next(generado_niveles_mediun, None)
    if siguiente is None:
        life.LIFE = 5
        reset_gen()
        get_name_levels = name_levels()
        generado_niveles_mediun = obtener_elemento(mediun_levels)
        # YOU_WIN_MUSIC.play()
        ganaste.ganador()
    else:
        siguiente()


def niveles_aleatorios_hard():
    global generado_niveles_hard, get_name_levels
    siguiente = next(generado_niveles_hard, None)
    if siguiente is None:
        life.LIFE = 5
        reset_gen()
        get_name_levels = name_levels()
        generado_niveles_hard = obtener_elemento(hard_levels)
        # YOU_WIN_MUSIC.play()
        ganaste.ganador()
    else:
        siguiente()


def niveles():
    lista_niveles = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4",
                     "Nivel 5", "Nivel 6", "Nivel 7", "Nivel 8", "Nivel 9", "Nivel 10"]
    while True:
        for nivel in lista_niveles:
            yield nivel


def reset_gen():
    global gen
    gen = niveles()


gen = niveles()


def name_levels():
    return next(gen)


get_name_levels = name_levels()
