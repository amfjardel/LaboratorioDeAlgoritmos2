def main():
  try:
    valor = int(input("> Digite um número POSITIVO: "))

    if valor < 0:
      raise ValueError("negative value")

    print(f"O número é: {valor}")
  except BaseException as erro:
    print(f"[ERROR] Ocorreu um erro: {erro}")


main()