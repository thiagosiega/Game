import pygame
import os
import sys
import subprocess
from tkinter import messagebox
from Log.infor import Log
from GUI.Foco_janela import FocoJanela

class Botoes:
    def __init__(self, x, y, largura, altura, cor, texto):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.texto = texto
        self.fonte = pygame.font.SysFont(None, 20)
        self.rect = pygame.Rect(x, y, largura, altura)  # Adiciona o retângulo para colisão

    def desenhar(self, tela):
        """
        Função para desenhar os botões na tela.
        tipo de entrada: pygame.Surface
        tipo de saída: None
        exemplo de entrada: pygame.display.set_mode((800, 600))
        exemplo de saída: None
        """
        pygame.draw.rect(tela, self.cor, self.rect)
        texto = self.fonte.render(self.texto, True, (0, 0, 0))
        tela.blit(texto, (self.x + self.largura / 2 - texto.get_width() / 2, self.y + self.altura / 2 - texto.get_height() / 2))

    def acao(self, texto):
        if texto == "Sair":
            # Pergunta se deseja sair
            if messagebox.askyesno("Sair", "Deseja sair?"):
                messagebox.showinfo("Saída", "Você irá se arrepender!")
                pygame.quit()
                sys.exit()
            else:
                messagebox.showinfo("Cancelado", "Acho bom!")
                # Foca a janela do pygame
                self.focar_janela()

        elif texto == "Iniciar":
            while True:
                try:
                    # Inicia o jogo e aguarda a conclusão
                    subprocess.run(["python", "Game/Lev1/Lev1.py"], check=True)
                    break
                except Exception as e:
                    print(f"Erro ao iniciar o jogo: {e}")
                    messagebox.showerror("Erro", f"Erro ao iniciar o jogo: {e}")
        
        elif texto == "Configurações":
            # Placeholder para configurações
            pass

    def focar_janela(self):
        """Método para focar a janela do Pygame usando pywinauto"""
        try:
            focojanela = FocoJanela("Game")
            focojanela.foco_janela()
        except Exception as e:
            Log(5).salvar()
            print(f"Erro ao focar a janela: {e}")

