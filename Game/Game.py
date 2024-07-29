import pygame
import os
import json
import subprocess
import sys


from tkinter import messagebox
from Log.infor import Log
from GUI.Botoes import Botoes


# Verificação e execução do script de instalação, se necessário
try:
    file = "Instalacao/Instalaçao.txt"
    if not os.path.exists(file):
        messagebox.showinfo("Instalação", "Upis algo deu errado!\nSo um minuto estamos resolvendo!")
        #informaçoes do erro!
        Log(4).salvar()
        subprocess.Popen(["python", "main.py"])
        sys.exit()
except Exception as e:
    print(f"Erro ao verificar ou executar o script de instalação: {e}")
    sys.exit()

# Função para carregar as configurações do jogo
def carregar_configuracoes():
    caminho_config = "Game/Config/Config.json"
    if os.path.exists(caminho_config):
        with open(caminho_config, "r") as file:
            configuracoes = json.load(file)
    else:
        configuracoes = {
            "resolucao": [800, 600],
            "fullscreen": False
        }
        os.makedirs(os.path.dirname(caminho_config), exist_ok=True)
        with open(caminho_config, "w") as file:
            json.dump(configuracoes, file)
    return configuracoes

# Função para definir a janela do jogo
def janela():
    pygame.init()
    configuracoes = carregar_configuracoes()
    fullscreen = configuracoes["fullscreen"]

    if fullscreen:
        info = pygame.display.Info()
        resolucao = (info.current_w, info.current_h)
        tela = pygame.display.set_mode(resolucao, pygame.FULLSCREEN)
    else:
        resolucao = configuracoes["resolucao"]
        tela = pygame.display.set_mode(resolucao)
    
    pygame.display.set_caption("Game")
    return tela

# Função para garantir que a janela do jogo tenha prioridade
def prioridade_janela():
    try:
        os.system("wmctrl -r Game -b add,above")
    except Exception as e:
        Log(5).salvar()

texto = ["Iniciar", "Configurações", "Pecados", "Sair"]

if __name__ == "__main__":
    screen = janela()
    prioridade_janela()
    running = True

    # Criação dos botões fora do loop para evitar recriação desnecessária
    botoes = [Botoes(100, 100 + i * 50, 200, 40, (255, 0, 0), t) for i, t in enumerate(texto)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for botao in botoes:
                    if botao.rect.collidepoint(pos):
                        botao.acao(botao.texto)

        # Limpar a tela antes de desenhar os botões
        screen.fill((0, 0, 0))

        # Desenhar botões
        for botao in botoes:
            botao.desenhar(screen)
        
        pygame.display.flip()

    pygame.quit()
