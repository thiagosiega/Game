import sys
import pygame
import json

def carregar_configuracoes():
    FILE_CONFIG = "Game/Config/Config.json"
    try:
        with open(FILE_CONFIG, 'r') as arquivo:
            config = json.load(arquivo)
        return config
    except FileNotFoundError:
        raise Exception(f"Arquivo de configuração '{FILE_CONFIG}' não encontrado.")
    except json.JSONDecodeError:
        raise Exception(f"Erro ao decodificar o arquivo JSON '{FILE_CONFIG}'.")

def janela():
    pygame.init()
    configuracoes = carregar_configuracoes()
    
    # Acessando configurações com get() para evitar KeyError
    fullscreen = configuracoes.get("fullscreen", False)
    
    if fullscreen:
        info = pygame.display.Info()
        resolucao = (info.current_w, info.current_h)
        tela = pygame.display.set_mode(resolucao, pygame.FULLSCREEN)
    else:
        resolucao = configuracoes.get("resolucao", (800, 600))
        tela = pygame.display.set_mode(resolucao)
    
    pygame.display.set_caption("Game")
    return tela

def main():
    tela = janela()
    running = True  # Definindo a variável 'running' antes do loop principal
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(1)
