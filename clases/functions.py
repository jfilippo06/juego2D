import pygame

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def text(texto, color, zise, x, y, screen):
    TEXT = get_font(zise).render(texto, True, color)
    RECT = TEXT.get_rect(center=(x,y))
    screen.blit(TEXT, RECT)