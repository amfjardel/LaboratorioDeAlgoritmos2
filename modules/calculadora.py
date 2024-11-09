from modules.menu import menu
from modules.obter_valores import obter_ints
import soma

def main():
  while True:
    opcao = menu()

    if opcao == 1:
      val1, val2 = obter_ints()
      resultado = soma.somar(val1, val2)
      print(f"Resultado da soma: {resultado}")
    elif opcao == 5:
      break


main()