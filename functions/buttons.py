import pygame
import random
from clases.button import Button
from functions.functions import get_font

ASK = (350, 325)
ASK2 = (350, 80)
BACK = (50, 640)
POSITIONS_ANIMALS = [(175, 175), (525, 175), (175, 475), (525, 475)]
POSITIONS_BUTTONS = [(175, 420), (525, 420), (175, 520), (525, 520)]
random.shuffle(POSITIONS_ANIMALS)
random.shuffle(POSITIONS_BUTTONS)

# MENU------------------------------
EASY_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(360, 240),
                     text_input="FACIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
MEDIUN_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(360, 360),
                       text_input="MEDIO", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
HARD_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(360, 480),
                     text_input="DIFICIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
BACK_BUTTON = Button(None, pos=(610, 30),
                     text_input="VOLVER", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

# LEVELS----------------------------
LEVEL_BACK_BUTTON = Button(None, pos=BACK,
                                 text_input="SALIR", font=get_font(12), base_color="black", hovering_color="white")

# FACIL-----------------------------

# LEVEL1----------------------------
EASY_LEVEL1_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál es el animal más grande del mundo?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel1/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel1/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel1/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel1/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL2-------------------------------
EASY_LEVEL2_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Qué animal es carnívoro?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel2/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel2/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel2/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel2/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL3---------------------------------
EASY_LEVEL3_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Qué animal juega con su presa antes de comérsela?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel3/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel3/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel3/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel3/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL4-------------------------------
EASY_LEVEL4_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál de las aves no pueden volar?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL4_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel4/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL4_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel4/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL4_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel4/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL4_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel4/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL5---------------------------------
EASY_LEVEL5_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál de estos animales carga con su casa?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL5_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel5/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL5_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel5/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL5_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel5/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL5_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel5/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL6---------------------------------
EASY_LEVEL6_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál de estos grupos de animales es el más extenso?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL6_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel6/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL6_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel6/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL6_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel6/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL6_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel6/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL7---------------------------------
EASY_LEVEL7_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál es el animal con la mordida más fuerte?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL7_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel7/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL7_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel7/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL7_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel7/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL7_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel7/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL8---------------------------------
EASY_LEVEL8_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál es el mejor amigo del hombre?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL8_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel8/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL8_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel8/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL8_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel8/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL8_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel8/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL9---------------------------------
EASY_LEVEL9_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál de estos animales tiene la mejor memoria?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL9_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel9/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL9_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel9/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL9_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel9/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL9_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel9/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL10---------------------------------
EASY_LEVEL10_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál es el animal nacional de Venezuela?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL10_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/facil/nivel10/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL10_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/facil/nivel10/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL10_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/facil/nivel10/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL10_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/facil/nivel10/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# MEDIO-----------------------------------

# LEVEL1---------------------------------
MEDIUN_LEVEL1_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿En qué habitad vive el topo de nariz estrellada?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL1_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/media/nivel1/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL1_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/media/nivel1/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL1_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/media/nivel1/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL1_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/media/nivel1/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL2---------------------------------
MEDIUN_LEVEL2_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál animal tiene el olfato más desarrollado?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL2_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/media/nivel2/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL2_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/media/nivel2/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL2_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/media/nivel2/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL2_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/media/nivel2/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL3---------------------------------
MEDIUN_LEVEL3_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿El sonido más fuerte por un ser vivo lo causa?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL3_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/media/nivel3/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL3_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/media/nivel3/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL3_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/media/nivel3/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL3_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/media/nivel3/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL4---------------------------------
MEDIUN_LEVEL4_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK2,
                              text_input="¿Cuantas horas pueden llegar a dormir un koala?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL4_ANSWER1 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[0],
                             text_input="2 Horas", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL4_ANSWER2 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[1],
                             text_input="4 Horas", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL4_ANSWER3 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[2],
                             text_input="22 Horas", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL4_ANSWER4 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[3],
                             text_input="15 Horas", font=get_font(12), base_color="black", hovering_color="black")

# LEVEL5---------------------------------
MEDIUN_LEVEL5_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK2,
                              text_input="¿Dónde viven los osos polares?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL5_ANSWER1 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[0],
                             text_input="Ártico", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL5_ANSWER2 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[1],
                             text_input="Polo sur", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL5_ANSWER3 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[2],
                             text_input="Polo norte", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL5_ANSWER4 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[3],
                             text_input="Antártida", font=get_font(12), base_color="black", hovering_color="black")

# LEVEL6---------------------------------
MEDIUN_LEVEL6_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK2,
                              text_input="¿Cómo se comunican los elefantes?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL6_ANSWER1 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[0],
                             text_input="Señas", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL6_ANSWER2 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[1],
                             text_input="Infrasonidos", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL6_ANSWER3 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[2],
                             text_input="Mirada", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL6_ANSWER4 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[3],
                             text_input="Voz", font=get_font(12), base_color="black", hovering_color="black")

