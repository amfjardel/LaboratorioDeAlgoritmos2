dicionario_vogais = {}
lista_de_vogais = ['a', 'e', 'i', 'o', 'u']

frase = "O rato roeu a roupa do rei de Roma"
frase = frase.lower()

for letra in frase:
  if letra in lista_de_vogais:
    dicionario_vogais[letra] = dicionario_vogais.get(letra, 0) + 1

    # if letra in dicionario_vogais:
    #   dicionario_vogais[letra] += 1
    # else:
    #   dicionario_vogais[letra] = 1

print(dicionario_vogais)