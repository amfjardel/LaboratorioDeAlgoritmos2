def nomeandoarquivo():
    try:
        nome = input("Digite o nome do arquivo:")
    except OSError:
        print ("O arquivo teve um problema.")
    else:
        return nome

def manipulandoaqruivos(nome):
    try:
      my_file = open (f"files/atividade-em-grupos/grupo-03/{nome}.txt","r")

      my_file2 = open (f"files/atividade-em-grupos/grupo-03/copy{nome}.txt","w")

      filetext = my_file.read()

      my_file2.write (filetext)

      my_file.close()
      my_file2.close()
    except OSError:
        print ("O arquivo teve um problema.")
    
def main():
    name = nomeandoarquivo()
    manipulandoaqruivos(name)
main()