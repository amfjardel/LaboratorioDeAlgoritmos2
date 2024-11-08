def alunosnotas():
    alunos = open("files/atividade-em-grupos/grupo-06/alunos.txt", 'r')
    notas = open("files/atividade-em-grupos/grupo-06/notas.txt", 'r')
    notasAlunos = open("files/atividade-em-grupos/grupo-06/sair.txt", 'w')

    for i in range(3):
        alunoMedia = []
        soma = 0
        lerAluno = alunos.readline().replace("\n", "")
        ler = notas.readline()
        ler2 = ler.split(" ")
        print(ler2)
        for i in range(3):
            trans = float(ler2[i])
            soma  = soma + trans
        media = soma / 3
        mediaString = str(media)

        notasAlunos.write(f"{lerAluno} - {mediaString}\n")
        # alunoMedia.append(lerAluno)
        # alunoMedia.append(mediaString)
        # notasAlunos.writelines(alunoMedia)
alunosnotas() 
