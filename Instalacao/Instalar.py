import datetime
import os
import subprocess
import sys
from tkinter import messagebox
from Game.Log.infor import Log

class Instalar:
    def __init__(self, requisitos):
        self.requisitos = requisitos

    def instalar(self):
        requisitos_instalados = []
        erros = []

        for requisito in self.requisitos:
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", requisito], check=True)
                requisitos_instalados.append(requisito)
                messagebox.showinfo("Instalação", f"{requisito} instalado com sucesso.")
            except subprocess.CalledProcessError as e:
                erros.append(f"Erro ao instalar {requisito}: {e}")
                Log(2).salvar(f"Erro ao instalar {requisito}: {e}")

        if erros:
            messagebox.showerror("Erro", "\n".join(erros))
        else:
            # Verificar se o diretório 'Instalacao' existe, se não, criar
            if not os.path.exists("Instalacao"):
                os.makedirs("Instalacao")
            
            # Criar o arquivo de instalação com mais informações
            with open("Instalacao/instalar.txt", "w") as file:
                file.write(f"Data da instalação: {datetime.now()}\n")
                file.write(f"Requisitos instalados: {', '.join(requisitos_instalados)}\n")

        return requisitos_instalados, erros
