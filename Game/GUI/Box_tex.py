import pygame

class Box_texto:
    def __init__(self, altura, largura, cor, tela, fonte, texto, x, y, cor_texto, tamanho):
        self.altura = altura
        self.largura = largura
        self.cor = cor
        self.tela = tela
        self.fonte = fonte
        self.texto = texto
        self.x = x
        self.y = y
        self.posicao = (self.x, self.y)
        self.cor_texto = cor_texto
        self.tamanho = tamanho

    def exibir_texto(self):
        # Desenha o fundo preto
        self.tela.fill((0, 0, 0))  # Cor de fundo preto
        # Desenha o quadrado azul na parte inferior da tela
        pygame.draw.rect(self.tela, (0, 0, 255), pygame.Rect(0, 500, 800, 100))  # Cor azul
        # Renderiza o texto
        texto_surface = self.fonte.render(self.texto, True, self.cor_texto)
        self.tela.blit(texto_surface, self.posicao)  # Desenha o texto na tela
        pygame.display.flip()  # Atualiza a tela

    def atualizar_texto(self, texto):
        self.texto = texto
        self.exibir_texto()
