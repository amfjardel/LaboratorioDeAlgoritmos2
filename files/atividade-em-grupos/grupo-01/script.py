''' 1. Crie um arquivo contendo uma lista de números separados por vírgulas. Escreva
um programa que lê esses números do arquivo e calcula a média deles. '''
import random


def escrever_arquivo():
    try:
        numeros = []
        for i in range(10):
            numeros.append(str(random.randint(0, 100)))
        file = open('files/atividade-em-grupos/grupo-01/numeros.txt', 'w')
        file.write(', '.join(numeros))
        file.close()
    except ValueError:
        print('Valor inválido. Digite um número inteiro.')
    except Exception as e:
        print(f"Ocorreu um erro inesperado")


def calcular_media():
    try:
        file = open('files/atividade-em-grupos/grupo-01/numeros.txt', 'r')
        numeros = file.read().split(', ')
        file.close()
        soma = 0
        for numero in numeros:
            soma += int(numero)
        return print(f'A média é de:{soma / len(numeros)}')
    except ZeroDivisionError:
        print("Erro: Não há números para calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado")
    
def main():
    escrever_arquivo()
    calcular_media()

main()

