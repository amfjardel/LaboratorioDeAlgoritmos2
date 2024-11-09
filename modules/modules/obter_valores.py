def obter_ints():
  """Método que obtém dois valores inteiros e retorno. Caso ocorra algum erro, ele solicita novamente"""
  while True:
    try:
      val1 = int(input("> Digite o primeiro valor: "))
      val2 = int(input("> Digite o segundo valor: "))

      return val1, val2
    except ValueError:
      print("[ERROR] Você digitou um valor inválido!\n")