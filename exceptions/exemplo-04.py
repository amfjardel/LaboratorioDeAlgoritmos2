class NegativeValueError(Exception):
  pass

def main():
  try:
    valor = int(input("> Digite um número POSITIVO: "))

    if valor < 0:
      raise NegativeValueError("negative value")

    print(f"O número é: {valor}")
  except NegativeValueError:
    print("[ERROR] O número deve ser positivo!")
  except BaseException as erro:
    print(f"[ERROR] Ocorreu um erro: {erro}")


main()