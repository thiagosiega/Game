from tkinter import messagebox
import os
import json

class Saives:
    def __init__(self, dados):
        self.dados = dados
        self.caminho = "Saves/"
    
    def infor_dados(self, dados):
        nome = dados["Nome"]
        vida = dados["Vida"]
        mana = dados["Mana"]
        itens = dados["Items"]
        cap = dados["Cap"]
        tex_vez = dados["Tex_vez"]
        config = dados.get("Config", {})  # Usando .get() para evitar erro se "Config" não existir
        return nome, vida, mana, itens, cap, tex_vez, config

    def salvar(self, dados):
        nome_arquivo = os.path.join(self.caminho, dados["Nome"] + ".json")
        # Verifica se o diretório de saves existe
        if not os.path.exists(self.caminho):
            os.makedirs(self.caminho)

        # Verifica se o arquivo já existe
        if os.path.exists(nome_arquivo):
            if messagebox.askyesno("Substituir", f"Deseja substituir o arquivo '{nome_arquivo}'?"):
                with open(nome_arquivo, "w") as file:
                    json.dump(dados, file, indent=4)
                    messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")
            else:
                messagebox.showinfo("Cancelado", "Arquivo não foi salvo!")
        else:
            with open(nome_arquivo, "w") as file:
                json.dump(dados, file, indent=4)
                messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")

    def carregar(self, nome):
        nome_arquivo = os.path.join(self.caminho, nome + ".json")
        print(nome_arquivo)
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, "r") as file:
                dados = json.load(file)
                return dados
        else:
            messagebox.showinfo("Erro", "Arquivo não encontrado!")
            return None

    def deletar(self, nome):
        nome_arquivo = os.path.join(self.caminho, nome + ".json")
        if os.path.exists(nome_arquivo):
            if messagebox.askyesno("Deletar", f"Deseja deletar o arquivo '{nome_arquivo}'?"):
                os.remove(nome_arquivo)
                messagebox.showinfo("Deletado", "Arquivo deletado com sucesso!")
            else:
                messagebox.showinfo("Cancelado", "Arquivo não foi deletado!")
        else:
            messagebox.showinfo("Erro", "Arquivo não encontrado!")
