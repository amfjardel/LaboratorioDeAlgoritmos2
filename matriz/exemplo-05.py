from random import randint

def gerar_matriz_aleatoria(tamanho = 3):
  matriz = []

  for linha in range(tamanho):
    lista_temporaria = []

    for coluna in range(tamanho):
      valor = randint(0, 100)
      lista_temporaria.append(valor)

    matriz.append(lista_temporaria)

  return matriz

def mostrar_matriz(matriz):
  for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
      print(matriz[linha][coluna], end="\t")
    print("")

nova_matriz = gerar_matriz_aleatoria(5)

mostrar_matriz(nova_matriz)