def main():
  dicionario = {}

  while True:  
    chave_informada = input("Informe uma chave para seu dicionario: ")

    if not chave_informada:
      break

    valor_informado = input("Informe um valor para seu dicionario: ")

    dicionario[chave_informada] = valor_informado

    print(dicionario)


main()