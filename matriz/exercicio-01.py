
def inverter_lista(lista):
  lista_invertida = []
  indice = len(lista) - 1

  while indice >= 0:
    lista_invertida.append(lista[indice])
    indice -= 1

  return lista_invertida

def main():
  minha_lista = [5, 3, 5, 6, 7, 3]
  lista_invertida = inverter_lista(minha_lista)

  print("> Lista Original ", minha_lista)
  print("> Lista Invertida ", lista_invertida)

main()