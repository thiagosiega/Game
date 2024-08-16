package main

import (
	"fmt"
	"os"
	"os/exec"
)

// Função para verificar se um arquivo existe
func isFile(filePath string) bool {
	info, err := os.Stat(filePath)
	if os.IsNotExist(err) {
		return false
	}
	return !info.IsDir()
}

func main() {
	filePath := "main.py"
	// Verifica se o arquivo é um arquivo e se existe
	if isFile(filePath) {
		// Executa o arquivo
		cmd := exec.Command("python", filePath)
		fmt.Println("Executando o script Python...")
		output, err := cmd.Output() // Corrige o erro de digitação: "outut" para "output"
		if err != nil {
			fmt.Println("Erro ao executar o script:", err)
			return
		}
		// Exibe a saída do script Python
		fmt.Println(string(output))
	} else {
		fmt.Println("O arquivo não existe")
	}
}
