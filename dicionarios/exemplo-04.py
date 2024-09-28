
dicionario = {
  'Maça': 1,
  'Banana': 3
}

print(dicionario.get('Banana'))
print(dicionario.get('Banana', 'Banana não existe'))
print(dicionario.get('Abacaxi'))
print(dicionario.get('Abacaxi', 'Abacaxi não existe'))

chave = input("Digite uma chave: ")
print(dicionario.get(chave, "Chave não existe"))

# print(dicionario['Abacaxi'])