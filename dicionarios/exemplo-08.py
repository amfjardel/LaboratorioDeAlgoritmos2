
# contatos = {
#   'Jardel': ['55999090238', '4499999999']
# }

contatos = {}

while True:
  print("=-=-= BEM-VINDO =-=-=")
  nome = input("> Digite seu nome: ")

  if not nome:
    break

  contatos[nome] = []

  while True:
    celular = input("> Digite seu celular: ")

    if not celular:
      break
    
    contatos[nome].append(celular)

  print(contatos)


for chave in contatos:
  print(f"> Nome: {chave}")
  
  for i in range(len(contatos[chave])):
    print(f"\t {i + 1} - {contatos[chave][i]}")