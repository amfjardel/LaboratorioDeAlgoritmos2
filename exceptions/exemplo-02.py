
def dividir(num_01, num_02):
  try:
    resultado = num_01 / num_02
    return resultado
  except ZeroDivisionError:
    print("[ERRO] Você não pode dividir um valor por ZERO!")
    raise

def main():
  try:
    num_01 = int(input("> Digite o primeiro número: "))
    num_02 = int(input("> Digite o segundo número: "))

    resultado = dividir(num_01, num_02)

    print(f"O resultado da divisão é: {resultado}")
  except ValueError:
    print("[ERROR] O valor informado não é um número válido!")
  except BaseException as erro:
    print(f"[ERROR] Ocorreu um erro inesperado: {erro}")

# main()
dividir(5, 0)