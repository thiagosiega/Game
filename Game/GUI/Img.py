import pygame

class Imgs:
    def __init__(self, Img, largura, altura, x, y):
        self.Img = Img
        self.largura = largura
        self.altura = altura
        self.x = x
        self.y = y

    def carregar_imagem(self):
        imagem = pygame.image.load(self.Img)
        imagem = pygame.transform.scale(imagem, (self.largura, self.altura))
        return imagem
    
    def desenhar_imagem(self, tela):
        tela.blit(self.carregar_imagem(), (self.x, self.y))