
clientes = []

while True:
  print("Bem-vindo :)")
  nome = input("> Digite o nome do cliente: ")

  if not nome:
    break

  sobrenome = input("> Sobrenome: ")
  idade = int(input("> Idade: "))

  pessoa = {
    "nome": nome,
    "sobrenome": sobrenome,
    "idade": idade
  }

  clientes.append(pessoa)

  print(clientes)



# Quero editar um cliente cadastrado
nome = input("> Digite o nome do cliente que você deseja editar: ")
encontrou = False

for i in range(len(clientes)):
  # clientes[i] -> { 'nome': 'Bla' }
  if clientes[i]['nome'] == nome:
    encontrou = True
    nova_idade = int(input("> Digite a nova idade: "))
    clientes[i]['idade'] = nova_idade

if encontrou == False:
  print(f"Não foi possível localizar o cliente {nome}")

print(clientes)