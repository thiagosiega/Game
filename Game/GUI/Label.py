import pygame

class Label:
    def __init__(self, x, y, text, font_size=20, font_color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)