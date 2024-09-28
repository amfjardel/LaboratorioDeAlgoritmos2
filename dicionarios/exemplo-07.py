# contatos = {
#   'Jardel': {
#     'celular': '55999090239',
#     'email': 'jardelfelipeknirsch@gmail.com'
#   }
# }

def formato_01():
  contatos = {}

  print("=-=-= Bem-vindo =-=-=")
  nome = input("> Digite seu nome: ")
  # { 'Jardel': {} }
  # contatos['Jardel']
  contatos[nome] = {}

  contatos[nome]['celular'] = input('> Digite o número do celular do contato: ')
  contatos[nome]['email'] = input('> Digite o número do celular do contato: ')

  print(contatos)


# Segundo formato

contatos = {}

print("=-=-= Bem-vindo =-=-=")
nome = input("> Digite seu nome: ")
celular_informado = input("> Digite o celular do contato: ")
email_informado = input("> Digite o e-mail do contato: ")

contatos[nome] = {
  'celular': celular_informado,
  'email': email_informado
}

print(contatos)