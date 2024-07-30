import pygame
import os
import json
import sys
import subprocess


from tkinter import messagebox


# Adicione o caminho antes das importações
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Player.Player import Player
from Inimigos.Inimigo import Inimigo
from GUI.Foco_janela import FocoJanela

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
                    subprocess.Popen(["python", "Game/Game.py"])
                    sys.exit()

        player.mover(5, 5)  # Movimentação do jogador
        player.limite_tela(screen.get_size())  # Limitar o movimento do jogador

        player.tiro(inimigo, screen)  # Verifica e cria projéteis
        screen.fill((0, 0, 0))
        
        # Player
        player.desenhar(screen)
        player.renge(screen)
        if player.atualizar_projetis(inimigo, screen):
            # Se o inimigo é derrotado
            messagebox.showinfo("Vitória", "O player venceu!")
            subprocess.Popen(["python", "Game/Game.py"])
            sys.exit()

        # Inimigo
        inimigo.desenhar(screen)
        inimigo.mover_player(player)
        inimigo.limite_tela(screen.get_size())  # Limitar o movimento do inimigo

        if inimigo.dano(player):
            # Se o player é derrotado
            messagebox.showinfo("Game Over", "O inimigo venceu!")
            subprocess.Popen(["python", "Game/Game.py"])
            sys.exit()

        pygame.display.flip()
        clock.tick(fps)  # Aplica o controle de FPS

    pygame.quit()
