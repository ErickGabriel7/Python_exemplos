#Universidade Federal Rural de Pernambuco
#Unidade Acadêmica do Cabo de Santo Agostinho
#Monitoria de Linguagem de Programação
#Gabarito da atividade extra - tipo 1
#Erick Gabriel de Lima Silva


from pylab import *
print("BOLETIM")

#Declarando as variáveis
nomes = []
nota1 = []
nota2 = []
add_nome = ""
add_n1 = 0
add_n2 = 0
executar = True

#Criação do menu:
#O programa deverá executar até que seja solicitado sair,
#então, usaremos um comando de repetição
while executar:
    #declarando a variável que perguntará a opção desejada ao usuário
    opc = int(input("\nDigite o numero da opcao desejada: \n1 - Adicionar nome" + "\n2 - Consultar notas" + "\n3 - Gerar Boletim"+ "\n4 - Plotar gráfico das médias\n" + "5 - Sair\n"))

    # Se a opção desejada for a 1...
    if opc == 1:
        #O programa perguntará pelo nome completo do aluno até que o usuário digite "0"
        print("Não deixe os espaços a seguir em branco.")
        while add_nome != "0":
            add_nome = input("\nDigite o nome completo do aluno, ou 0 para sair da opção: ")
            #Mas, se o usuário digitar "0", não será preciso perguntar sobre as notas
            if add_nome != "0":
                #O programa perguntará a 1ª nota
                add_n1 = float(input("Digite a primeira nota deste aluno: "))
                # Perguntará a 2ª nota
                add_n2 = float(input("Digite a segunda nota deste aluno: "))

                #precisamos verificar se já há alguém com este nome na turma
                c = 0
                mesmoNome = False
                while c < len(nomes):
                    if add_nome == nomes[c]:
                        mesmoNome = True
                    c += 1
                #Lembrando que as notas tem que ser entre 0 e 10
                #Fazendo a verificação geral
                if 0 <= add_n1 <= 10 and 0 <= add_n2 <= 10 and mesmoNome == False:
                    #Adicionando os dados válidos as listas
                    nomes.append(add_nome)
                    nota1.append(add_n1)
                    nota2.append(add_n2)
                else:
                    print("Nome já existente ou nota inválida!")
        # Se a opção desejada for a 2...
    elif opc == 2:
        # declaramos uma variável para fazer uma busca
        search = input("Digite o nome do aluno: ")
        # e procuraremos a posição em que o aluno está
        contador = 0
        posicao = 0
        achou = False
        while contador < len(nomes):
            if search == nomes[contador]:
                achou = True
                posicao = contador
            contador += 1
        #se o programa achar, devemos prosseguir
        if achou:
            #calcularemos a média do aluno
            media_aluno = (nota1[posicao]+nota2[posicao])/2
            #E imprimiremos o que foi pedido
            print("Aluno:", nomes[posicao])
            print("Nota 1:", nota1[posicao], "\nNota 2:", nota2[posicao], "\nMédia:", media_aluno)
        else:
            print("Nome não encontrado, tente novamente.")
    # Se a opção desejada for a 3...
    elif opc == 3:
        # Declarando uma variável 'ata', que servirá para imprimir a
        # ata em ordem alfabética, mas sem
        # alterar a ordem de nomes-notas, que são precisos nas outras opções
        boletim = nomes[:]
        boletim.sort()
        # Imprimindo literalmente uma lista de nomes
        print("Boletim\n")
        c = 0
        while c < len(boletim):
            print(boletim[c])
            c += 1
        #Calculando a média geral
        #media_geral = soma das médias de cada aluno / quant. de alunos
        #Obtendo a soma das médias de cada aluno:
        soma_medias = 0
        c = 0
        while c < len(nomes):
            media_aluno = (nota1[c] + nota2[c])/2
            soma_medias += media_aluno
            c += 1
        media_geral = soma_medias/len(nomes)
        print("\nMedia geral da turma:", media_geral)
    #Se a opção desejada for a 4...
    elif opc == 4:
        #para plotar o gráfico, precisamos de uma lista com todas as médias
        media_aluno_lista = []
        c = 0
        while c < len(nomes):
            media = (nota1[c] + nota2[c])/2
            media_aluno_lista.append(media)
            c += 1

        #Definindo um espaçamento para o gráfico de +0.5
        pos = arange(len(nomes)) + 0.5
        #Definindo os parâmetros do gráfico
        title('Média dos alunos')
        xlabel('Alunos')
        ylabel('Média')
        #Plotando
        bar(pos, media_aluno_lista, align='center', color='b')
        xticks(pos, nomes, rotation=30, size='small')
        grid(True)
        show()
    # Se a opção desejada for a 5...
    elif opc == 5:
        #O programa acabará
        executar = False
    #Se o usuário digitar qualquer outra opção:
    else:
            print("Digite uma opção válida!")