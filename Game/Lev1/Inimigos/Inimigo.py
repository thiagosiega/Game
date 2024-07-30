import pygame
import random

class Inimigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 50
        self.altura = 50
        self.largura = 50
        self.velocidade = 1
        self.id = random.randint(1000, 9999)

    def limite_tela(self, resolucao):
        if self.x < 0:
            self.x = 0
        if self.x + self.largura > resolucao[0]:
            self.x = resolucao[0] - self.largura
        if self.y < 0:
            self.y = 0
        if self.y + self.altura > resolucao[1]:
            self.y = resolucao[1] - self.altura

    def dano(self, player):
        # Se o player colidir com o inimigo, o player perde 10 de hp
        if self.colidir_player(player):
            player.hp -= 1
            if player.hp <= 0:
                return True
        return False

    def desenhar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.largura, self.altura))

    def mover_player(self, player, velocidade):
        if self.x < player.x:
            self.x += velocidade
        if self.x > player.x:
            self.x -= velocidade
        if self.y < player.y:
            self.y += velocidade
        if self.y > player.y:
            self.y -= velocidade

    def colidir_player(self, player):
        if self.x < player.x + player.largura and self.x + self.largura > player.x and self.y < player.y + player.altura and self.y + self.altura > player.y:
            # Calcular a sobreposição
            overlap_x = min(self.x + self.largura - player.x, player.x + player.largura - self.x)
            overlap_y = min(self.y + self.altura - player.y, player.y + player.altura - self.y)

            # Empurrar o player fora do inimigo
            if overlap_x < overlap_y:
                if self.x < player.x:
                    player.x += overlap_x
                else:
                    player.x -= overlap_x
            else:
                if self.y < player.y:
                    player.y += overlap_y
                else:
                    player.y -= overlap_y
            return True
        return False
    def colidir_inimigo(self, inimigo):
        if self.x < inimigo.x + inimigo.largura and self.x + self.largura > inimigo.x and self.y < inimigo.y + inimigo.altura and self.y + self.altura > inimigo.y:
            # Calcular a sobreposição
            overlap_x = min(self.x + self.largura - inimigo.x, inimigo.x + inimigo.largura - self.x)
            overlap_y = min(self.y + self.altura - inimigo.y, inimigo.y + inimigo.altura - self.y)

            # Empurrar o inimigo fora do inimigo
            if overlap_x < overlap_y:
                if self.x < inimigo.x:
                    inimigo.x += overlap_x
                else:
                    inimigo.x -= overlap_x
            else:
                if self.y < inimigo.y:
                    inimigo.y += overlap_y