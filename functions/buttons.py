import pygame, random
from clases.button import Button
from functions.functions import get_font

POSITIONS = [(175, 420), (525, 420), (175, 520), (525, 520)]
random.shuffle(POSITIONS)

#MENU-----------------------------
EASY_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 240), 
                    text_input="FACIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
MEDIUN_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 360), 
                    text_input="MEDIO", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
HARD_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(360, 480), 
                    text_input="DIFICIL", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
BACK_BUTTON = Button(None, pos=(610, 30), 
                    text_input="VOLVER", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

#FACIL-----------------------------

#LEVEL1----------------------------
EASY_LEVEL1_QUESTION = Button(image=pygame.image.load("assets/frame1.png"), pos=(265, 80), 
                    text_input="¿Cuál es el animal más grande del mundo?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER1 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[0], 
                    text_input="Ballena Azul", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER2 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[1], 
                    text_input="Ballena jorobada", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER3 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[2], 
                    text_input="Oso", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_ANSWER4 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[3], 
                    text_input="Elefante", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL1_BACK_BUTTON = Button(None, pos=(565,120), 
                    text_input="VOLVER", font=get_font(12), base_color="black", hovering_color="white")

#LEVEL2-------------------------------
EASY_LEVEL2_QUESTION = Button(image=pygame.image.load("assets/frame1.png"), pos=(265, 80), 
                    text_input="¿Qué animal es carnívoro?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER1 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[0], 
                    text_input="Tigre", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER2 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[1], 
                    text_input="Conejo", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER3 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[2], 
                    text_input="Cebra", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_ANSWER4 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[3], 
                    text_input="Perezoso", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL2_BACK_BUTTON = Button(None, pos=(565,120), 
                    text_input="VOLVER", font=get_font(12), base_color="black", hovering_color="white")

#LEVEL3---------------------------------
EASY_LEVEL3_QUESTION = Button(image=pygame.image.load("assets/frame1.png"), pos=(265, 80), 
                    text_input="¿Qué animal juega con su presa antes de comérsela?", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER1 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[0], 
                    text_input="Orca", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER2 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[1], 
                    text_input="Delfín", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER3 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[2], 
                    text_input="León", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_ANSWER4 = Button(image=pygame.image.load("assets/frame.png"), pos=POSITIONS[3], 
                    text_input="Tigre", font=get_font(12), base_color="black", hovering_color="black")
EASY_LEVEL3_BACK_BUTTON = Button(None, pos=(565,120), 
                    text_input="VOLVER", font=get_font(12), base_color="black", hovering_color="white")

#LEVEL4-------------------------------