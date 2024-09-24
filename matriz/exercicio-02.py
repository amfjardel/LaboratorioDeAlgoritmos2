
def somar_matriz(matriz_um, matriz_dois):
  matriz_soma = []

  for linha in range(len(matriz_um)):
    lista_soma = []

    for coluna in range(len(matriz_um[linha])):
      resultado_soma = matriz_um[linha][coluna] + matriz_dois[linha][coluna]
      lista_soma.append(resultado_soma)
    
    matriz_soma.append(lista_soma)

  return matriz_soma




def main():
  matriz_01 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ]

  matriz_02 = [
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
  ]

  resultado = somar_matriz(matriz_01, matriz_02)

  print("Resultado...", resultado)


main()