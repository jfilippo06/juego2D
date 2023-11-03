import pygame
import random
from clases.button import Button
from functions.functions import get_font

# pos=(265, 80)
# POSITIONS = [(175, 420), (525, 420), (175, 520), (525, 520)]
POSITIONS_ANIMALS = [(175, 175), (525, 175), (175, 475), (525, 475)]
BACK = (50, 640)
ASK = (350, 325)
random.shuffle(POSITIONS_ANIMALS)

# MENU-----------------------------
EASY_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(360, 240),
                     text_input="FACIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
MEDIUN_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(360, 360),
                       text_input="MEDIO", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
HARD_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(360, 480),
                     text_input="DIFICIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
BACK_BUTTON = Button(None, pos=(610, 30),
                     text_input="VOLVER", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

# FACIL-----------------------------

# LEVEL1----------------------------
EASY_LEVEL1_QUESTION = Button(image=pygame.image.load("assets/dificultad/facil/nivel1/ask.png"), pos=ASK,
                              text_input="¿Cuál es el animal más grande del mundo?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel1/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel1/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel1/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel1/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")


# LEVEL2-------------------------------
EASY_LEVEL2_QUESTION = Button(image=pygame.image.load("assets/dificultad/facil/nivel2/ask.png"), pos=ASK,
                              text_input="¿Qué animal es carnívoro?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel2/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel2/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel2/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel2/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")

# LEVEL3---------------------------------
EASY_LEVEL3_QUESTION = Button(image=pygame.image.load("assets/dificultad/facil/nivel3/ask.png"), pos=ASK,
                              text_input="¿Qué animal juega con su presa antes de comérsela?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel3/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel3/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel3/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel3/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")

# LEVEL4-------------------------------
EASY_LEVEL4_QUESTION = Button(image=pygame.image.load("assets/dificultad/facil/nivel4/ask.png"), pos=ASK,
                              text_input="¿Cuál de las aves no pueden volar?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL4_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel4/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL4_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel4/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL4_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel4/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL4_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel4/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL4_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")

# LEVEL5---------------------------------
EASY_LEVEL5_QUESTION = Button(image=pygame.image.load("assets/dificultad/facil/nivel5/ask.png"), pos=ASK,
                              text_input="¿Cuál de estos animales carga con su casa?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL5_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel5/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL5_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel5/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL5_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel5/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL5_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel5/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL5_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")

# LEVEL6---------------------------------
EASY_LEVEL6_QUESTION = Button(image=pygame.image.load("assets/dificultad/facil/nivel6/ask.png"), pos=ASK,
                              text_input="¿Cuál de estos grupos de animales es el más extenso?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL6_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel6/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL6_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel6/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL6_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel6/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL6_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel6/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL6_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")

# LEVEL7---------------------------------
EASY_LEVEL7_QUESTION = Button(image=pygame.image.load("assets/dificultad/facil/nivel7/ask.png"), pos=ASK,
                              text_input="¿Cuál es el animal con la mordida más fuerte?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL7_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel7/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL7_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel7/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL7_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel7/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL7_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel7/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL7_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")

# LEVEL8---------------------------------
EASY_LEVEL8_QUESTION = Button(image=pygame.image.load("assets/dificultad/facil/nivel8/ask.png"), pos=ASK,
                              text_input="¿Cuál es el mejor amigo del hombre?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL8_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel8/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL8_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel8/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL8_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel8/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL8_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel8/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL8_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")

# LEVEL9---------------------------------
EASY_LEVEL9_QUESTION = Button(image=pygame.image.load("assets/dificultad/facil/nivel9/ask.png"), pos=ASK,
                              text_input="¿Cuál de estos animales tiene la mejor memoria?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL9_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel9/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL9_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel9/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL9_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel9/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL9_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel9/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL9_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")

# LEVEL10---------------------------------
