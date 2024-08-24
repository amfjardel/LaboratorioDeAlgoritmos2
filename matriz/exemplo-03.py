
def Menor(matriz):
    numeromenor = matriz[0][0]
    for linha in range (len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] < numeromenor:
                numeromenor = matriz[linha][coluna]
    return numeromenor
                
matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def main():
    numeromenor = Menor(matriz)
    print("O menor numero da matriz é ",numeromenor)

main()