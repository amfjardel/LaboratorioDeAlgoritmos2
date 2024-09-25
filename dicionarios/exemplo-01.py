def main():
  usuarios = {
    "nome": "Felipe",
    "cidade": "Santa Maria"
  }

  usuarios["nome"] = input("Digite seu nome: ")
  usuarios["idade"] = int(input("Digite sua idade: "))

  print("\n# Dados do usuário:")

  print("> Nome:", usuarios["nome"])
  print("> Idade:", usuarios["idade"])
  print("> Cidade:", usuarios["cidade"])

main()