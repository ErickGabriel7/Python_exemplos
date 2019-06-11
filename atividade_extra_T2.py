#Universidade Federal Rural de Pernambuco
#Unidade Acadêmica do Cabo de Santo Agostinho
#Monitoria de Linguagem de Programação
#Gabarito da atividade extra - tipo 2
#Erick Gabriel de Lima Silva


from pylab import *
print("ORGANIZADOR DE SERIES DE TV")

#declarando as variáveis
series = []
episodios = []
total = []
add_s = ""
add_ep = 0
add_tot = 0
executar = True

#Criação do menu:
#O programa deverá executar até que seja solicitado sair,
#então, usaremos um comando de repetição
while executar:
    #declarando a variável que perguntará a opção desejada ao usuário
    opc = int(input("\nDigite o numero da opcao desejada: \n1 - Adicionar serie de TV" + "\n2 - Pesquisar serie de TV" + "\n3 - Gerar lista de séries"+ "\n4 - Plotar gráfico das séries\n" +"5 - Sair\n"))

    #Se a opção desejada for a 1...
    if opc == 1:
        #o programa perguntará pelo nome da série até que o usuário digite "0"
        print("Não deixe os espaços a seguir em branco.")

        while add_s != "0":
            add_s = input("\nDigite o nome da serie de TV, ou digite 0 para sair: ")
            #Mas, se o usuário já digitar 0, o programa não precisará perguntar sobre os episódios
            if add_s != "0":
                #perguntará pelo ultimo episódio assistido
                add_ep = int(input("Digite o numero do ultimo episodio assistido: "))

                #perguntará pelo total
                add_tot = int(input("Digite a quantidade total de episódios: "))
                #Precisamos verificar se a série já foi adicionada
                c = 0
                achou = False
                while c < len(episodios):
                    if add_s == episodios[c]:
                        achou = True
                    c += 1

                #lembrando que a quantidade de ep. assistidos não pode ser maior que a quantidade de ep. existentes
                #Fazendo a verificação dos dados do usuário:
                if add_ep <= add_tot and achou == False:
                    #Adicionará essa informação na lista 'episodios'
                    episodios.append(add_ep)
                    # Adicionará essa informação na lista 'series'
                    series.append(add_s)
                    #E adicionará essa informação na lista 'total'
                    total.append(add_tot)
                else:
                    print("O número de episódios assistidos é maior que o número de episódios existentes \n ou a série já foi inserida, digite novamente!")

    #Se a opção desejada for a 2...
    elif opc == 2:
        #declaramos uma variável para fazer uma busca
        search = input("Digite o nome da serie: ")
        #e procuraremos a posição em que essa série está
        #e verificamos se realmente há uma série com este nome
        contador = 0
        posicao = 0
        achou = False
        while contador < len(series):
            if search == series[contador]:
                posicao = contador
                achou = True
            contador = contador + 1
        #Se sim, informar ao usuario
        if achou:
            percentagem=(episodios[posicao]/total[posicao])*100
            print("\nSerie: ", series[posicao] ,"\nVoce parou no episodio", episodios[posicao],"\n", percentagem,"% concluído")
        else:
            print("Serie nao encontrada, tente novamente.")

    elif opc == 3:
        #Declarando uma variável 'lista', que servirá para imprimir a
        #lista de séries em ordem alfabética, mas sem
        #alterar a ordem de séries-episódios, que são precisos nas outras opções
        lista = series[:]
        lista.sort()
        #Imprimindo literalmente uma listagem das séries
        print("Minhas séries")
        c = 0
        while c < len(lista):
            print(lista[c])
            c += 1
        #Calculando o percentual total de episódios assistidos
        #(quant. de ep. assistidos / quant.  de ep. ) * 100
        #primeiramente iremos fazer uma lista contendo a razão ep. assistidos/ep. totais
        #de cada série
        c = 0
        tot_ep = 0
        while c < len(episodios):
            tot_ep = tot_ep + episodios[c]
            c += 1
        c = 0
        tot_tot = 0
        while c < len(total):
            tot_tot += total[c]
            c += 1
        percentagem_geral = (tot_ep / tot_tot)*100
        print(percentagem_geral,"% de episódios assistidos.")

    #Se a opção desejada for a 4...
    elif opc == 4:
        #O programa precisará de uma lista com o percentual assistido de cada série
        percentual = []
        c = 0
        while c < len(series):
            por = (episodios[c]/total[c])*100
            percentual.append(por)
            c+=1
        # Definindo os parâmetros do gráfico
        title('Percentual de episódios assistidos')
        xlabel('Séries')
        ylabel('%')
        #Definindo um espaçamento de +0.5
        pos = arange(len(series)) + 0.5

        # Plotando
        bar(pos, percentual, align='center', color='b')
        xticks(pos, series, rotation=30, size='small')
        grid(True)
        show()
    #Se a opção desejada for a 5...
    elif opc == 5:
        print("Obrigado por utilizar o programa!")
        #O programa irá fechar.
        executar = False
    # Se o usuário digitar qualquer outra opção:
    else:
        print("Digite uma opção válida!")