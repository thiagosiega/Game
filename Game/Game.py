import pygame
import os
import json
import subprocess
import sys


from tkinter import messagebox
from Log.infor import Log
from GUI.Botoes import Botoes
from GUI.Foco_janela import FocoJanela
from GUI.Img import Imgs

# Verificação e execução do script de instalação, se necessário
def verificar_instalacao():
    try:
        file = "Instalacao/Instalaçao.txt"
        if not os.path.exists(file):
            messagebox.showinfo("Instalação", "Algo deu errado!\nEstamos resolvendo!")
            # Informar erro e reiniciar o script
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
            "fullscreen": False,
            "FPS": 60
        }
        os.makedirs(os.path.dirname(caminho_config), exist_ok=True)
        with open(caminho_config, "w") as file:
            json.dump(configuracoes, file)
    return configuracoes

# Função para definir a janela do jogo
def criar_janela():
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
def garantir_prioridade_janela():
    try:
        focojanela = FocoJanela("Game")
        focojanela.foco_janela()
    except Exception as e:
        Log(5).salvar()

def main():
    verificar_instalacao()
    screen = criar_janela()
    garantir_prioridade_janela()

    texto = ["Iniciar", "Configurações", "Pecados", "Sair"]
    img = "Game/Img/Fundo_Game1.jpg"
    fundo_img = Imgs(img, screen.get_width(), screen.get_height(), 0, 0)

    # Criação dos botões fora do loop para evitar recriação desnecessária
    botoes = [Botoes(100, 100 + i * 50, 200, 40, (255, 0, 0), t) for i, t in enumerate(texto)]

    running = True
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

        # Limpar a tela e desenhar a imagem de fundo
        screen.fill((0, 0, 0))  # Preencher com preto antes de desenhar o fundo
        fundo_img.desenhar_imagem(screen)

        # Desenhar botões
        for botao in botoes:
            botao.desenhar(screen)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
