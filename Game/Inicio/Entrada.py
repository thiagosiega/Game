import os
import sys
import json
import subprocess
import tkinter as tk

from tkinter import messagebox

# Adiciona o diretório "Game" ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora o import deve funcionar
from Pecados.Saves import Saives
from Log.infor import Log

# Verifica se o diretório de saves existe
FILE_SAVES = "Saves/"
if not os.path.exists(FILE_SAVES):
    os.makedirs(FILE_SAVES)

# Função para listar todos os arquivos no diretório de saves
def listar_arquivos():
    arquivos = os.listdir(FILE_SAVES)
    Padrao = ["Novo_jogo.json"]

    # Se houver apenas o arquivo de continuar
    if arquivos == Padrao:
        janela = tk.Tk()
        janela.title("Novo Jogo")
        janela.geometry("400x200")
        janela.resizable(False, False)

        #da janela para frente
        janela.attributes("-topmost", True)
        def salvar():
            dados_padrao = {
                "Nome": entradas[0].get(),
                "Vida": 100,
                "Mana": 100,
                "Items": [],
                "Cap": 1,
                "Tex_vez": "1",
            }
            Saives({}).salvar(dados_padrao)
            janela.destroy()
            cap = dados_padrao["Cap"]
            nome = dados_padrao["Nome"]
            file_path = f"Game/Caps/Cap_{cap}/main.py"
            if os.path.exists(file_path):
                try:
                    subprocess.run(["python", file_path, nome])
                except Exception as e:
                    Log(12, str(e)).salvar()  # Passar a mensagem de erro
            else:
                Log(12, f"Arquivo não encontrado: {file_path}").salvar()  # Mensagem específica para o arquivo não encontrado

        labeis = ["Nome"]
        entradas = []
        for i in range(len(labeis)):
            tk.Label(janela, text=labeis[i]).grid(row=i, column=0)
            entradas.append(tk.Entry(janela))
            entradas[i].grid(row=i, column=1)
        
        tk.Button(janela, text="Salvar", command=salvar).grid(row=len(labeis), column=0, columnspan=2)
        janela.mainloop()
        
    else:
        resposta = tk.messagebox.askyesno("Multiplos Saves", "Escolha um save para continuar")
        if resposta:
            janela = tk.Tk()
            janela.title("Continuar")
            janela.geometry("400x200")

            def ler_save(arquivos):
                btns = []
                for arquivo in arquivos:
                    if arquivo != "Continuar.json":
                        nome = arquivo.split(".")[0]
                        def carregar_save(arquivo=arquivo):
                            if arquivo != "Novo_jogo.json":
                                with open(FILE_SAVES + arquivo, "r") as file:
                                    dados = json.load(file)
                                    cap = dados["Cap"]
                                    nome = dados["Nome"]
                                    file_path = f"Game/Caps/Cap_{cap}/main.py"
                                    if os.path.exists(file_path):
                                        try:
                                            subprocess.run(["python", file_path, nome])
                                            janela.destroy()
                                        except Exception as e:
                                            Log(12, str(e)).salvar()
                                    else:
                                        Log(12, f"Arquivo não encontrado: {file_path}").salvar()
                            else:
                                janela = tk.Tk()
                                janela.title("Novo Jogo")
                                janela.geometry("400x200")
                                janela.resizable(False, False)

                                #da janela para frente
                                janela.attributes("-topmost", True)
                                def salvar():
                                    dados_padrao = {
                                        "Nome": entradas[0].get(),
                                        "Vida": 100,
                                        "Mana": 100,
                                        "Items": [],
                                        "Cap": 1,
                                        "Tex_vez": "1",
                                    }
                                    Saives({}).salvar(dados_padrao)
                                    janela.destroy()
                                    cap = dados_padrao["Cap"]
                                    nome = dados_padrao["Nome"]
                                    file_path = f"Game/Caps/Cap_{cap}/main.py"
                                    if os.path.exists(file_path):
                                        try:
                                            subprocess.run(["python", file_path, nome])
                                        except Exception as e:
                                            Log(12, str(e)).salvar()  # Passar a mensagem de erro
                                    else:
                                        Log(12, f"Arquivo não encontrado: {file_path}").salvar()  # Mensagem específica para o arquivo não encontrado

                                labeis = ["Nome"]
                                entradas = []
                                for i in range(len(labeis)):
                                    tk.Label(janela, text=labeis[i]).grid(row=i, column=0)
                                    entradas.append(tk.Entry(janela))
                                    entradas[i].grid(row=i, column=1)
                                
                                tk.Button(janela, text="Salvar", command=salvar).grid(row=len(labeis), column=0, columnspan=2)
                                janela.mainloop()
                                
                        btn = tk.Button(janela, text=nome, command=lambda a=arquivo: carregar_save(a))
                        btns.append(btn)
                return btns

            label = tk.Label(janela, text="Escolha um save:")
            label.pack()
            btns = ler_save(arquivos)
            for btn in btns:
                btn.pack()
            
            janela.mainloop() 
        else:
            messagebox.showinfo("Erro", "Celecine a opção de Novo Jogo")  


listar_arquivos()
