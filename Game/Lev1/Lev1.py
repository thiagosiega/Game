import pygame
import os
import json
import sys
import random
import subprocess

# Adicione o caminho antes das importações
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Player.Player import Player
from Inimigos.Inimigo import Inimigo
from GUI.Foco_janela import FocoJanela
from GUI.Label import Label
from GUI.Img import Imgs

pygame.init()

def prioridade_janela():
    janela = FocoJanela("Lev1")
    janela.foco_janela()

def carregar_configuracoes():
    file = "Game/Config/Config.json"
    if os.path.exists(file):
        with open(file, "r") as f:
            configuracoes = json.load(f)
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

def criar_inimigos(qtd, screen):
    inimigos = []
    # se a lista estiver vazia, cria a qunatidade de inimigos deacordo com os pontos
    if screen:
        info = pygame.display.Info()
        for _ in range(qtd):
            random_x = random.randint(0, info.current_w - 50)
            random_y = random.randint(0, info.current_h - 50)
            inimigos.append(Inimigo(random_x, random_y))
    return inimigos

def aumento_proporcao_player():
    global pontos
    patamares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Patamares de pontos
    aumento = 0.1  # Aumento de 10%
    
    if pontos in patamares:
        player.hp += int(player.hp * aumento)
        player.atk += int(player.atk * aumento)
        player.defense += int(player.defense * aumento)
        player.renger += int(player.renger * aumento)
        player.intervalo_tiro -= int(player.intervalo_tiro * aumento)

def aumento_proporcao_inimigo():
    global pontos_inimigo
    patamares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Patamares de pontos
    aumento = 0.1  # Aumento de 10%

    if pontos_inimigo in patamares:
        for inimigo in inimigo_lista:
            inimigo.hp += int(inimigo.hp * aumento)
            inimigo.velocidade += int(inimigo.velocidade * aumento)

if __name__ == "__main__":
    screen, fps = janela()
    clock = pygame.time.Clock()
    prioridade_janela()
    running = True

    player = Player(50, 50)
    pontos = 1
    pontos_inimigo = 0
    inimigo_lista = criar_inimigos(pontos, screen) 
    img = "Game/Img/Fundo_Lev1.jpg"
    fundo = Imgs(img, screen.get_width(), screen.get_height(), 0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        

        player.mover(5, 5)  # Movimentação do jogador
        player.limite_tela(screen.get_size())  # Limitar o movimento do jogador

        player.tiro(inimigo_lista, screen)  # Verifica e cria projéteis
        screen.fill((0, 0, 0))
        fundo.desenhar_imagem(screen)
        
        # Player
        player.desenhar(screen)
        player.renge(screen)
        if player.atualizar_projetis(inimigo_lista, screen):
            pontos += 1  # Incrementar pontos
            pontos_inimigo += 1  # Incrementar pontos do inimigo
            aumento_proporcao_player()
            aumento_proporcao_inimigo()
            #se a lista de inimigos estiver vazia, cria a quantidade de inimigos de acordo com os pontos
            if len(inimigo_lista) == 0:
                inimigo_lista = criar_inimigos(pontos, screen)
                pontos_inimigo += pontos

            
            # Remover o inimigo derrotado
            inimigos_para_remover = [inimigo for inimigo in inimigo_lista if inimigo.hp <= 0]
            try:
                inimigo_lista.remove(inimigos_para_remover[0])
            except IndexError:
                pass

        # Inimigo
        if len(inimigo_lista) == 0:
            inimigo_lista = criar_inimigos(pontos, screen)
            pontos_inimigo += pontos
        for inimigo in inimigo_lista:
            inimigo.mover_player(player, inimigo.velocidade)
            inimigo.limite_tela(screen.get_size())
            inimigo.desenhar(screen)
            inimigo.colidir_player(player)
            #colidir com inimigos
            for inimigo2 in inimigo_lista:
                if inimigo != inimigo2:
                    inimigo.colidir_inimigo(inimigo2)

        # Labels
        labeis = [
            Label(10, 10, f"Player HP: {player.hp}"),
            Label(10, 30, f"Inimigo HP: {', '.join(str(inimigo.hp) for inimigo in inimigo_lista)}"),
            Label(10, 50, f"Pontos: {pontos}"),
            Label(10, 70, f"Player Atk: {player.atk}"),
            Label(10, 90, f"Player Defense: {player.defense}"),
            Label(10, 110, f"Player Renger: {player.renger}"),
            Label(10, 130, f"Player Intervalo Tiro: {player.intervalo_tiro}"),
            Label(10, 150, f"Inimigo Velocidade: {', '.join(str(inimigo.velocidade) for inimigo in inimigo_lista)}"),
            Label(10, 170, f"Tiros: {len(player.projetis)}"),
            Label(10, 190, f"Tiros player: {player.tiros}"),
        ]
        for label in labeis:
            label.draw(screen)
        
        pygame.display.flip()
        clock.tick(fps)  # Aplica o controle de FPS

    pygame.quit()
