dicionario = {
  'a': 10,
  'b': 20,
  'c': 30
}

valor = int(input("Digite um valor: "))

# [10, 20, 30]
if valor in dicionario.values():
  print("O valor está presente no dicionário")
else:
  print("O valor NÃO está presente no dicionário")