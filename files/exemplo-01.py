import random

def gerar_arquivo():
  arquivo = open("files/arquivos/teste.txt", "w")

  for i in range(50):
    numero_aleatorio = random.randint(0, 50)
    arquivo.write(str(numero_aleatorio))
    arquivo.write("\n")

  arquivo.close()

def ler_arquivo():
  arquivo = open("files/arquivos/teste.txt", "r")

  # print(arquivo.read())
  linhas = arquivo.readlines()

  print(f"> Quantidade de linhas: {len(linhas)}")

  for i in range(len(linhas)):
    print(f"Linha {i}: {linhas[i]}", end="")

def main():
  gerar_arquivo()
  ler_arquivo()

main()