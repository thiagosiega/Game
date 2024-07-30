import pygame
import os
import json
import sys
import subprocess
import random


from tkinter import messagebox


# Adicione o caminho antes das importações
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Player.Player import Player
from Inimigos.Inimigo import Inimigo
from GUI.Foco_janela import FocoJanela
from GUI.Label import Label

pygame.init()

def prioridade_janela():
    janela = FocoJanela("Lev1")
    janela.foco_janela()

def carregar_configuracoes():
    file = "Game/Config/Config.json"
    if os.path.exists(file):
        with open(file, "r") as f:
            configuracoes = json.load(f)
            print(configuracoes)
    else:
        configuracoes = {
            "resolucao": [800, 600],
            "fullscreen": False,
            "FPS": 60
        }
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, "w") as f:
            json.dump(configuracoes, f)
    return configuracoes

def janela():
    configuracoes = carregar_configuracoes()
    fullscreen = configuracoes["fullscreen"]

    if fullscreen:
        info = pygame.display.Info()
        resolucao = (info.current_w, info.current_h)
        tela = pygame.display.set_mode(resolucao, pygame.FULLSCREEN)
    else:
        resolucao = configuracoes["resolucao"]
        tela = pygame.display.set_mode(resolucao)
    
    pygame.display.set_caption("Lev1")
    return tela, configuracoes["FPS"]

player = Player(50, 50)
inimigo = Inimigo(200, 200)
pontos = 0
pontos_inimigo = 0

#almento de proporçao_player
#acada ponto ganha 10% a mais em todos os atributos
def almento_proporcao_player():
    global pontos
    patamares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Patamares de pontos
    aumento = 0.1  # Aumento de 10%
    
    if pontos in patamares:
        player.hp += int(player.hp * aumento)
        player.atk += int(player.atk * aumento)
        player.defense += int(player.defense * aumento)
        player.renger += int(player.renger * aumento)
        player.intervalo_tiro -= int(player.intervalo_tiro * aumento)


def almento_proporcao_inimigo():
    global pontos_inimigo
    patamares = [1, 2, 3, 4, 5]  # Patamares de pontos
    aumento = 0.1  # Aumento de 10%

    if pontos_inimigo in patamares:
        inimigo.hp += int(inimigo.hp * aumento)
        inimigo.velocidade += int(inimigo.velocidade * aumento)



if __name__ == "__main__":
    screen, fps = janela()
    clock = pygame.time.Clock()
    prioridade_janela()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #subprocess.Popen(["python", "Game/Game.py"])
                    sys.exit()

        player.mover(5, 5)  # Movimentação do jogador
        player.limite_tela(screen.get_size())  # Limitar o movimento do jogador

        player.tiro(inimigo, screen)  # Verifica e cria projéteis
        screen.fill((0, 0, 0))
        
        # Player
        player.desenhar(screen)
        player.renge(screen)
        if player.atualizar_projetis(inimigo, screen):
            # Randomizar posição do inimigo
            random_x = random.randint(0, screen.get_width() - inimigo.largura)
            random_y = random.randint(0, screen.get_height() - inimigo.altura)
            inimigo = Inimigo(random_x, random_y)
            pontos += 1  # Incrementar pontos
            almento_proporcao_player()
            almento_proporcao_inimigo()

            

        # Inimigo
        inimigo.desenhar(screen)
        inimigo.mover_player(player, inimigo.velocidade)  # Movimentação do inimigo
        inimigo.limite_tela(screen.get_size())  # Limitar o movimento do inimigo

        if inimigo.dano(player):
            # Randomizar posição do inimigo
            random_x = random.randint(0, screen.get_width() - inimigo.largura)
            random_y = random.randint(0, screen.get_height() - inimigo.altura)
            player = Player(random_x, random_y)
            pontos = 0  # Reseta pontos do jogador
            pontos_inimigo += 1  # Incrementa pontos do inimigo
            almento_proporcao_inimigo()
        
        labeis = [
            Label(10, 10, f"Player HP: {player.hp}"),
            Label(10, 30, f"Inimigo HP: {inimigo.hp}"),
            Label(10, 50, f"Pontos: {pontos}"),
            Label(10, 70, f"Player Atk: {player.atk}"),
            Label(10, 90, f"Player Defense: {player.defense}"),
            Label(10, 110, f"Player Renger: {player.renger}"),
            Label(10, 130, f"Player Intervalo Tiro: {player.intervalo_tiro}"),
            Label(10, 150, f"Inimigo Velocidade: {inimigo.velocidade}")
        ]
        for label in labeis:
            label.draw(screen)
        pygame.display.flip()
        clock.tick(fps)  # Aplica o controle de FPS

    pygame.quit()
