import sys
import os
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Agora o import deve funcionar
from Pecados.Saves import Saives
from Log.infor import Log


# verifica se resebeu a variavel nome
if len(sys.argv) == 2:
    nome = sys.argv[1]
    carregar = Saives({}).carregar(nome)
    if carregar:
        nome, vida, mana, itens, cap, tex_vez, config = Saives({}).infor_dados(carregar)
        print(f"Nome: {nome}\nVida: {vida}\nMana: {mana}\nItens: {itens}\nCap: {cap}\nTex_vez: {tex_vez}\nConfig: {config}")
    else:
        Log(4).salvar()
        messagebox.showinfo("Erro", "Consulte a pasta Game/Log para mais informações!")

else:
    Log(4).salvar()
    messagebox.showinfo("Erro", "Consulte a pasta Game/Log para mais informações!")
    