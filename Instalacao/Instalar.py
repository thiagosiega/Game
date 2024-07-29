import sys
import os

from tkinter import messagebox
from Game.Log.infor import Log


class Instalar:
    def __init__(self, Requisitos):
        self.Requisitos = Requisitos
        self.Instalacao = False

    def Instalar(self):
        for Requisito in self.Requisitos:
            try:
                os.system(f"pip install {Requisito}")
                #verifica se o requisito foi instalado
                if os.system(f"pip show {Requisito}") != 0:
                    Log(5).salvar()
                    raise Exception("Requisito não instalado")
                messagebox.showinfo("Instalação", f"{Requisito} instalado com sucesso.")
                #cria o arquivo de instalação
                with open("Instalacao/Instalaçao.txt", "w") as file:
                    file.write("Instalado")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao instalar o requisito {Requisito}: {e}")
                Log(2).salvar()
                self.Instalacao = False
                return self.Instalacao
        self.Instalacao = True
        return self.Instalacao
    
    def Desinstalar(self):
        for Requisito in self.Requisitos:
            try:
                os.system(f"pip uninstall -y {Requisito}")
                messagebox.showinfo("Desinstalação", f"{Requisito} desinstalado com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao desinstalar o requisito {Requisito}: {e}")
                Log(3).salvar()
                self.Instalacao = True
                return self.Instalacao
        self.Instalacao = False
        return self.Instalacao
