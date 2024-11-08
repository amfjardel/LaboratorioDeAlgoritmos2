#Grupo 5
#Nomes:Wellington Juan , Eduardo Gomes, Eduardo Barreto, Guilherme Losekann, Vinicius Krohn
def inverter_arquivo(nome_arquivo, arquivo_invertido):
    try:
        myfile = open(nome_arquivo, "r")
        linhas = myfile.readlines()
        myfile.close()
        
        linhas_invertidas = []

        for i in range(len(linhas)-1, -1, -1):
            linhas_invertidas.append(linhas[i])

        file_invertido = open("arquivo_saida.txt", "w")
        for linha in linhas_invertidas:
            file_invertido.write(linha)
        file_invertido.close()

        print(f"As linhas foram invertidas em '{arquivo_invertido}'.")

    except (FileNotFoundError, IOError, Exception):
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        '''
        FileNotFoundError: O arquivo 'exercicio5.txt' não foi encontrado.
        IOError: Quando tem problemas de ler ou escrever arquivos.
        Exception: Classe base para quase todas as exceções.
        '''

def main():
    nome_arquivo = 'files/atividade-em-grupos/grupo-05/exercicio5.txt'
    arquivo_invertido = 'files/atividade-em-grupos/grupo-05/arquivo_destino.txt'

    inverter_arquivo(nome_arquivo, arquivo_invertido)

main()