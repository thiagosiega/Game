import os
import shutil

def desistalar():
    # Diretórios a serem removidos
    programa = "main.py"
    files = ["Game", "Instalacao"]
    
    # Bibliotecas a serem desinstaladas
    bibliotecas = ["pygame", "pywinauto"]

    # Remover diretórios especificados
    for file in files:
        if os.path.exists(file):
            shutil.rmtree(file, ignore_errors=True)
            print(f"Desinstalando {file}...")
        else:
            print(f"O diretório {file} não existe ou já foi removido.")

    # Desinstalar bibliotecas especificadas
    for biblioteca in bibliotecas:
        os.system(f"pip uninstall {biblioteca} -y")
        print(f"Desinstalando {biblioteca}...")
    
    # Remover o arquivo principal
    if os.path.exists(programa):
        os.remove(programa)
        print(f"Desinstalando {programa}...")
    else:
        print(f"O arquivo {programa} não existe ou já foi removido.")

    print("Desinstalação concluída com sucesso!")

if __name__ == "__main__":
    desistalar()
