import os
import subprocess
import sys

from tkinter import messagebox
from Instalacao.Instalar import Instalar  
from Game.Log.infor import Log  

def main():
    messagebox.showinfo("Jogo", "Iniciando o jogo!")
    subprocess.call(["python", "Game/Game.py"])

def instalar_dependencias():
    requisitos = ["pygame", "pywinauto"]
    messagebox.showinfo("Instalação", "Instalando dependências!\nAguarde...")
    instalacao = Instalar(requisitos)
    if not instalacao.instalar():  # Corrigido para chamar o método correto
        messagebox.showinfo("Instalação", "Oops! Algo deu errado!\nLeia o arquivo 'Log.txt' para mais informações!")
        Log(1).salvar()
        sys.exit(1)
    else:
        if messagebox.askyesno("Abrir", "Dependências instaladas\nDeseja abrir o jogo?"):
            main()

if __name__ == "__main__":
    file = "Instalacao/instalar.txt"
    messagebox.showinfo("Instalação", "Verificando dependências!")
    if not os.path.exists(file):
        instalar_dependencias()
        messagebox.showinfo("Instalação", "Instalação concluída com sucesso!")
    else:
        messagebox.showinfo("Instalação", "Dependências já instaladas!")
        main()
