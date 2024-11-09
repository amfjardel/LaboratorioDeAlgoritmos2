def main():
  my_file = open("files/append.txt", "a")
  nome = input("Digite seu nome: ")
  my_file.write(f"{nome}\n")

main()