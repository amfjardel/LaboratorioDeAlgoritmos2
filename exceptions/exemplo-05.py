def input_int(mensagem):
  while True:
    try:
      value = int(input(mensagem))
      return value
    except ValueError:
      print("[ERROR] O valor digitado não é um número válido")


def main():
  num_01 = input_int("> Digite o primeiro número: ")
  num_02 = input_int("> Digite o segundo número: ")

  resultado = num_01 + num_02

  print(resultado)

main()