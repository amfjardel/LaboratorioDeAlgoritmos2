# 4. Utilizando dicionários, crie um programa que simule um caixa eletrônico. O usuário poderá optar pelas seguintes funcionalidades:

# Depositar dinheiro – Usuário pode depositar valor ilimitado, desde que seja positivo;
# Sacar dinheiro – Usuário pode sacar um valor limitado que deve ser validado pelo campo “transaction_limit”;
# Verificar saldo bancário – Usuário pode consultar o saldo atual;
# Histórico de movimentações – Usuário pode consultar todas as movimentações efetuadas;
# Sair – Usuário pode sair do sistema.

#  Lembre de tratar exceções. Para criar o programa, utilize a seguinte estrutura de dicionário:

class InvalidOptionError(BaseException):
  pass

class NegativeValueError(BaseException):
  pass

class TransactionLimitError(BaseException):
  pass

class BalanceError(BaseException):
  pass

def menu():
  while True:
    try:
      print("\n\n### MENU INICIAL ###")
      print("1. Depositar")
      print("2. Sacar")
      print("3. Extrato")
      print("4. Histórico de movimentações")
      print("5. Sair")

      opcao = int(input("\n> Digite sua opção: "))

      if opcao < 1 or opcao > 5:
        raise InvalidOptionError

      return opcao
    except ValueError:
      print("[ERROR] O valor digitado não é um número válido")
    except InvalidOptionError:
      print("[ERROR] O valor digitado não é uma opção válida")

def depositar(bank):
  try:
    print("\n # Depositar")
    valor = float(input("> Digite o valor que deseja depositar: "))

    if valor <= 0:
      raise NegativeValueError

    bank["balance"] += valor
    bank["historic"].append(f"Deposito de R$ {valor}")
  except ValueError:
    print("[ERROR] O valor digitado não é válido")
  except NegativeValueError:
    print("[ERROR] O valor digitado deve ser maior que zero")
  else:
    print("\nDeposito efetuado com sucesso!")
  finally:
    return bank

def sacar(bank):
  try:
    print("# Sacar")
    valor = float(input("> Digite o valor que deseja sacar: "))

    if valor <= 0:
      raise NegativeValueError
    
    if valor > bank["transaction_limit"]:
      raise TransactionLimitError
    
    if valor > bank["balance"]:
      raise BalanceError

    bank["balance"] -= valor
    bank["historic"].append(f"Saque de R$ {valor}")
  except ValueError:
    print("[ERROR] O valor digitado não é válido")
  except NegativeValueError:
    print("[ERROR] O valor digitado deve ser maior que zero")
  except TransactionLimitError:
    print(f"[ERROR] O valor de saque é maior que o limite R$ {bank['transaction_limit']}")
  except BalanceError:
    print("[ERROR] Você está tentando sacar mais que seu valor em conta")
  else:
    print("\nSaque efetuado com sucesso!")
  finally:
    return bank
  
def extrato(bank):
  print("# Extrato")
  print(f"Seu saldo atual é de: R$ {bank['balance']}")

def historico(bank):
  print("# Histórico de movimentações")

  for i in range(len(bank["historic"])):
    print(f"> {bank['historic'][i]}")


def main():
  bank = {
    "balance": 0,
    "transaction_limit": 1000,
    "historic": []
  }

  while True:
    opcao = menu()

    if opcao == 1:
      bank = depositar(bank)
    elif opcao == 2:
      bank = sacar(bank)
    elif opcao == 3:
      extrato(bank)
    elif opcao == 4:
      historico(bank)
    elif opcao == 5:
      print("\n\nObrigado por utilizar o sistema!")
      print("\nAté logo :)")
      break

main()