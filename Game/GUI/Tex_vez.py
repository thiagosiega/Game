import json
import os

class Text_exibir:
    def __init__(self, cap, tex_vez):
        self.cap = cap
        self.tex_vez = tex_vez
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório atual do script
        self.FILE_TEXTO = os.path.join(base_dir, f"../Caps/Cap_{cap}/Text.json")
    
    def ler_texto(self):
        if not os.path.exists(self.FILE_TEXTO):
            return f"Erro: O arquivo {self.FILE_TEXTO} não foi encontrado."
        
        try:
            with open(self.FILE_TEXTO, 'r', encoding='utf-8') as f:
                return json.load(f)
        except IOError as e:
            return f"Erro ao ler o arquivo: {e}"
        except json.JSONDecodeError as e:
            return f"Erro ao decodificar o JSON: {e}"
    
    def exibir_texto(self):
        texto = self.ler_texto()
        if isinstance(texto, str):
            return texto  # Retorna a mensagem de erro
        return texto.get(self.tex_vez, "Texto não encontrado")