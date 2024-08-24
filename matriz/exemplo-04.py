def soma(matriz):
    soma = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            soma += matriz[linha][coluna]

    print("A soma de todos os valores da matriz é: ", soma)

def main():
    matriz = [ 
        [1, 2 ,3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18 ,19, 20],
        [21, 22, 23, 24, 25],
        ]
    
    soma(matriz)
    
main()