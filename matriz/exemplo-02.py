# Escreva uma função que recebe uma matriz e um valor como entrada e 
# verifica se o valor está presente na matriz.

def buscar_valor_em_matriz(matriz, valor):
  numero_existe = False

  for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
      # matriz[linha][coluna] -> Isso armazena o valor em questão
      if matriz[linha][coluna] == valor:
        numero_existe = True

  if numero_existe:
    print("O número está presente na matriz!")
  else:
    print("O número não está presente na matriz!")


matriz = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
]

buscar_valor_em_matriz(matriz, 35)