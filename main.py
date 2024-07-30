import os
import subprocess
import sys
from tkinter import messagebox
from Instalacao.Instalar import Instalar  
from Game.Log.infor import Log  

def main():
    subprocess.call(["python", "Game/Game.py"])

def instalar_dependencias():
    # Lista de dependências
    requisitos = ["pygame", "pywinauto"]
    messagebox.showinfo("Instalação", "Instalando dependências!\nAguarde...")
    # Instala as dependências
    instalacao = Instalar(requisitos)
    if not instalacao.Instalar():
        messagebox.showinfo("Instalação", "Oops! Algo deu errado!\nLeia o arquivo 'Log.txt' para mais informações!")
        # Informações do erro
        Log(1).salvar()
        sys.exit(1)
    else:
        # Pergunta se deseja abrir o jogo
        if messagebox.askyesno("Abrir", "Dependências instaladas\nDeseja abrir o jogo?"):
            main()

if __name__ == "__main__":
    file = "Instalacao/Instalaçao.txt"
    if not os.path.exists(file):
        instalar_dependencias()
    else:
        main()
