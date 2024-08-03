import sys
import os
import pygame
from tkinter import messagebox

# Adiciona o caminho do diretório superior à lista de caminhos do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Pecados.Saves import Saives
from Log.infor import Log
from GUI.Tex_vez import Text_exibir
from GUI.Box_tex import Box_texto

def exibir_erro(codigo_erro, mensagem):
    Log(codigo_erro).salvar()
    messagebox.showinfo("Erro", mensagem)

# Verifica se recebeu a variável nome
"""
# Para facilitar os testes, o código foi comentado
if len(sys.argv) == 2:
    nome = sys.argv[1]
    salvar = Saives({})
    carregar = salvar.carregar(nome)
    if carregar:
        nome, vida, mana, itens, cap, tex_vez, config = salvar.infor_dados(carregar)
    else:
        exibir_erro(4, "Consulte a pasta Game/Log para mais informações!")
else:
    pass
"""

def game():
    cap = 1
    tex_vez = "1"
    
    pygame.init()
    pygame.font.init()
    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jogo")
    clock = pygame.time.Clock()
    fonte = pygame.font.Font(None, 32)

    box_texto = Box_texto(60, 20, (0, 0, 0), tela, fonte, "", 20, 500, (255, 255, 255), 32)    
    
    while True:
        texto_obj = Text_exibir(cap, tex_vez)
        texto = texto_obj.exibir_texto()
        box_texto.atualizar_texto(texto)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    # Exibe o próximo texto
                    tex_vez = str(int(tex_vez) + 1)
                    texto = texto_obj.exibir_texto()
                    box_texto.atualizar_texto(texto)
        pygame.display.update()
        clock.tick(60)  # Limita a 60 quadros por segundo

if __name__ == "__main__":
    game()