# LEVEL7---------------------------------
MEDIUN_LEVEL7_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK2,
                              text_input="¿Cuál género de caballito de mar puede tener crías?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL7_ANSWER1 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[0],
                             text_input="Hembra", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL7_ANSWER2 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[1],
                             text_input="Macho", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL7_ANSWER3 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[2],
                             text_input="Ambos", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL7_ANSWER4 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[3],
                             text_input="Ninguno", font=get_font(12), base_color="black", hovering_color="black")

# LEVEL8---------------------------------
MEDIUN_LEVEL8_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál es el felino más peligroso?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL8_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/media/nivel8/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL8_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/media/nivel8/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL8_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/media/nivel8/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL8_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/media/nivel8/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL9---------------------------------
MEDIUN_LEVEL9_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál es el animal con los ojos más grandes del planeta?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL9_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/media/nivel9/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL9_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/media/nivel9/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL9_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/media/nivel9/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL9_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/media/nivel9/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")

# LEVEL10---------------------------------
MEDIUN_LEVEL10_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK2,
                              text_input="¿Cuánto dura la gestación de los elefantes?", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL10_ANSWER1 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[0],
                             text_input="22 Meses", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL10_ANSWER2 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[1],
                             text_input="1 Semana", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL10_ANSWER3 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[2],
                             text_input="1 Mes", font=get_font(12), base_color="black", hovering_color="black")
MEDIUN_LEVEL10_ANSWER4 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[3],
                             text_input="1 Año", font=get_font(12), base_color="black", hovering_color="black")

# HARD_LEVELS----------------------------

# LEVEL1---------------------------------
HARD_LEVEL1_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK2,
                              text_input="¿Tasa de mortalidad tiene el mordisco de la mamba negra?", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL1_ANSWER1 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[0],
                             text_input="10%", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL1_ANSWER2 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[1],
                             text_input="50%", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL1_ANSWER3 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[2],
                             text_input="80%", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL1_ANSWER4 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[3],
                             text_input="95%", font=get_font(12), base_color="black", hovering_color="black")

# LEVEL2---------------------------------
HARD_LEVEL2_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK2,
                              text_input="¿Cuál lagarto puede disparar sangre por los ojos?", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL2_ANSWER1 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[0],
                             text_input="Lagarto cornudo", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL2_ANSWER2 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[1],
                             text_input="Lagarto escamaso", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL2_ANSWER3 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[2],
                             text_input="Lagarto escupido", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL2_ANSWER4 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[3],
                             text_input="Lagarto", font=get_font(12), base_color="black", hovering_color="black")

# LEVEL3---------------------------------
HARD_LEVEL3_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK2,
                              text_input="Cuánto puede girar la cabeza de un búho?", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL3_ANSWER1 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[0],
                             text_input="360°", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL3_ANSWER2 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[1],
                             text_input="600°", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL3_ANSWER3 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[2],
                             text_input="70°", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL3_ANSWER4 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[3],
                             text_input="100°", font=get_font(12), base_color="black", hovering_color="black")

# LEVEL4---------------------------------
HARD_LEVEL4_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK2,
                              text_input="Cuánto pesa la lengua de una ballena?", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL4_ANSWER1 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[0],
                             text_input="0.00 Kg°", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL4_ANSWER2 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[1],
                             text_input="100.00 Kg°", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL4_ANSWER3 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[2],
                             text_input="2.000 Kg", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL4_ANSWER4 = Button(image=pygame.image.load("assets/button_ask.png"), pos=POSITIONS_BUTTONS[3],
                             text_input="6.000 Kg", font=get_font(12), base_color="black", hovering_color="black")

# LEVEL5---------------------------------
HARD_LEVEL5_QUESTION = Button(image=pygame.image.load("assets/ask.png"), pos=ASK,
                              text_input="¿Cuál es el insecto más pequeño del mundo?", font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL5_ANSWER1 = Button(image=pygame.image.load("assets/dificultad/dificil/nivel5/1.png"), pos=POSITIONS_ANIMALS[0],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL5_ANSWER2 = Button(image=pygame.image.load("assets/dificultad/dificil/nivel5/2.png"), pos=POSITIONS_ANIMALS[1],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL5_ANSWER3 = Button(image=pygame.image.load("assets/dificultad/dificil/nivel5/3.png"), pos=POSITIONS_ANIMALS[2],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")
HARD_LEVEL5_ANSWER4 = Button(image=pygame.image.load("assets/dificultad/dificil/nivel5/4.png"), pos=POSITIONS_ANIMALS[3],
                             text_input=None, font=get_font(12), base_color="black", hovering_color="black")