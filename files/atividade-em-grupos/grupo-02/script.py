def encontrar_palavra():
    encontrado = False
    sla=0
    try:
        open_file = open(
            "files/atividade-em-grupos/grupo-02/trabalho.txt",
            "r",
        )

        palavra_escolhida = input("Digite a palavra que quer buscar: ")
        
        lista = open_file.readlines()

        for i in range(len(lista)):
            if palavra_escolhida in lista[i]:
                encontrado = True
                sla=i
            

        if encontrado:
            print("Linha número:", sla+1)
            open_file.close()
            return


        else:
           print('[ERROR]: Valor não aceito')


    except FileExistsError as err:
        print(f'[ERROR]: o arquivo não existe, {err}')


encontrar_palavra()
