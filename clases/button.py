import random

class Button():
    POSITIONS_ANIMALS = [(175,150), (525,150), (175, 450), (525,450)]
    index = 0

    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)
    
    @classmethod
    def set_random_position(cls, button):
        if cls.index == 0:
            random.shuffle(cls.POSITIONS_ANIMALS)
        new_pos = cls.POSITIONS_ANIMALS[cls.index]
        cls.index = (cls.index + 1) % len(cls.POSITIONS_ANIMALS)
        # Actualiza la posición del rectángulo y el texto
        button.x_pos = new_pos[0]
        button.y_pos = new_pos[1]
        button.rect.center = (button.x_pos, button.y_pos)
        button.text_rect.center = (button.x_pos, button.y_pos)