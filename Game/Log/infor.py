import json
from datetime import datetime

# Formatação segura para o nome do arquivo de log
data = datetime.now().strftime("%Y-%m-%d")
file_path = f"Game/Log/Log_{data}.txt"
quebra = "------------------------------------------------------------------------------------------------------------------------"

FILE_LISTA_ERRO = "Game/Log/Erros.json"

def get_erro():
    with open(FILE_LISTA_ERRO, "r", encoding="utf-8") as file:
        return json.load(file)


def pesquisa_erro(id):
    erros = get_erro()
    for erro in erros["Codigos de erros"]:
        if erro["ID"] == id:
            return erro.get("Infor", {})
    return {}


def salvar_erro(erro):
    erro_info = pesquisa_erro(erro)
    print(erro_info)
    erro_descricao = erro_info.get('Descrição', 'Descrição não disponível')
    erro_mensagem = erro_info.get('Erro', 'Erro desconhecido')
    
    with open(file_path, "a") as file:
        file.write(f"\n{quebra}\n")
        file.write(f"Erro: {erro_mensagem}\n")
        file.write(f"Descrição: {erro_descricao}\n")
        file.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"{quebra}\n")


class Log:
    def __init__(self, id):
        self.id = id

    def pesquisa(self):
        return pesquisa_erro(self.id)

    def salvar(self):
        salvar_erro(self.id)
