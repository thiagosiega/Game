import pygame
import os
import sys
import subprocess

from tkinter import messagebox
from pywinauto import Application
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
                messagebox.showinfo("!", "Você irá se arrepender!")
                pygame.quit()
                sys.exit()
            else:
                messagebox.showinfo("!", "Acho bom!")
                # Foca a janela do pygame
                focojanela = FocoJanela("Game")
                focojanela.foco_janela()
        if texto == "Iniciar":
            subprocess.Popen(["python", "Game/Lev1/Lev1.py"])
            sys.exit()
            

