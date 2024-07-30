import pygame
import os
import json
import sys
import random

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
            return json.load(f)
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

def configurar_janela():
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
    if screen:
        info = pygame.display.Info()
        for _ in range(qtd):
            random_x = random.randint(0, info.current_w - 50)
            random_y = random.randint(0, info.current_h - 50)
            inimigos.append(Inimigo(random_x, random_y))
    return inimigos

def aumento_proporcao_player(pontos, player):
    if pontos % 5 == 0:
        player.atk += 5
        player.defense += 2
        player.renger += 10
        player.intervalo_tiro = max(1, pontos* 5)
        player.tiros += 1

def aumento_proporcao_inimigos(pontos, inimigos):
    if pontos % 5 == 0:
        for inimigo in inimigos:
            inimigo.hp += 5
            inimigo.velocidade += 1

def desenhar_labels(screen, player, inimigo_lista, pontos, fps):
    labels = [
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
        Label(10, 210, f"FPS: {fps}")
    ]
    for label in labels:
        label.draw(screen)

def main():
    screen, fps = configurar_janela()
    clock = pygame.time.Clock()
    tiros = 5
    prioridade_janela()
    running = True

    player = Player(400, 300, tiros)
    pontos = 5
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

        player.mover(10, 10)
        player.limite_tela(screen.get_size())
        player.tiro(inimigo_lista, screen)
        
        screen.fill((0, 0, 0))
        fundo.desenhar_imagem(screen)
        player.desenhar(screen)
        player.renge(screen)

        if player.atualizar_projetis(inimigo_lista, screen):
            pontos += 1
            pontos_inimigo += 1
            aumento_proporcao_player(pontos, player)
            aumento_proporcao_inimigos(pontos_inimigo, inimigo_lista)
            
            if not inimigo_lista:
                inimigo_lista = criar_inimigos(pontos, screen)
                pontos_inimigo += pontos

            inimigos_para_remover = [inimigo for inimigo in inimigo_lista if inimigo.hp <= 0]
            for inimigo in inimigos_para_remover:
                inimigo_lista.remove(inimigo)

        if not inimigo_lista:
            inimigo_lista = criar_inimigos(pontos, screen)
            pontos_inimigo += pontos

        for inimigo in inimigo_lista:
            inimigo.mover_player(player, inimigo.velocidade)
            inimigo.limite_tela(screen.get_size())
            inimigo.desenhar(screen)
            inimigo.colidir_player(player)
            for inimigo2 in inimigo_lista:
                if inimigo != inimigo2:
                    inimigo.colidir_inimigo(inimigo2)

        desenhar_labels(screen, player, inimigo_lista, pontos, fps)
        
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()
